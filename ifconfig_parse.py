class NetWorkInterface:
    def __innit__(self,interface_name,mac_addr,status):
        self.interface_name=interface_name
        self.mac_addr=mac_addr
        self.status=status


data='''lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>
	inet 127.0.0.1 netmask 0xff000000 
	inet6 ::1 prefixlen 128 
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 
	nd6 options=201<PERFORMNUD,DAD>
gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
stf0: flags=0<> mtu 1280
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=400<CHANNEL_IO>
	ether c8:69:cd:b6:56:f2 
	inet6 fe80::e8:f88:a5bd:2d5d%en0 prefixlen 64 secured scopeid 0x4 
	inet 192.168.1.12 netmask 0xffffff00 broadcast 192.168.1.255
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
en1: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
	options=460<TSO4,TSO6,CHANNEL_IO>
	ether 82:18:15:cd:3b:00 
	media: autoselect <full-duplex>
	status: inactive
bridge0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=63<RXCSUM,TXCSUM,TSO4,TSO6>
	ether 82:18:15:cd:3b:00 
	Configuration:
		id 0:0:0:0:0:0 priority 0 hellotime 0 fwddelay 0
		maxage 0 holdcnt 0 proto stp maxaddr 100 timeout 1200
		root id 0:0:0:0:0:0 priority 0 ifcost 0 port 0
		ipfilter disabled flags 0x2
	member: en1 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 5 priority 0 path cost 0
	nd6 options=201<PERFORMNUD,DAD>
	media: <unknown type>
	status: inactive
p2p0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> mtu 2304
	options=400<CHANNEL_IO>
	ether 0a:69:cd:b6:56:f2 
	media: autoselect
	status: inactive
awdl0: flags=8943<UP,BROADCAST,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1484
	options=400<CHANNEL_IO>
	ether a6:fd:8f:0f:9f:9d 
	inet6 fe80::a4fd:8fff:fe0f:9f9d%awdl0 prefixlen 64 scopeid 0x8 
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
llw0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=400<CHANNEL_IO>
	ether a6:fd:8f:0f:9f:9d 
	inet6 fe80::a4fd:8fff:fe0f:9f9d%llw0 prefixlen 64 scopeid 0x9 
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
utun0: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1380
	inet6 fe80::7766:43fa:531d:eec3%utun0 prefixlen 64 scopeid 0xa 
	nd6 options=201<PERFORMNUD,DAD>
utun1: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 2000
	inet6 fe80::ae0c:f95c:c9c2:5b29%utun1 prefixlen 64 scopeid 0xb 
	nd6 options=201<PERFORMNUD,DAD>'''


def parseString(data):
    ipdata=data.splitlines(keepends=False)
    op=[]
    dict={}
    iface_name=""
    for line in ipdata:
        if line[0]!='\t':
            #print(line)
            #e=ipdata[i].find(":")
            #print(ipdata[i][0:e])
            iface_name=line.split(":")[0]
            if iface_name not in dict:
                dict[iface_name]=[]
        else:
            dict[iface_name].append(line)

    for key in dict:
        print(dict[key])










parseString(data)