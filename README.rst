Weblate Fedora Messaging integration
====================================

.. image:: https://cloud.drone.io/api/badges/WeblateOrg/fedora_messaging/status.svg
   :target: https://cloud.drone.io/WeblateOrg/fedora_messaging

.. image:: https://travis-ci.com/WeblateOrg/fedora_messaging.svg?branch=master
   :target: https://travis-ci.com/WeblateOrg/fedora_messaging

.. image:: https://codecov.io/gh/WeblateOrg/fedora_messaging/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/WeblateOrg/fedora_messaging

Fedora messaging integration for Weblate.

Installation:

.. code-block:: sh

    pip install weblate-fedora-messaging

Weblate integration:

.. code-block:: python

   # Add to installed apps
   INSTALLED_APPS.append('weblate_fedora_messaging')
   # Path to configuration file
   FEDORA_MESSAGING_CONF = '/etc/fedora-messaging/config.toml'
   # Route messaging to notify queue
   CELERY_TASK_ROUTES['weblate_fedora_messaging.tasks.*'] = {'queue': 'notify'}
