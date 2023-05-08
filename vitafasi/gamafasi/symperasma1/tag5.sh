#!/bin/bash

while read line; do
    if ! grep -E "(3[0-9] [3-9][1-9] [4-5][0-9]|3[1-9] [4-5][0-9] [4-5][1-9])" <<< "$line" > /dev/null; then
        echo "$line" >> pentakatharo.txt
    fi
done < katharo.txt

