#!/bin/bash

mkdir step1_host-discovery && cd step1_host-discovery
nmap -sn 10.13.38.0/24 --min-rate=5000 -oN nmap_host-discovery

mkdir step2_65k-find-open-ports && cd step2_65k-find-open-ports
for ip in $(cat ../nmap_host-discovery|grep 'scan report'|awk '{print $5}');do nmap -Pn -p- $ip --min-rate=5000 -oN nmap_65k-ports_$ip;done

mkdir step3_sCV && cd step3_sCV
for ip in $(cat ../../nmap_host-discovery|grep 'scan report'|awk '{print $5}');do for ports in $(cat ../nmap_65k-ports_$ip|grep open|awk -F '/' '{print $1}'|sed -z 's/\n/,/g'|sed 's/,$//');do nmap -Pn $ip -p $ports -sCV -oN nmap_sCV_$ip;done;done
