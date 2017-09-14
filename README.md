# docker

Docker InfraRed Plugin

*WORK IN PROGRESS*

*This plugin is not ready for use*

## Installation

1. Install infrared (https://github.com/redhat-openstack/infrared)
2. Install docker infrared plugin:

    infrared plugin add <ir_docker_plugin_path>

3. Run the plugin:

    infrared docker -h

## Usage

To create and run docker container:

    infrared docker --name mario --run yes

## Tests

To run Ansible lint tests, run the following command::

    tox -e ansible-lint

## Contributions

Contributions are done with pull requests :)
