#!/bin/bash

# Αρχικοποίηση του αρχείου εξόδου
> katharo.txt

# Διάβασμα του αρχείου εισόδου και διαγραφή γραμμών με συνεχόμενους αριθμούς 1-10
while read line
do
    # Χρησιμοποιούμε την grep για να ελέγξουμε αν υπάρχουν οι συνεχόμενοι αριθμοί στη γραμμή
    echo "$line" | grep -E -q '1 2|2 3|3 4|4 5|5 6|6 7|7 8|8 9|9 10'

    # Εάν η grep δεν βρει τίποτα, τότε η γραμμή δεν έχει συνεχόμενους αριθμούς 1-10 και είναι ασφαλές να προστεθεί στο αρχείο εξόδου
    if [ $? -ne 0 ]
    then
        echo "$line" >> katharo.txt
    fi
done < teliko.txt
