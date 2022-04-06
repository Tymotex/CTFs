#!/usr/bin/bash

# cat <(sleep 3) <(echo g 1) | nc -q 1 13.210.180.94 10003 &
# secret=$(echo s | ./vuln | egrep ": [0-9]+" | egrep -o "[0-9]+")
# echo Secret should be: $secret
# cat <(sleep 3) <(echo s) | nc -q 1 13.210.180.94 10003 &

while sleep 0.5; do 
    secret=$(echo s | ./vuln | egrep ": [0-9]+" | egrep -o "[0-9]+")
    echo $secret >> secrets
done