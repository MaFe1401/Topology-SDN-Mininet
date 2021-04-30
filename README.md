# Topology-SDN-Mininet

Mininet command to load the topology:  
`sudo mn --custom topo.py --topo mytopo --controller=remote,ip=127.0.0.1,port=6633 --switch ovsk,protocols=OpenFlow10 --link tc --mac`  
Run the controller:  
`sudo docker run -it -p 6633:6633 -p 8080:8080 -p 6653:6653 lvillatoroq/odl:hydrogen`
