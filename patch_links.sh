#!/bin/bash

find . -type f -name "*.md" -exec sed -i -E 's|(https://nextcloud-public\.hoshiyomi-dev\.work/s/[a-zA-Z0-9_-]+)(/download)?|\1/download|g' {} +
