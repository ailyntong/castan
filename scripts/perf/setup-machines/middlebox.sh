#!/bin/bash

set -e

echo "[init] Setting up middlebox..."

apt-get -qq update

apt-get install -yqq \
    tcpdump git libpcap-dev \
    linux-headers-4.4.0-210-generic \
    libglib2.0-dev daemon iperf3 netperf tmux

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

$DIR/install-dpdk.sh
