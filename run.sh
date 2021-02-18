#!/bin/bash

docker build -t pennsive/whitestripe .
rm -rf dist
docker run --rm -it -v $PWD:/workspace -w /workspace pennsive/whitestripe python3 -m build
docker run --rm -it -v $PWD:/workspace -w /workspace pennsive/whitestripe python3 -m twine upload dist/*
