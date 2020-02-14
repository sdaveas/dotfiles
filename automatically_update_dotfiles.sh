#!/bin/bash

python update.py

pushd . > /dev/null
cd /home/stelios/etc/dotfiles
if git diff-index --quiet HEAD --; then
    echo "No changes" > /dev/null
else
    echo "Some dotfiles are changed"
    read -p "Update? (Y/n) " answer
    answer=${answer:-y}
    while true; do
        case $answer in
            [Yy]* )
                git diff HEAD~1
                echo "Commiting changes ...";
                git add $(git diff --name-only)
                read -p "Commit message: (default is Automatically commited changes) " message
                message=${message:-"Automatically commited changes"}
                echo $message
                git commit -m "$message";
                echo "... OK";
                break;;
            [Nn]* ) break;;
        esac
        read -p "Update? (Y/n) " answer
    done
fi
popd > /dev/null
