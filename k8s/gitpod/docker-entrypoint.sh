#!/bin/sh

set -e

git clone $GITHUB_WORKSPACE app/

# TODO install an array of apt packages

chown -R openvscode-server app/

exec "$@"