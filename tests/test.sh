#!/bin/sh

perl -e 'for(my $i=0;$i<2;$i++){for(my $j=0;$j<100000;$j++){$sh{"$i,$j"}=$i+$j;}sleep(1);'
perl -e 'for(my $i=0;$i<2;$i++){for(my $j=0;$j<100000;$j++){$sh{"$i,$j"}=$i+$j;}sleep(1);'
perl -e 'for(my $i=0;$i<2;$i++){for(my $j=0;$j<100000;$j++){$sh{"$i,$j"}=$i+$j;}sleep(1);'
perl -e 'for(my $i=0;$i<2;$i++){for(my $j=0;$j<100000;$j++){$sh{"$i,$j"}=$i+$j;}sleep(1);'