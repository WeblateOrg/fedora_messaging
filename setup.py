#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2012 - 2019 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <https://weblate.org/>
#

import os

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    LONG_DESCRIPTION = readme.read()

setup(
    name="weblate_fedora_messaging",
    version="0.1",
    packages=["weblate_fedora_messaging"],
    include_package_data=True,
    license="MIT",
    description="Weblate Fedora Messaging integration",
    long_description=LONG_DESCRIPTION,
    long_description_content_typ="text/x-rst",
    keywords="i18n l10n gettext git mercurial translate",
    url="https://weblate.org/",
    author="Michal Čihař",
    author_email="michal@cihar.com",
    install_requires=["Weblate"],
    zip_safe=False,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Internationalization",
        "Topic :: Software Development :: Localization",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
