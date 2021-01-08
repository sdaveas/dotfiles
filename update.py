#!/bin/python
"""
Checks if there are changes at any versioned dotfiles
Called by automate.sh, which is recommended to add in your {bash/zsh}rc
"""

import subprocess


def check_for_changes():
    """
    Prompts a message if there are changes
    """

    command = str("git status")
    command_list = command.split(" ")

    out = subprocess.Popen(
        command_list, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    git_status = str(out.communicate()[0].decode("utf-8")).splitlines()

    changed_files = []

    for line in git_status:
        if "modified" in line:
            changed_files.append(line.split(":")[1].strip(" "))

    changed = len(changed_files)
    if changed <= 0:
        return
    if changed == 1:
        print("There is a changed dotfile: ", end="")
    elif changed > 1:
        print("There are", len(changed_files), "changed dotfiles: ", end="")

    for changed in changed_files:
        print(changed, end=" ")

    print("")


def update():
    """
    Updates the content of dotfiles
    """

    command = "find -type f"
    command_list = command.split(" ")

    out = subprocess.Popen(
        command_list, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )

    files = str(out.communicate()[0].decode("utf-8")).splitlines()

    home = "/home/stelios/"

    for versioned_file in files:
        if versioned_file.startswith("./.git"):
            continue
        home_file = home + versioned_file
        command = ["rsync", home_file, versioned_file]
        subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


update()
check_for_changes()
