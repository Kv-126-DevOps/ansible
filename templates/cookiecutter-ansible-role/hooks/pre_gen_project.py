#!/usr/bin/env python
from re import match
from sys import exit


def check_role_name():
    # Role Naming Convention according to https://galaxy.ansible.com/docs/contributing/creating_role.html#role-names
    role_name_regex = r'^[_a-z0-9]+$'

    role_name = '{{ cookiecutter.role_name }}'

    if not match(role_name_regex, role_name):
        print('ERROR: \"%s\" is not a valid role name!\n'
              'Valid name includes lowercase letters, numbers, and underscores\n' % role_name)

        # exits with status 1 to indicate failure
        exit(1)


if __name__ == '__main__':
    check_role_name()
