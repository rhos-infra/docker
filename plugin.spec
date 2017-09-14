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
                      required: yes

                  image:
                      type: Value
                      help: The name of the image to use with docker
                      default: python:2.7-slim

                  run:
                      type: Bool
                      default: yes
                      help: Run the container after creation

                  create:
                      type: Bool
                      default: no
                      help: Create the container

                  remove:
                      type: Bool
                      default: no
                      help: Remove the container
