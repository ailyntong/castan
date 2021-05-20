#!/bin/bash

set -e

echo "[init] Setting up tester..."

sudo apt-get -qq update

sudo apt-get install -yqq \
    tcpdump hping3 python-scapy git \
    libpcap-dev libglib2.0-dev \
    daemon iperf3 netperf liblua5.2-dev \
    make binutils gcc \
    bc cmake

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

$DIR/install-dpdk.sh

$DIR/install-moongen.sh
