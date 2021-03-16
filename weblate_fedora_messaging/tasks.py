#
# Copyright © 2012 - 2021 Michal Čihař <michal@cihar.com>
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
from weblate.trans.models import Change
from weblate.trans.util import split_plural
from weblate.utils.celery import app
from weblate.utils.site import get_site_url


def get_change_topic(change):
    """
    Generates a topic for the change.

    Is is in the form weblate.<action>.<project>.<component>.<translation>
    """
    parts = ["weblate", change.get_action_display().lower().replace(" ", "_")]
    if change.project:
        parts.append(change.project.slug)
    if change.component:
        parts.append(change.component.slug)
    if change.translation:
        parts.append(change.translation.language.code)
    return ".".join(parts)


def get_change_body(change):
    result = {
        "id": change.id,
        "action": change.get_action_display(),
        "timestamp": change.timestamp.isoformat(),
    }
    url = change.get_absolute_url()
    if url:
        result["url"] = get_site_url(url)
    if change.target:
        result["target"] = split_plural(change.target)
    if change.old:
        result["old"] = split_plural(change.old)
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
    if change.unit:
        result["source"] = split_plural(change.unit.source)
        result["context"] = split_plural(change.unit.context)
    result.update(change.details)
    return result


def get_change_headers(change):
    result = {
        "action": change.get_action_display(),
    }
    if change.project:
        result["project"] = change.project.slug
    if change.component:
        result["component"] = change.component.slug
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
    publish(
        Message(
            topic=get_change_topic(change),
            headers=get_change_headers(change),
            body=get_change_body(change),
        )
    )
