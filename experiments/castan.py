#!/usr/local/lib/python3.8
from mininet.net import Containernet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel
setLogLevel('info')

def main():
    info('Starting network...\n')
    net = Containernet(controller=Controller)
    c0 = net.addController('c0')

    # d1 = net.addDocker('d1', ip='10.0.0.251', dimage="ubuntu:xenial")
    # d2 = net.addDocker('d2', ip='10.0.0.252', dimage="ubuntu:xenial")
    d1 = net.addDocker('d1', ip='10.0.0.251', dimage="middlebox:latest")
    d2 = net.addDocker('d2', ip='10.0.0.252', dimage="tester:latest")

    def cmd(c):
        info('Running command %s on all hosts...\n' % c)
        d1.cmd(c)
        d2.cmd(c)

    # cmd('apt update -qq')
    # cmd('apt upgrade -yqq')
    # cmd('apt install -yqq ip')
    # cmd('apt install -yqq iputils-ping')
    # cmd('apt install -yqq iproute2')
    # cmd('apt install -yqq net-tools')
    # cmd('apt install -yqq telnet telnetd iperf')

    # info('Setting up middlebox...\n')
    # d1.cmd('/bin/bash ~/castan/scripts/perf/init-middlebox.sh')

# TODO: moongen script broken because of kernel version number issue again,
# trying to figure where exactly is causing it
    # info('Setting up tester...\n')
    # d2.cmd('/bin/bash /home/castan/scripts/init-tester.sh')

    info('Adding links...\n')
    s1 = net.addSwitch('s1')
    net.addLink(d1, s1, cls=TCLink, delay='1ms', bw=1000)
    net.addLink(d2, s1, cls=TCLink, delay='1ms', bw=1000)
    net.start()
    info('Network started.\n')

    info('Pinging all hosts...\n')
    net.ping([d1, d2])

    info('Running the experiment...\n')
    d1.cmd('/bin/bash ~/castan/scripts/perf/start-middlebox.sh dpdk-nat-basichash')

    info('Starting CLI...\n')
    CLI(net)

    info('Stopping network...\n')
    net.stop()

if __name__ == '__main__':
    main()
