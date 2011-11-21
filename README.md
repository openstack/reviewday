# ReviewDay

HTML report generator for OpenStack code reviews. Launchpad meets SmokeStack and Gerrit.

Based on and inspired by 'reviewlist' by Thierry Carez.

## Description

HTML report generator which creates a prioritized review list w/ function test results. The report includes:

* Prioritized listing of merge proposals by project
* Direct links to gerrit code reviews
* Direct links to test results for each branch (Unit, Libvirt, XenServer)

## Installation

Install directly from pip (requires liblaunchpad and cheetah):

	pip install reviewday

You'll also need a working gerrit setup: http://wiki.openstack.org/GerritWorkflow
Specifically you'll need to be able to run gerrit command line queries.

## Execution

	reviewday

An output directory called 'out_report' is generated in your working directory.
