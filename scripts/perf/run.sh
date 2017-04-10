#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

. $DIR/config.sh

MIDDLEBOX=$1
SCENARIO=$2
RESULTS_FILE=$3
PCAP_FILE=$4

if [ -z $MIDDLEBOX ]; then
    echo "[bench] No app specified" 1>&2
    exit 1
fi

if [ -z $SCENARIO ]; then
    echo "[bench] No scenario specified" 1>&2
    exit 2
fi

if [ -z $RESULTS_FILE ]; then
    echo "[bench] No result file specified" 1>&2
    exit 3
fi

if [ -f "$RESULTS_FILE" ]; then
    echo "[run] The result file $RESULTS_FILE exists! exiting" 1>&2
    exit 4
fi

if [ -z $PCAP_FILE ]; then
    echo "[run] No pcap file specified" 1>&2
    exit 5
fi

case $SCENARIO in
    "thru-1p")
        LUA_SCRIPT="pcap-find-1p.lua"
        echo "[bench] Benchmarking throughput..."
        ssh $TESTER_HOST "sudo ~/moon-gen/build/MoonGen ~/scripts/moongen/$LUA_SCRIPT -r 3000 -u 5 -t 20 1 0 $PCAP_FILE"
        scp $TESTER_HOST:pcap-find-1p-results.txt "./$RESULTS_FILE"
        ssh $TESTER_HOST "sudo rm pcap-find-1p-results.txt"
        ;;
    "latency")
        LUA_SCRIPT="pcap-latency-light.lua"
        echo "[bench] Benchmarking throughput..."
        ssh $TESTER_HOST "sudo ~/moon-gen/build/MoonGen ~/scripts/moongen/$LUA_SCRIPT -u 5 -t 20 1 0 $PCAP_FILE"
        scp $TESTER_HOST:mf-lat.txt "./$RESULTS_FILE"
        ssh $TESTER_HOST "sudo rm mf-lat.txt"
        ;;
    *)
        echo "[bench] Unknown scenario: $SCENARIO" 1>&2
        exit 10
        ;;
esac
