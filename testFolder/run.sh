#!/bin/bash  

# define variables
bug_program="testCase1-bug"

cpp=".cpp"
cpp_gcov=".cpp.gcov"


# commands
g++ input.cpp -o input
g++ testCase1.cpp -o testCase1
g++ -fprofile-arcs -ftest-coverage -fPIC -O0 ${bug_program}${cpp} -o $bug_program

for ((i=0; i<5000; i++))
do
	echo "Case: "$i 
    ./input > input.txt
	./testCase1 < input.txt > output.txt
	./$bug_program < input.txt > output-bug.txt
	cmp -s output.txt output-bug.txt
	if [ $? -ne 0 ]
	then
		echo $i >> ../gcovResult/bug_cases.txt
	fi
	gcov $bug_program -r
	mv $bug_program$cpp_gcov ../gcovResult/example$i.gcov
	

done