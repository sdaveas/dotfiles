#!/bin/python
"""
Runs 'update.py' and checks if there were any changes
"""

import subprocess

def check_for_changes():
    repo_path = '/home/stelios/etc/dotfiles'

    command = str('git -C ' + repo_path + ' status')
    command_list = command.split(' ')

    out = subprocess.Popen(command_list, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    git_status = str(out.communicate()[0].decode('utf-8')).splitlines()

    changed_files = []

    for l in git_status:
        if 'modified' in l:
            changed_files.append(l.split(':')[1].strip(' '))

    changed = len(changed_files)
    if changed <= 0:
        return
    elif changed == 1:
        print('There is a changed dotfile: ', end='')
    elif changed > 1:
        print('There are', len(changed_files), 'changed dotfiles: ', end='')

    for c in changed_files:
        print(c, end=' ')

    print("")

check_for_changes()
