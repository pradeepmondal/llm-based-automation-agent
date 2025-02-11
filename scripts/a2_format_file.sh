#!/bin/bash

prettier_version="$1"
file_path="$2"

apt-get install nodejs npm
npm install -g npx

npx prettier@"$prettier_version" --write "$file_path"