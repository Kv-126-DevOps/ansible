# Jankins

This Ansible Role infuses antigravity, you are warned

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
    - jankins
```

Example of running a playbook via a shell

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

## Testing the role

Test scenarios

| Name      | Description |
| :---      | :---        |
| `default` | Default scenario |

Add here additional information regarding testing your role

## License

MIT

## Contributors

[Anatolii Pedchenko](https://github.com/olyakaya) (maintainer)
