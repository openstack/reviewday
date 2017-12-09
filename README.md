# ReviewDay

HTML report generator for OpenStack code reviews. Launchpad meets Gerrit.

Inspired by 'reviewlist' scripts written by Thierry Carez.

## Description

HTML report generator which creates a prioritized review list w/ function test results. The report includes:

* Prioritized listing of merge proposals by project
* Direct links to gerrit code reviews
* Direct links to test results for each branch (Unit, Libvirt, XenServer)

## Installation

1. Git clone the project.
2. Install Python libraries for launchpadlib and cheetah.
3. Setup your ssh credentials to work w/ Gerrit. See http://docs.openstack.org/infra/manual/developers.html#development-workflow for details.

```bash
	$ cat ~/.ssh/config 
	Host review
	  Hostname review.openstack.org
	  Port 29418
	  User dan-prince
```


## Execution

	PYTHONPATH=$PWD ./bin/reviewday

An output directory called 'out\_report' is generated in the current directory.

Alternately you can execute reviewday in a tox environment by using:

       tox -erun

## Customizing the projects

If you wish to customize the output of reviewday you can use the -p (--project-file) option to provide a custom project names file. This file should be
a valid YAML/JSON file formatted like this:

	projects:
	  - name: dib-utils
	  - name: diskimage-builder
	  - name: tripleo-heat-templates
	    launchpad_project: tripleo
	  - name: tripleo-image-elements
	    launchpad_project: tripleo
	  - name: tripleo-incubator
	    launchpad_project: tripleo
          #Add a custom namespace like this. Defaults to 'openstack/'
	  - name: openstack-infra/tripleo-ci
	    launchpad_project: tripleo

## License

See LICENSE.txt for further details.
