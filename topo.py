from mininet.topo import Topo

class MyTopo(Topo):
	def __init__(self):
		#initialise topology
		Topo.__init__(self)
		#add hosts
		linkOptsCore = dict(bw=200, delay='100ms')
		linkOptsAccess=dict(bw=1000, delay='10ms')
		h1a=self.addHost('h1a', ip='169.0.10.2')
		h2p=self.addHost('h2p', ip='169.0.10.3')
		h3a=self.addHost('h3a', ip='169.0.10.4')
		h4p=self.addHost('h4p', ip='169.0.10.5')
		#add switchs
		s1=self.addSwitch('s1')
		s2=self.addSwitch('s2')
		s3=self.addSwitch('s3')
		#add links
		self.addLink(h4p,s3, **linkOptsAccess)
		self.addLink(h3a,s3, **linkOptsAccess)
		self.addLink(s3,s1, **linkOptsCore)
		self.addLink(s1,s2, **linkOptsCore)
		self.addLink(s2,h2p, **linkOptsAccess)
		self.addLink(s2,h1a, **linkOptsAccess)

topos={'mytopo':(lambda:MyTopo())}
