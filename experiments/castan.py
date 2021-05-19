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

    d1 = net.addDocker('d1', ip='10.0.0.251', dimage="ubuntu:xenial")
    d2 = net.addDocker('d2', ip='10.0.0.252', dimage="ubuntu:xenial")

    def cmd(c):
        info('Running command %s on all hosts...\n' % c)
        d1.cmd(c)
        d2.cmd(c)

    cmd('apt update -qq')
    cmd('apt upgrade -yqq')
    cmd('apt install -yqq ip')
    cmd('apt install -yqq iputils-ping')
    cmd('apt install -yqq iproute2')
    cmd('apt install -yqq net-tools')

    s1 = net.addSwitch('s1')
    net.addLink(d1, s1, cls=TCLink, delay='1ms', bw=1000)
    net.addLink(d2, s1, cls=TCLink, delay='1ms', bw=1000)
    # net.addLink(c0, s1)
    net.start()
    info('Network started.\n')

    info('Pinging all hosts...\n')
    net.ping([d1, d2])

    info('Starting CLI...\n')
    CLI(net)

    info('Stopping network...\n')
    net.stop()

if __name__ == '__main__':
    main()
