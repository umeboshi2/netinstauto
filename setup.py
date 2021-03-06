#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Jinja2',
    'PyYAML',
    'requests',
]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Joseph Rawson",
    author_email='joseph.rawson.works@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Remaster a netinst iso, and perform preseed auto install.",
    install_requires=requirements,
    license="UNLICENSED",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='netinstauto',
    name='netinstauto',
    packages=find_packages(include=['netinstauto', 'netinstauto.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/umeboshi2/netinstauto',
    version='0.1.0',
    zip_safe=False,
    entry_points="""
    # -*- Entry points: -*-
    [console_scripts]
    nia-check = netinstauto.scripts.nia_check:main
    nia-get-iso = netinstauto.scripts.nia_get_iso:main
    nia-mkconfig = netinstauto.scripts.nia_mkconfig:main
    nia-mkiso = netinstauto.scripts.nia_mkiso:main
    nia-init = netinstauto.scripts.nia_init:main
    """,
)
