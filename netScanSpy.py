#!/usr/bin/python
import scapy.all as scapy
import argparse

def scan(ip):
    arpReq = scapy.ARP(pdst=ip)
    broadc = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arpReq_broadc = broadc/arpReq
    answer = scapy.srp(arpReq_broadc, timeout=1, verbose=False)[0]

    print("IP\t\tMAC\n----------- \t-----------")
    for e in answer:
        print(e[1].psrc + "\t" + e[1].hwsrc)

def getArguments():
    par = argparse.ArgumentParser()
    par.add_argument("-t", dest="tar", help="Ip-Target/Ip-Range")
    opt = par.parse_args()
    return opt

opt = getArguments()
scan(opt.tar)
