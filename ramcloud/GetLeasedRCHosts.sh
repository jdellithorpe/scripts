#!/bin/bash
# A simple script to parse out the hosts this user has leased from rcres

i=0
for host in `rcres ls -l | grep "$(whoami)" | cut -c13-16 | grep "rc[0-9]" | cut -c3-4`;
do
  hosts[i]=rc$host
  (( i++ ))
done

echo ${hosts[*]}
