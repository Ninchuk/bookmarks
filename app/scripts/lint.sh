#!/bin/bash

set -e
set -x

isort --diff .
flake8 .
