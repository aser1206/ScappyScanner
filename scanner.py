from scapy.all import Ether, ARP, srp, conf
import sys
import time
#scann the network
def arp_scan(iface,ip_range):
    print("[+] Scanning ", ip_range)
    current_time=time.time()
    print("[+] Scan started at: ",time.ctime(current_time))
    conf.verb = 0 #hide all the information and run in the background
    broadcast ="ff:ff:ff:ff:ff:ff"
    ether_layer = Ether(dst=broadcast)
    arp_layer=ARP(pdst = ip_range)
    packet = ether_layer/arp_layer

    ans, unasw = srp(packet, iface=iface, timeout=2,inter=0.1)
    for snd,rcv in ans:
        ip = rcv[ARP].psrc
        mac = rcv[Ether].src
    duration = time.time() - current_time
    print("[+] Scan finished. Duration: ", duration)

#scan an IP range 
#scanner.py eth0 192.168.0.1/24 (/24 = subnet masking)
if __name__=="__main__":
    iface =sys.argv[1]
    ip_range = sys.argv[2]
    arp_scan(iface,ip_range)

