#!/bin/bash
rcres unlease rc61-70
for i in {61..70}
do
  read line
  rcres lease 1d rc$i -m "$line"
done < /home/jdellit/scripts/rcresbanner$(($RANDOM % 8)).txt
