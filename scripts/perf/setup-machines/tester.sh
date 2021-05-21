#!/bin/bash

set -e

echo "[init] Setting up tester..."

apt-get -qq update

# Update the kernel to the expected version, then relink headers.
apt-get install -yqq --reinstall linux-image-`uname -r`
apt-get install -yqq linux-headers-`uname -r`

# Dependencies
apt-get install -yqq \
    tcpdump hping3 python-scapy git \
    libpcap-dev libglib2.0-dev \
    daemon iperf3 netperf liblua5.2-dev \
    make binutils gcc \
    bc cmake \
    libnuma-dev kmod pciutils

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

$DIR/install-dpdk.sh

$DIR/install-moongen.sh
