#!/usr/bin/python

"""
Script created by VND - Visual Network Description
"""
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink

def topology():
    "Create a network."
    net = Mininet( controller=Controller, link=TCLink, switch=OVSKernelSwitch )

    print "*** Creating nodes"
    h1 = net.addHost( 'h1', mac='00:00:00:00:00:01', ip='10.0.0.1/8' )
    h2 = net.addHost( 'h2', mac='00:00:00:00:00:02', ip='10.0.0.2/8' )
    h3 = net.addHost( 'h3', mac='00:00:00:00:00:03', ip='10.0.0.3/8' )
    s4 = net.addSwitch( 's4', mac='00:00:00:00:00:10')
    s5 = net.addSwitch( 's5', mac='00:00:00:00:00:11')
    c6 = net.addController( 'c6', controller=RemoteController, defaultIP="127.0.0.1", port=6633)

    print "*** Creating links"
    net.addLink(s4, s5, 3, 5, bw=100)
    net.addLink(s5, h3, 2, 0, bw=100)
    net.addLink(s5, h2, 1, 0, bw=100)
    net.addLink(s4, h2, 2, 0, bw=100)
    net.addLink(s4, h1, 1, 0, bw=100)

    print "*** Starting network"
    net.build()
    s5.start( [c6] )
    s4.start( [c6] )
    c6.start()

    print "*** Running CLI"
    CLI( net )

    print "*** Stopping network"
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()
