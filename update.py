#!/bin/python
"""
Checks if there are changes at any versioned dotfiles
"""

import subprocess

def check_for_changes():

    command = str('git status')
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

def update():
    command = "find -type f"
    command_list = command.split(' ')

    out = subprocess.Popen(command_list,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)

    files = str(out.communicate()[0].decode('utf-8')).splitlines()

    home = '/home/stelios/'

    for versioned_file in files:
        if versioned_file.startswith('./.git'):
            continue
        home_file = home + versioned_file
        command = ['rsync', home_file, versioned_file]
        subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)

update()
check_for_changes()
