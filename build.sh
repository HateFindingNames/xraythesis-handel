#!/bin/bash
set -x
rm -r ./scons-out
rm -r ./myapp/lib
# Build for udxp with usb2 for x64
TMP=/tmp sh swtoolkit/hammer.sh --no-epp --no-serial --no-usb --usb2 --no-plx --no-saturn --udxp --no-udxps --no-xmap --no-stj --no-mercury --no-alpha --no-vba --no-xw --x64 --no-tests --no-samples --no-vld --verbose 2>&1 | tee ./build.log
mkdir ./myapp/lib/
cp ./scons-out/rel-x64/lib/* ./myapp/lib/
python libdocer.py