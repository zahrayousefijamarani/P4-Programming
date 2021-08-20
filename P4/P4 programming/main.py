from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch

from TOPO import CustomTOPO

myTopo = CustomTOPO()
rm = RemoteController('c0', ip = '192.168.1.6', port=6653)
net = Mininet(topo=myTopo, controller= rm, link=TCLink,build= True, cleanup=True, autoStaticArp=True, switch=OVSSwitch)
setLogLevel('info')
net.start()
CLI(net)
net.stop()