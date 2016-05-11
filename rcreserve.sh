#!/bin/bash
rcres unlease rc01-10 
for i in {01..10}
do
  read line
  rcres lease 1d rc$i -m "$line"
done < /home/jdellit/scripts/rcresbanner$(($RANDOM % 8)).txt
