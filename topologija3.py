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
    net = Mininet( controller=RemoteController, link=TCLink, switch=OVSKernelSwitch )

    print "*** Creating nodes"
    s1 = net.addSwitch( 's1', mac='00:00:00:00:00:01')
    s2 = net.addSwitch( 's2', mac='00:00:00:00:00:02')
    s3 = net.addSwitch( 's3', mac='00:00:00:00:00:03')
    s4 = net.addSwitch( 's4', mac='00:00:00:00:00:04')
    s5 = net.addSwitch( 's5', mac='00:00:00:00:00:05')
    s6 = net.addSwitch( 's6', mac='00:00:00:00:00:06')
    s7 = net.addSwitch( 's7', mac='00:00:00:00:00:07')
    s8 = net.addSwitch( 's8', mac='00:00:00:00:00:08')
    s9 = net.addSwitch( 's9', mac='00:00:00:00:00:09')
    s10 = net.addSwitch( 's10', mac='00:00:00:00:00:10')
    s11 = net.addSwitch( 's11', mac='00:00:00:00:00:11')
    s12 = net.addSwitch( 's12', mac='00:00:00:00:00:12')
    s13 = net.addSwitch( 's13', mac='00:00:00:00:00:13')
    s14 = net.addSwitch( 's14', mac='00:00:00:00:00:14')
    s16 = net.addSwitch( 's16', mac='00:00:00:00:00:16')
    s38 = net.addSwitch( 's38', mac='00:00:00:00:00:15')
    s39 = net.addSwitch( 's39', mac='00:00:00:00:00:17')
    h50 = net.addHost( 'h50', mac='00:00:00:00:00:50', ip='192.168.1.2/24' )
    h51 = net.addHost( 'h51', mac='00:00:00:00:00:51', ip='192.168.1.3/24' )
    c52 = net.addController( 'c52', controller=RemoteController, ip='127.0.0.1', port=6633)

    print "*** Creating links"
    net.addLink(s16, h51, 4, 0, bw=1000)
    net.addLink(h50, s9, 0, 4, bw=1000)
    net.addLink(s38, s16, 4, 3, bw=1000)
    net.addLink(s39, s16, 2, 2, bw=1000)
    net.addLink(s38, s13, 3, 3, bw=1000)
    net.addLink(s13, s16, 2, 1, bw=1000)
    net.addLink(s3, s13, 3, 1, bw=100)
    net.addLink(s38, s14, 2, 2, bw=1000)
    net.addLink(s14, s39, 1, 1, bw=1000)
    net.addLink(s12, s38, 3, 1, bw=1000)
    net.addLink(s11, s12, 2, 2, bw=1000)
    net.addLink(s10, s11, 4, 1, bw=1000)
    net.addLink(s10, s12, 3, 1, bw=1000)
    net.addLink(s6, s10, 3, 2, bw=1000)
    net.addLink(s8, s7, 3, 4, bw=1000)
    net.addLink(s9, s7, 3, 3, bw=1000)
    net.addLink(s6, s7, 2, 2, bw=1000)
    net.addLink(s8, s6, 2, 1, bw=1000)
    net.addLink(s9, s8, 2, 1, bw=1000)
    net.addLink(s5, s9, 3, 1, bw=100)
    net.addLink(s10, s4, 1, 6, bw=1000)
    net.addLink(s7, s4, 1, 5, bw=1000)
    net.addLink(s2, s3, 3, 2, bw=1000)
    net.addLink(s4, s3, 4, 1, bw=1000)
    net.addLink(s4, s2, 3, 2, bw=1000)
    net.addLink(s4, s1, 2, 3, bw=1000)
    net.addLink(s5, s4, 2, 1, bw=1000)
    net.addLink(s1, s5, 2, 1, bw=1000)
    net.addLink(s1, s2, 1, 1, bw=1000)

    print "*** Starting network"
    net.build()
    s38.start( [c52] )
    s10.start( [c52] )
    s4.start( [c52] )
    c52.start()

    print "*** Running CLI"
    CLI( net )

    print "*** Stopping network"
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()

