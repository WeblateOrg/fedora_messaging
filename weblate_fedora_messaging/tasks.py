# -*- coding: utf-8 -*-
#
# Copyright © 2012 - 2019 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <https://weblate.org/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

from django.core.exceptions import ObjectDoesNotExist
from fedora_messaging.api import Message, publish
from fedora_messaging.exceptions import ConnectionException, PublishReturned
from weblate.celery import app
from weblate.trans.models import Change


def get_change_topic(change):
    scope = "global"
    if change.unit:
        scope = "unit"
    elif change.translation:
        scope = "translation"
    elif change.component:
        scope = "component"
    elif change.project:
        scope = "project"
    return "weblate.{}.{}".format(
        scope, change.get_action_display().lower().replace(" ", "_")
    )


def get_change_body(change):
    result = {
        "id": change.id,
        "action": change.get_action_display(),
        "timestamp": change.timestamp,
        "target": change.target,
        "old": change.old,
    }
    if change.author:
        result["author"] = change.author.username
    if change.user:
        result["user"] = change.user.username
    if change.project:
        result["project"] = change.project.slug
    if change.component:
        result["component"] = change.component.slug
    if change.translation:
        result["translation"] = change.translation.language.code
    result.update(change.details)
    return result


# Retry for not existing object (maybe transaction not yet committed) with
# delay of 10 minutes growing exponentially
@app.task(
    trail=False,
    autoretry_for=(ObjectDoesNotExist, PublishReturned, ConnectionException),
    retry_backoff=600,
    retry_backoff_max=3600,
)
def fedora_messaging_change(change_id):
    change = Change.objects.get(pk=change_id)
    publish(Message(topic=get_change_topic(change), body=get_change_body(change)))
