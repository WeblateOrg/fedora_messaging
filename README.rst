Weblate Fedora Messaging integration
====================================

.. image:: https://cloud.drone.io/api/badges/WeblateOrg/fedora_messaging/status.svg
   :target: https://cloud.drone.io/WeblateOrg/fedora_messaging

.. image:: https://travis-ci.com/WeblateOrg/fedora_messaging.svg?branch=master
   :target: https://travis-ci.com/WeblateOrg/fedora_messaging

.. image:: https://codecov.io/gh/WeblateOrg/fedora_messaging/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/WeblateOrg/fedora_messaging

Fedora messaging integration for Weblate.

Installation
------------

Install from PyPI:

.. code-block:: sh

    pip install weblate-fedora-messaging

Configure Weblate integration:

.. code-block:: python

   # Add to installed apps
   INSTALLED_APPS.append('weblate_fedora_messaging')
   # Path to configuration file
   FEDORA_MESSAGING_CONF = '/etc/fedora-messaging/config.toml'
   # Route messaging to notify queue
   CELERY_TASK_ROUTES['weblate_fedora_messaging.tasks.*'] = {'queue': 'notify'}


Messages
--------

All messages have topic ``weblate.SCOPE.ACTION``. The scope is ``global``,
``project``, ``component``, ``translation`` or ``unit``, action is lowercase
textual representation of action with underscores instead of space, for example
``resource_update``.

The body consists of following fields (given that they are available for the event):

``id``
   Numerical ID of change
``action``
   Verbose name of the change
``timestamp``
   ISO formatted timestamp
``target``
   New value of the change (eg. new translation of the string)
``old``
   Old value of the change (eg. previous translation of the string)
``source``
   Source string.
``url``
   Absolute URL to view the related object.
``author``
   Author username (this can be different from user for example when accepting suggestions)
``user``
   Acting username
``project``
   Project slug
``component``
   Component slug
``translation``
   Translation language code
