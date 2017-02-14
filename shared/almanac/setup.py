#!/usr/bin/env python
import os

from setuptools import find_packages, setup

PROJECT_DIR = os.path.dirname(__file__)

if PROJECT_DIR:
    os.chdir(PROJECT_DIR)

setup(
    name='his.almanac',
    version='0.0.1',
    url='',
    author="Jonathan Moss",
    author_email="xirisr@gmail.com",
    description="A services registry",
    long_description=open(os.path.join(PROJECT_DIR, 'README.rst')).read(),
    keywords="registry",
    license='BSD',
    platforms=['linux'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Other/Nonlisted Topic'
    ]
)
