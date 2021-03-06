GitLab Runner [![Build Status](https://api.travis-ci.org/thozza/ansible-gitlab-runner.svg?branch=master)](https://travis-ci.org/thozza/ansible-gitlab-runner) [![Ansible Role](https://img.shields.io/badge/role-thozza.gitlab--runner-blue.svg)](https://galaxy.ansible.com/thozza/gitlab-runner/)
=============

This role will install the [official GitLab Runner](https://gitlab.com/gitlab-org/gitlab-ci-multi-runner)

Requirements
------------

This role requires Ansible 2.0 or higher.

Role Variables
--------------

`gitlab_runner_concurrent`
The maximum number of jobs to run concurrently.
Defaults to the number of processor cores.

`gitlab_runner_registration_token`
The GitLab registration token. If this is specified, a runner will be registered to a GitLab server.

`gitlab_runner_coordinator_url`
The GitLab coordinator URL.
Defaults to `https://gitlab.com/ci`.

`gitlab_runner_description`
The description of the runner.
Defaults to the hostname.

`gitlab_runner_executor`
The executor used by the runner.
Defaults to `shell`.

`gitlab_runner_docker_image`
The default Docker image to use. Required when executor is `docker`.

`gitlab_runner_tags`
The tags assigned to the runner,
Defaults to an empty list.

See the [config for more options](https://github.com/thozza/ansible-gitlab-runner/blob/master/tasks/register-runner.yml)

Example Playbook
----------------
```yaml
- hosts: all
  remote_user: root
  vars_files:
    - vars/main.yml
  roles:
    - { role: thozza.gitlab-runner }
```

Inside `vars/main.yml`
```yaml
gitlab_runner_registration_token: 'HUzTMgnxk17YV8Rj8ucQ'
gitlab_runner_description: 'Example GitLab Runner'
gitlab_runner_tags:
  - node
  - ruby
  - mysql
gitlab_runner_docker_volumes:
  - "/var/run/docker.sock:/var/run/docker.sock"
  - "/cache"
```

License
-------

MIT

Author Information
------------------

Original author is [Harold Barker](https://github.com/haroldb/ansible-gitlab-runner). This version is a fork of a fork by [Erik-jan Riemers](https://github.com/riemers/ansible-gitlab-runner).

This version reworks the installation of the runner, to work also on Fedora. Contributions are welcomed.
