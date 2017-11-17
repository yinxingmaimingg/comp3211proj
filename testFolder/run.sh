#!/bin/bash  

gcc input.c -o input
g++ testCase1.cpp -o testCase1
g++ -fprofile-arcs -ftest-coverage -fPIC -O0 testCase1B.cpp -o testCase1B


for ((i=0; i<50; i++))
do
    ./input > input.txt
	./testCase1 <input.txt >>output.txt
	./testCase1B <input.txt >>outputB.txt
	gcov testCase1B -r
	mv testCase1B.cpp.gcov ../example$i.gcov
	sleep 3
done