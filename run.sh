#!/bin/bash
export IFS=","
cat keywords.csv | while read line
do
        echo $line | cut -d',' -f4     # get the first name
#        echo $line | cut -d'"' -f18    # get the telephone number
done
