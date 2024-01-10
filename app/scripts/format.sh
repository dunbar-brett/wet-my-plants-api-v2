#!/bin/sh -e
set -x

# look up more options here: like --alphabetical-sort for imports, maybe --import-order-by=pylint

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place app --exclude=__init__.py
black app
isort --recursive --apply app