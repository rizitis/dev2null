#!/bin/bash

# Εκχώρηση ονομάτων αρχείων σε μεταβλητές
second_file="result5.txt"
output_file="result6.txt"
input="katheta5.txt"

cp "$second_file" "$output_file"
wait

while IFS= read -r line
do
  echo "$line"
  wait
  sed -i "/$line/d" "$output_file"
  wait
done < "$input"
