.. image:: https://s.weblate.org/cdn/Logo-Darktext-borders.png
   :alt: Weblate
   :target: https://weblate.org/
   :height: 80px

**Weblate is a copylefted libre software web-based continuous localization system,
used by over 1150 libre projects and companies in more than 115 countries.**


Fedora messaging integration for Weblate.

.. image:: https://img.shields.io/badge/website-weblate.org-blue.svg
    :alt: Website
    :target: https://weblate.org/

.. image:: https://hosted.weblate.org/widgets/weblate/-/svg-badge.svg
    :alt: Translation status
    :target: https://hosted.weblate.org/engage/weblate/?utm_source=widget

.. image:: https://bestpractices.coreinfrastructure.org/projects/552/badge
    :alt: CII Best Practices
    :target: https://bestpractices.coreinfrastructure.org/projects/552

.. image:: https://img.shields.io/pypi/v/weblate-fedora-messaging.svg
    :target: https://pypi.org/project/weblate-fedora-messaging/
    :alt: PyPI package

.. image:: https://readthedocs.org/projects/weblate/badge/
    :alt: Documentation
    :target: https://docs.weblate.org/

Installation
------------

Install from PyPI:

.. code-block:: sh

    pip install weblate-fedora-messaging

Sources are available at <https://github.com/WeblateOrg/fedora_messaging>.

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
   Verbose name of the change, see `Change actions source code`_ for possible values
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


.. _Change actions source code: https://github.com/WeblateOrg/weblate/blob/master/weblate/trans/models/change.py#L218


Example messages
----------------

Repository merge event:

.. code-block:: json

    {
      "id": 1,
      "action": "Merged repository",
      "timestamp": "2017-06-15T11:30:47.325000+00:00",
      "url": "http://example.com/projects/test/test/",
      "component": "test"
    }

New source string event:

.. code-block:: json

    {
      "id": 2,
      "action": "New source string",
      "timestamp": "2017-06-15T11:30:47.372000+00:00",
      "url": "http://example.com/translate/test/test/cs/?checksum=6412684aaf018e8e",
      "component": "test",
      "translation": "cs",
      "source": "Hello, world!\n"
    }

Resource update event:

.. code-block:: json

    {
      "id": 6,
      "action": "Resource update",
      "timestamp": "2017-06-15T11:30:47.410000+00:00",
      "url": "http://example.com/projects/test/test/cs/",
      "project": "test",
      "component": "test",
      "translation": "cs"
    }
    {
      "id": 7,
      "action": "Resource update",
      "timestamp": "2017-06-15T11:30:47.510000+00:00",
      "url": "http://example.com/projects/test/test/de/",
      "project": "test",
      "component": "test",
      "translation": "de"
    }
    {
      "id": 8,
      "action": "Resource update",
      "timestamp": "2017-06-15T11:30:47.595000+00:00",
      "url": "http://example.com/projects/test/test/it/",
      "project": "test",
      "component": "test",
      "translation": "it"
    }

Project removal event:

.. code-block:: json

    {
      "id": 9,
      "action": "Removed project",
      "timestamp": "2019-10-17T15:57:08.559420+00:00",
      "target": "test",
      "user": "testuser"
    }

New contributor event:

.. code-block:: json

    {
      "id": 11,
      "action": "New contributor",
      "timestamp": "2019-10-17T15:57:08.759960+00:00",
      "url": "http://example.com/translate/test/test/cs/?checksum=6412684aaf018e8e",
      "author": "testuser",
      "user": "testuser",
      "project": "test",
      "component": "test",
      "translation": "cs",
      "source": "Hello, world!\n"
    }

New translation event:

.. code-block:: json

    {
      "id": 12,
      "action": "New translation",
      "timestamp": "2019-10-17T15:57:08.772591+00:00",
      "url": "http://example.com/translate/test/test/cs/?checksum=6412684aaf018e8e",
      "target": "Ahoj svete!\n",
      "author": "testuser",
      "user": "testuser",
      "project": "test",
      "component": "test",
      "translation": "cs",
      "source": "Hello, world!\n"
    }
