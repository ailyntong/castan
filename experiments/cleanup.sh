#!/bin/bash
docker stop mn.d1
docker stop mn.d2
docker rm mn.d1
docker rm mn.d2

ip link delete s1-eth1
ip link delete s1-eth2
ip link delete s1-eth3
echo "MORE LINKS MUST BE DELETED MANUALLY! Run ip link to list them. They are prefixed with veth."
