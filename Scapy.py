from scapy.all import IP, ICMP, sr1, ls

ip_layer = IP(src = "192.168.0.36", dst ="www.google.com")

icmp_req = ICMP()

packet = ip_layer/icmp_req

# recieved_packet = sr1(packet)

# if recieved_packet:
#     print(recieved_packet.src)
#     print(recieved_packet.dst)
#print(ip_layer.show) to show the layers fieldd .summary for a summary of the layer
print(ls(ip_layer))