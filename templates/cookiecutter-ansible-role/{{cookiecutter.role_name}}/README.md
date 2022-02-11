# {{ cookiecutter.role_name | replace('_', ' ') | title }}

{{ cookiecutter.short_description }}

## Requirements

* Ansible inventory
* etc

## Role Variables

### Default variables

file defaults/main.yaml

| Variable                           | Default                | Description |
| :---                               | :---                   | :---        |
| `` |  |  |

### Сonstant variables

file vars/main.yaml

| Variable                           | Default                | Description |
| :---                               | :---                   | :---        |
| `` |  |  |

## Tags

Tags

| Name          | Description |
| :---          | :---        |
| `` |  |

Possible tag combination usage

| Combination   | Description |
| :---          | :---        |
| --tags `` |  |

## Dependencies

A list of other roles should go here,
plus any details in regard to parameters that may need to be set for other roles,
or variables that are used from other roles.

* common
* etc

## Example Playbook
```yaml
- hosts: all
  gather_facts: no
  roles:
    - {{ cookiecutter.role_name }}
```

Example of running a playbook via a shell
{% raw %}
```bash
ansible-playbook \
--private-key=~/.ssh/devops.pem \
-u devops \
--limit {{ HOST_GROUP }} \
--tags "{{ TAG_LIST }}" \
-i ansible-inventory/ \
ansible/site.yaml \
-e "{{ EXTRA_VARIABLES }}"
```
{% endraw %}
## Testing the role

Test scenarios

| Name      | Description |
| :---      | :---        |
| `default` | Default scenario |

Add here additional information regarding testing your role

## License

MIT

## Contributors

[{{ cookiecutter.full_name }}](https://github.com/{{ cookiecutter.github_user }}) (maintainer)
