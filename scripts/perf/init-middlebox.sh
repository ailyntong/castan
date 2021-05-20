#!/bin/bash

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

. $DIR/config.sh

$DIR/setup-machines/middlebox.sh
# $DIR/clean/middlebox.sh
# $DIR/init-machines/middlebox.sh
