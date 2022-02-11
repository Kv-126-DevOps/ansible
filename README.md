# Ansible Roles Repository

## Ansible Version

Current Ansible version is **2.11**

## Repository Rules

- All roles should be created with `cookiecutter` tool
(see details here [templates/cookiecutter-ansible-role/README.md](/templates/cookiecutter-ansible-role#cookiecutter-ansible-role))
- `yaml` extension is preferable

## Molecule Usage

> The created role must be in the `roles/` folder since relative paths are written in
> the `molecule.yml` file for the linters.
> ```plaintext
>   ../../linter_rules/yamllint.yaml
>   ../../linter_rules/ansiblelint/
> ```

### Installation Guide

There are two ways to install and use this tool:
1. Using a container that is used in CI (see instructions below)
1. Install it locally, here is [Installation Guide](https://molecule.readthedocs.io/en/latest/installation.html)

### Testing on the local machine

As a recommendation, it is better to use the same docker image that is used in CI for testing roles.
To do this, simply change the directory to the role for testing and run the docker command as follows

```shell
docker run --rm -it \
    -v "$(dirname $(dirname "${PWD}"))":/tmp/ansible-roles:ro \
    -v /var/run/docker.sock:/var/run/docker.sock \
    --env REGISTRY_DOCKER_ID=$REGISTRY_DOCKER_ID \
    --env REGISTRY_DOCKER_PWD=$REGISTRY_DOCKER_PWD \
    --workdir /tmp/ansible-roles/roles/$(basename "${PWD}") \
    quay.io/ansible/toolset:3.5.0 \
    bash
```

Then you can use any commands of the Molecule tool, e.g.

```shell
molecule test
```

## The configuration file

To use settings from the `ansible.cfg` file, you need to run playbooks in the same directory.
