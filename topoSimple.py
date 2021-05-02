from mininet.topo import Topo
class MyTopo(Topo):
	def __init__(self):
		#initialise topology
		Topo.__init__(self)
		#add hosts
		h1=self.addHost('h1', ip='169.10.0.2')
		h2=self.addHost('h2', ip='169.10.0.3')
		#add switchs
		s1=self.addSwitch('s1')
		#add links
		self.addLink(h1, s1)
		self.addLink(s1, h2)
		
topos={'mytopo':(lambda:MyTopo())}
