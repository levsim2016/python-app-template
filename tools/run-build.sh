#!/bin/bash

cd $(dirname $(realpath $0))/..
cd bin
chmod +x ./app.pex

./app.pex