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
    controller = net.addController('c0')
    middlebox = net.addDocker('d1', ip='10.0.0.251', dimage="middlebox:latest")
    tester = net.addDocker('d2', ip='10.0.0.252', dimage="tester:latest")

    def cmd(c):
        info('Running command %s on all hosts...\n' % c)
        middlebox.cmd(c)
        tester.cmd(c)

    info('Adding links...\n')
    switch = net.addSwitch('s1')
    net.addLink(middlebox, switch, cls=TCLink, delay='1ms', bw=1000)
    net.addLink(tester, switch, cls=TCLink, delay='1ms', bw=1000)
    net.start()
    info('Network started.\n')

    # info('Pinging all hosts...\n')
    # net.ping([middlebox, tester])

    info('Running the experiment...\n')
    nf = 'dpdk-nat-basichash'
    scenario = 'latency'    # either 'thru-1p' or 'latency'
    pcap_file = '1packet.pcap'
    result_file = 'bench-%s-%s-%s.results' % (nf, scenario, pcap_file)

    middlebox.cmd('mkdir /mnt/huge')
    middlebox.cmd('mount -t hugetlbfs nodev /mnt/huge')
    middlebox.cmd('/bin/bash ~/castan/scripts/perf/start-middlebox.sh %s' % nf)
    # middlebox.cmd('/bin/bash ~/castan/scripts/perf/run.sh %s %s %s %s' % (nf, scenario, result_file, pcap_file))

    info('Starting CLI...\n')
    CLI(net)

    info('Stopping network...\n')
    net.stop()

if __name__ == '__main__':
    main()
