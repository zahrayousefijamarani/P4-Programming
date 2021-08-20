from mininet.topo import Topo
from mininet.node import OVSSwitch


class CustomTOPO(Topo):

    def __init__(self):
        super(CustomTOPO, self).__init__(self)
        self.build()

        for i in range(1, 4):
            s = OVSSwitch(name='s%d' % i, protocols='OpenFlow13')
            self.addSwitch(name=s.name)

        self.addLink('s1', 's2', bw=20, delay= '10ms')
        self.addLink('s2', 's3', bw=30, delay= '10ms')

        for i in range(1,7):
            self.addHost('h%d' % i)

        self.addLink('s1', 'h1')
        self.addLink('s2', 'h4')
        self.addLink('s3', 'h6')
        self.addLink('s1','h2', bw=20, delay='100ms')
        self.addLink('s1', 'h3', bw=20)
        self.addLink('s2', 'h5',bw=20, loss = 1)