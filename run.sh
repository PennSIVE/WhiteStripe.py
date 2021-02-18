#!/bin/bash

# docker build -t pennsive/whitestripe .

docker run --rm -it -v $PWD:/workspace -w /workspace pennsive/whitestripe python3 -m build
docker run --rm -it -v $PWD:/workspace -w /workspace pennsive/whitestripe python3 -m twine upload --repository testpypi dist/*
