# Cookiecutter Ansible Role

[Cookiecutter](https://github.com/audreyr/cookiecutter) recipe to easily create
[ansible roles](http://docs.ansible.com/playbooks_roles.html#roles).

## Features

1. Follows Ansible [best practices](http://docs.ansible.com/playbooks_best_practices.html)
1. Follows Ansible Galaxy [best practices](https://galaxy.ansible.com/intro#good)
1. Only Creates the necessary files and folders
1. Blazing fast creation, forget about file creation and focus in actions
1. Lint checks ([Ansible-lint](https://github.com/ansible/ansible-lint),
[yamllint](https://github.com/adrienverge/yamllint))
1. Test infrastructure already implemented ([Molecule](https://github.com/ansible/molecule))

## Template Usage

1. Install [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html#install-cookiecutter)
version >= 1.7+

   ```shell script
   pip install cookiecutter
   ```
   or
   ```
   brew install cookiecutter
   ```
1. Clone the repository if you don’t have it yet

   ```shell script
   git clone git@github.com:Kv-126-DevOps/ansible.git
   ```
1. Go to the roles folder and run the cookiecutter utility

   ```shell script
   cd ansible/roles
   cookiecutter ../templates/cookiecutter-ansible-role
   ````

   It will ask you questions about the structure of your role.
   You can jump to the next question by entering an empty string.
   Projects are always generated to your current directory.

> Then don't forget to change a tag `{{ cookiecutter.role_name }}_molecule_test` to yours,
> which you are going to use in real work. Moreover, it is possible to add multiple tags, e.g.
> ```yaml
> provisioner:
>  name: ansible
>  options:
>    v: true
>    tags: >-
>      role_install,
>      role_config
> ...
> ```

### Example

```yaml
full_name [Anatolii Pedchenko]: 
gitlab_user [apedc]: 
role_name [super_role]: awesome_role
short_description [This Ansible Role infuses antigravity, you are warned]: 
min_ansible_version [2.9.0]: 
main_docker_image [amazonlinux:2.0.20220121.0]: 
Select molecule_driver:
1 - docker
2 - delegated
Choose from 1, 2 [1]: 
Should it have handlers? [no]: 
Should it have templates? [no]: yes
Should it have files? [no]:
```

Here is the standard role file hierarchy if you used the `docker` driver
```shell
super_role
├── CHANGELOG.md
├── defaults
│   └── main.yaml
├── files
├── handlers
│   └── main.yaml
├── meta
│   └── main.yaml
├── molecule
│   └── default
│       ├── converge.yml
│       ├── molecule.yml
│       ├── prepare.yml
│       └── verify.yml
├── README.md
├── tasks
│   └── main.yaml
└── templates
```

## Usage for existing roles

1. The following commands will create only non-existing files, e.g. a Molecule file hierarchy

   ```shell
   # Go to the roles folder and run the cookiecutter utility
   cd ansible/roles
   # Overwrite the contents of the output directory if it already exists
   cookiecutter -f ../templates/cookiecutter-ansible-role
   # Revert changes to modified files
   git reset --hard
   ```

1. Then check if the same header structure is used in the `README.md` as in the cookiecutter template.
1. After that, configure all the new files according to the requirements for your role.

## Contributors

[Anatolii Pedchenko](https://github.com/anatolek) (maintainer)
