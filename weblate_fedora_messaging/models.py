#
# Copyright © Michal Čihař <michal@weblate.org>
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

from appconf import AppConf
from django.db.models.signals import post_save
from django.dispatch import receiver
from weblate.trans.models import Change
from weblate.utils.decorators import disable_for_loaddata

from .tasks import fedora_messaging_change


@receiver(post_save, sender=Change)
@disable_for_loaddata
def fedora_notify_change(sender, instance, **kwargs):
    fedora_messaging_change.delay(instance.pk)


try:
    from weblate.trans.signals import change_bulk_create
except ImportError:
    pass
else:

    @receiver(change_bulk_create)
    @disable_for_loaddata
    def fedora_notify_change(sender, instances, **kwargs):
        for instance in instances:
            fedora_messaging_change.delay(instance.pk)


class FedoraConf(AppConf):
    FEDORA_MESSAGING_CONF = None

    class Meta:
        prefix = ""
