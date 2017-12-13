#!/usr/env/bash

grep logfile | sort | uniq -c | sort -k1,1nr -k2,2| awk '{print $2,$1}'




ifconfig eth0:svc 10.0.2.100/32 netmask 255.255.255.0


arping -q -U -c 3 -I eth0 10.0.2.100/32






sudo groupadd -g 2005 RestrictedUsers 
sudo groupadd -g 2006 ExternalUsers
sudo groupadd -g 2007 InternalUsers

sudo useradd internal_users -g InternalUsers -s /bin/sh
sudo useradd restricted_user -G RestrictedUsers,ExternalUsers -s /binfalse


