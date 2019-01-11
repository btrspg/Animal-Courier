#!/bin/sh

touch test.txt
touch test2.txt
touch test3.txt
for i in `seq 1 200000`;do echo $i;done