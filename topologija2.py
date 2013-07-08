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
    s1 = net.addSwitch( 's1', mac='00:00:00:00:00:10')
    s2 = net.addSwitch( 's2', mac='00:00:00:00:00:11')
    c0 = net.addController( 'c0', controller=RemoteController, defaultIP="127.0.0.1", port=6633)

    print "*** Creating links"
    net.addLink(s1, s2, 3, 5, bw=100)
    net.addLink(s2, h3, 2, 0, bw=100)
    net.addLink(s2, h2, 1, 0, bw=100)
    net.addLink(s1, h2, 2, 0, bw=100)
    net.addLink(s1, h1, 1, 0, bw=100)

    print "*** Starting network"
    net.build()
    s2.start( [c0] )
    s1.start( [c0] )
    c0.start()

    print "*** Running CLI"
    CLI( net )

    print "*** Stopping network"
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()
