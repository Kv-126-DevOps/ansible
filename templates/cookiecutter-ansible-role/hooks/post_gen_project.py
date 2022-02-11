#!/usr/bin/env python
from os import remove, path
from shutil import rmtree
from cookiecutter.prompt import read_user_yes_no

optional_folders_list = ['handlers', 'templates', 'files']


def configure_folders():
    for folder in optional_folders_list:
        if read_user_yes_no('Should it have {}?'.format(folder), default_value=u'no'):
            try:
                # '.empty' file has to be there, git doesn't store empty folders
                remove(path.join(folder, '.empty'))
            except OSError:
                pass
        else:
            rmtree(folder)


def crete_cleanup_file():
    global cleanup_file
    if '{{ cookiecutter.molecule_driver }}' == "delegated":
        try:
            cleanup_file = open("molecule/default/cleanup.yml", "w")
            cleanup_file.write("---\n")
        except IOError:
            print("Unable to create file on disk.")
        finally:
            cleanup_file.close()


if __name__ == '__main__':
    configure_folders()
    crete_cleanup_file()
