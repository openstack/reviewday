import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="reviewday",
    version="0.2.0",
    author="Dan Prince",
    author_email="dan.prince@rackspace.com",
    description=("Report generator for OpenStack code reviews."),
    license="BSD",
    keywords="OpenStack HTML report generator",
    url="https://github/dprince/reviewday",
    packages=['reviewday'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    scripts=['bin/reviewday'],
    data_files=[
        ('reviewday', ['reviewday/report.html']),
        ('reviewday/report_files', [
         'reviewday/report_files/arrowBlank',
         'reviewday/report_files/arrowDown',
         'reviewday/report_files/arrowUp',
         'reviewday/report_files/combo.css',
         'reviewday/report_files/CRITICALBUGFIX.png',
         'reviewday/report_files/ESSENTIALFEATURE.png',
         'reviewday/report_files/HIGHBUGFIX.png',
         'reviewday/report_files/HIGHFEATURE.png',
         'reviewday/report_files/LOWBUGFIX.png',
         'reviewday/report_files/LOWFEATURE.png',
         'reviewday/report_files/MEDIUMBUGFIX.png',
         'reviewday/report_files/MEDIUMFEATURE.png',
         'reviewday/report_files/NOLINK.png',
         'reviewday/report_files/REGRESSIONHOTFIX.png',
         'reviewday/report_files/RELEASECRITICALBUG.png',
         'reviewday/report_files/sorting.js',
         'reviewday/report_files/UNDECIDEDBUGFIX.png',
         'reviewday/report_files/UNTARGETEDFEATURE.png',
         'reviewday/report_files/WISHLISTBUGFIX.png',
         ])
    ],
    install_requires=[
        "launchpadlib",
        "cheetah",
    ],
)
