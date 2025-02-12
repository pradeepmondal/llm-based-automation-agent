#!/bin/bash

prettier_version="$1"
file_path="$2"

# Update package lists
apt-get update

# Install dependencies
apt-get install -y curl

# Install nvm (Node Version Manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash

# Source nvm script
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

# Install a specific version of Node.js
nvm install 20.17.0
nvm use 20.17.0

# Install Prettier using npm
npm install -g prettier@"$prettier_version"

# Run Prettier on the specified file
npx prettier@"$prettier_version" --write "$file_path"