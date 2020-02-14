#!/bin/bash

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
                git add * && git commit -m "Automatically commited changes";
                echo "... OK";
                break;;
            [Nn]* ) echo "No"; break;;
        esac
        read -p "Update? (Y/n) " answer
    done
fi
python update.py
popd > /dev/null
