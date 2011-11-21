# ReviewDay

HTML report generator for OpenStack code reviews. Launchpad meets SmokeStack and Gerrit.

Inspired by 'reviewlist' scripts written by Thierry Carez.

## Description

HTML report generator which creates a prioritized review list w/ function test results. The report includes:

* Prioritized listing of merge proposals by project
* Direct links to gerrit code reviews
* Direct links to test results for each branch (Unit, Libvirt, XenServer)

## Installation

1. Git clone the project.
2. Install Python libraries for launchpadlib and cheetah.
3. Setup your ssh credentials to work w/ Gerrit. See http://wiki.openstack.org/GerritWorkflow for details.

```bash
	$ cat ~/.ssh/config 
	Host review
	  Hostname review.openstack.org
	  Port 29418
	  User dan-prince
```


## Execution

	PYTHONPATH=$PWD ./bin/reviewday

An output directory called 'out_report' is generated in the current directory.
