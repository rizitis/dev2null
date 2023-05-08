#!/bin/bash

sed  -i 's/Triplets://g' p*.txt
wait
sed  -i 's/Quads://g' p*.txt
wait
sed  -i 's/Quints://g' p*.txt
wait
sed -i "s/^.//g" p*.txt 
wait 
sed -i 's/.$//' p*.txt 
wait
sed  -i 's/,//g' p*.txt
wait

# Εκχώρηση ονομάτων αρχείων σε μεταβλητές
second_file="result6.txt"
output_file="presults1.txt"
input="p1.txt"

cp "$second_file" "$output_file"
wait

while IFS= read -r line
do
  echo "$line"
  wait
  sed -i "/$line/d" "$output_file"
  wait
done < "$input"
