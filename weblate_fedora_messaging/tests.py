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

from django.test.utils import modify_settings
from weblate.auth.models import User
from weblate.trans.models import Change, Project
from weblate.trans.tests.test_views import FixtureTestCase

from .tasks import get_change_body, get_change_topic


class FedoraTestCase(FixtureTestCase):
    def test_topic(self):
        for change in Change.objects.all():
            self.assertIsNotNone(get_change_topic(change))

    def test_body(self):
        for change in Change.objects.all():
            self.assertIsNotNone(get_change_body(change))

    @modify_settings(INSTALLED_APPS={"append": "weblate_fedora_messaging"})
    def test_create(self):
        user = User.objects.get(username="testuser")
        project = Project.objects.all()[0]
        Change.objects.create(
            action=Change.ACTION_REMOVE_PROJECT, target="test", user=user
        )
        Change.objects.create(
            action=Change.ACTION_REMOVE_COMPONENT,
            project=project,
            target="test",
            user=user,
            author=User.objects.get(username="jane"),
        )
        self.edit_unit('Hello, world!\n', 'Ahoj svete!\n')
