#!/bin/bash


echo ""
echo "do not run this script just read it"
echo ""
sleep 11 
exit 0
sed -i "s/^.//g" tetrada*.txt 
wait 
sed -i 's/.$//' tetrada*.txt 
wait
sed  -i 's/,//g' tetrada*.txt
wait
grep -v -f tetrada.txt filtered_combinations_processed.txt | sed '/^$/d' > temp.txt
wait
grep -v -f tetrada2.txt temp.txt | sed '/^$/d' > temp2.txt
wait
grep -v -f tetrada3.txt temp2.txt | sed '/^$/d' > temp3.txt
grep -v -f tetrada4.txt temp3.txt | sed '/^$/d' > temp4.txt
grep -v -f tetrada5.txt temp4.txt | sed '/^$/d' > temp5.txt
grep -v -f tetrada6.txt temp5.txt | sed '/^$/d' > temp6.txt
grep -v -f tetrada7.txt temp6.txt | sed '/^$/d' > temp7.txt
grep -v -f tetrada8.txt temp7.txt | sed '/^$/d' > temp8.txt
grep -v -f tetrada9.txt temp8.txt | sed '/^$/d' > temp9.txt
# run next scripts {13-17}.py and came back
# exoyme eksereseis apo : digonio kai kathera*.txt --> temp9.txt
18.py
