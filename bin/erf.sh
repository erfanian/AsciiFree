#!/bin/sh
# executes the given script in Eric's python environment

PYTHONCMD='/usr/bin/env python3.0'

echo $#

if [ $# -lt 1 ]; then
	echo "USAGE: $0 TARGET"
	exit -1
else
        # assert: good to go
        echo "$PYTHONCMD $1"
        $PYTHONCMD $1
fi
