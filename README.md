# Docker IR

Docker InfraRed Plugin

## Installation

1. Install infrared (https://github.com/redhat-openstack/infrared)

2. Install docker infrared plugin:

    infrared plugin add https://github.com/rhos-infra/docker.git

## Usage

Create a container without starting it:

    infrared docker --name mario --create yes

Create a conatainer using the image 'centos7' and run it:

    infrared docker --name centos7 --create yes --run yes

Create a container and run /bin/bash:

    infrared docker --create yes --run yes --command /bin/bash

To list all the images in the registry:

    infrared docker --list-images yes

To list all the tags for a specific image:

    infrared docker --list-tags yes --image luigi


## Tests

To run Ansible lint tests, run the following command::

    tox -e ansible-lint

## Contributions

Contributions are done with pull requests :)
