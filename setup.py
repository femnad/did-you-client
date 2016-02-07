#!/usr/bin/env python
import setuptools

setuptools.setup(
    name='did_you_client',
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={'console_scripts':
                  ['did_you_client = did_you_client.command:run_client',
                   'did_you_checker = did_you_client.command:run_checker']},
    )
