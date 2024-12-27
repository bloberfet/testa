#!/bin/bash

mkdir a && cd a
nmap -sn 10.13.38.0/24 --min-rate=5000 -oN nmap_host-discovery
mkdir b && cd b

for ip in $(cat ../nmap_host-discovery|grep 'scan report'|awk '{print $5}');do nmap -Pn -p- $ip --min-rate=5000 -oN nmap_65k-ports_$ip;done
mkdir c && cd c

for ip in $(cat ../../nmap_host-discovery|grep 'scan report'|awk '{print $5}');do for ports in $(cat ../nmap_65k-ports_$ip|grep open|awk -F '/' '{print $1}'|sed -z 's/\n/,/g'|sed 's/,$//');do nmap -Pn $ip -p $ports -sCV -oN nmap_sCV_$ip;done;done
