#!/bin/bash
# install.sh: Script to install uv (Python package manager)

set -e


# Install uv using curl (no pip or pipx required)
curl -Ls https://astral.sh/uv/install.sh | bash

echo "uv installation complete."
