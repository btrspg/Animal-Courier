#!/bin/sh

perl -e 'for(my $i=0;$i<2;$i++){for(my $j=0;$j<10000;$j++){$sh{"$i,$j"}=$i+$j;}sleep(2);}'
perl -e 'for(my $i=0;$i<2;$i++){for(my $j=0;$j<20000;$j++){$sh{"$i,$j"}=$i+$j;}sleep(2);}'
perl -e 'for(my $i=0;$i<2;$i++){for(my $j=0;$j<30000;$j++){$sh{"$i,$j"}=$i+$j;}sleep(2);}'
perl -e 'for(my $i=0;$i<2;$i++){for(my $j=0;$j<40000;$j++){$sh{"$i,$j"}=$i+$j;}sleep(2);}'
perl -e 'for(my $i=0;$i<2;$i++){for(my $j=0;$j<50000;$j++){$sh{"$i,$j"}=$i+$j;}sleep(2);}'
perl -e 'for(my $i=0;$i<2;$i++){for(my $j=0;$j<60000;$j++){$sh{"$i,$j"}=$i+$j;}sleep(2);}'
perl -e 'for(my $i=0;$i<2;$i++){for(my $j=0;$j<70000;$j++){$sh{"$i,$j"}=$i+$j;}sleep(2);}'
perl -e 'for(my $i=0;$i<2;$i++){for(my $j=0;$j<80000;$j++){$sh{"$i,$j"}=$i+$j;}sleep(2);}'
perl -e 'for(my $i=0;$i<2;$i++){for(my $j=0;$j<90000;$j++){$sh{"$i,$j"}=$i+$j;}sleep(2);}'
perl -e 'for(my $i=0;$i<2;$i++){for(my $j=0;$j<100000;$j++){$sh{"$i,$j"}=$i+$j;}sleep(2);}'
