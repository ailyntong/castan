#!/bin/bash

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

. $DIR/config.sh

$DIR/setup-machines/tester.sh
#$DIR/clean/tester.sh
#$DIR/init-machines/tester.sh
