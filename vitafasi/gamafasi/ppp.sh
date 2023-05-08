#!/bin/bash

# Εκχώρηση ονομάτων αρχείων σε μεταβλητές
second_file="presults1.txt"
output_file="ppppresults.txt"
cp "$second_file" "$output_file"
wait



input2="k1-2.txt"
while IFS= read -r line
do
  wait
  echo "$line"
  wait
  sed -i "/$line/d" "$output_file"
  wait
done < "$input2"

wait

input3="k1-3.txt"
while IFS= read -r line
do
  wait
  echo "$line"
  wait
  sed -i "/$line/d" "$output_file"
  wait
done < "$input3"

wait

input4="k1-4.txt"
while IFS= read -r line
do
  wait
  echo "$line"
  wait
  sed -i "/$line/d" "$output_file"
  wait
done < "$input4"

wait

input5="k1-5.txt"
while IFS= read -r line
do
  wait
  echo "$line"
  wait
  sed -i "/$line/d" "$output_file"
  wait
done < "$input5"

wait

inputa="k2-3.txt"
while IFS= read -r line
do
  wait
  echo "$line"
  wait
  sed -i "/$line/d" "$output_file"
  wait
done < "$inputa"

wait

inputb="k2-4.txt"
while IFS= read -r line
do
  wait
  echo "$line"
  wait
  sed -i "/$line/d" "$output_file"
  wait
done < "$inputb"

wait

inputc="k2-5.txt"
while IFS= read -r line
do
  wait
  echo "$line"
  wait
  sed -i "/$line/d" "$output_file"
  wait
done < "$inputc"

wait

inputtt="k3-4.txt"
while IFS= read -r line
do
  wait
  echo "$line"
  wait
  sed -i "/$line/d" "$output_file"
  wait
done < "$inputtt"

wait

inputttt="k3-5.txt"
while IFS= read -r line
do
  wait
  echo "$line"
  wait
  sed -i "/$line/d" "$output_file"
  wait
done < "$inputttt"

wait

inputt5="k4-5.txt"
while IFS= read -r line
do
  wait
  echo "$line"
  wait
  sed -i "/$line/d" "$output_file"
  wait
done < "$inputt5"

wait
sleep 3 
echo "PROBABLY OK....DONE"





































































