---
plugin_type: provision
subparsers:
    docker:
        description: Create and run containers using Ansible modules
        include_groups: ['Ansible options', 'Inventory', 'Common options', 'Answers file']
        groups:
            - title: docker
              options:

                  name:
                      type: Value
                      help: The name of the container

                  image:
                      type: Value
                      help: The name of the image to use with docker
                      default: python:2.7-slim

                  run:
                      type: Bool
                      default: yes
                      help: Run the container after creation

                  command:
                      type: Value
                      default: None
                      help: The command to execute when running the container

                  create:
                      type: Bool
                      default: no
                      help: Create the container

                  remove:
                      type: Bool
                      default: no
                      help: Remove the container

                  registry:
                      type: Value
                      help: The address for the docker registry to use
                      default: rhos-qe-mirror-tlv.usersys.redhat.com

                  list-images:
                      type: Bool
                      help: List the existing images in the registry
                      default: no

                  list-tags:
                      type: Bool
                      help: List all the tags of a specific image (you have to specify image with --image)
                      default: no
