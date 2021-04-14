#!/bin/bash

git add ./

if [ -z $1 ]; then
    git commit -m "Push by lazyPush.sh."
else
    git commit -m "$1"
fi

git push

echo "Push finished."