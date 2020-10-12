#!/usr/bin/env python
#
# Copyright © 2012 - 2020 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <https://weblate.org/>
#

from setuptools import setup

with open("README.rst") as handle:
    LONG_DESCRIPTION = handle.read()

with open("requirements.txt") as handle:
    REQUIRES = handle.read().split()

with open("requirements-test.txt") as handle:
    REQUIRES_TEST = handle.read().split()

setup(
    name="weblate_fedora_messaging",
    version="0.3",
    author="Michal Čihař",
    author_email="michal@cihar.com",
    description="Weblate Fedora Messaging integration",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/x-rst",
    license="GPLv3+",
    keywords="i18n l10n gettext git mercurial translate",
    url="https://weblate.org/",
    download_url="https://github.com/WeblateOrg/fedora_mesaging",
    project_urls={
        "Issue Tracker": "https://github.com/WeblateOrg/fedora_messaging/issues",
        "Documentation": "https://docs.weblate.org/",
        "Source Code": "https://github.com/WeblateOrg/fedora_messaging",
        "Twitter": "https://twitter.com/WeblateOrg",
    },
    platforms=["any"],
    packages=["weblate_fedora_messaging"],
    include_package_data=True,
    install_requires=REQUIRES,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Internationalization",
        "Topic :: Software Development :: Localization",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires=">=3.6",
    setup_requires=["pytest-runner"],
    tests_require=REQUIRES_TEST,
)
