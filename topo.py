from mininet.topo import Topo

class MyTopo(Topo):
	def __init__(self):
		#system.call initialise topology
		Topo.__init__(self)
		#add hosts
		h1a=self.addHost('h1a')
		h2p=self.addHost('h2p')
		h3a=self.addHost('h3a')
		h4p=self.addHost('h4p')
		#add links
		s1=self.addSwitch('s1')
		s2=self.addSwitch('s2')
		s3=self.addSwitch('s3')
		#add links
		self.addLink(h4p,s3)
		self.addLink(h3a,s3)
		self.addLink(s3,s1)
		self.addLink(s1,s2)
		self.addLink(s2,h2p)
		self.addLink(s2,h1a)

topos={'mytopo':(lambda:MyTopo())}
