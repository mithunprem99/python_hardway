#!/bin/bash

# Set your Git credentials and repository information
USERNAME="your_username"
TOKEN="your_token"
REPO_URL="https://github.com/your_username/your_repo.git"

# Get the current branch name
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

# Add and commit changes
git add .
git commit -m "Commit message"

# Push to remote
git push $REPO_URL $CURRENT_BRANCH --quiet << EOF
${TOKEN}
EOF


