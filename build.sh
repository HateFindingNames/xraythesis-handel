#!/bin/bash
set -x
#TMP=/tmp sh swtoolkit/hammer.sh --verbose --samples --udxp --no-udxps --no-xw --no-serial --no-xmap --no-stj
#TMP=/tmp sh swtoolkit/hammer.sh --verbose --udxp --x64 2>&1 | tee ./build.log
rm -r ./scons-out
TMP=/tmp sh swtoolkit/hammer.sh --udxp --no-udxps --no-xw --no-serial --no-xmap --no-stj --no-mercury --no-saturn --x64 --verbose 2>&1 | tee ./build.log