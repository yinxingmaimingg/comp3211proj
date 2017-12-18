#!/bin/bash  

# define variables
loopMax=500
testCaseNo=$1


# const
testDir="testFolder/"
correctProgram="testCase"$testCaseNo
generateInputPy="generateInput.py"
resultDir="gcovResult/"
cpp=".cpp"
cppGcov=".cpp.gcov"
tempTrash="tempTrash.txt"


# commands

for ((j=0; j<10; j++))
do 
	cd $testDir
	g++ $correctProgram$cpp -o $correctProgram
	bugProgram="testCase"$testCaseNo"WithBug"$j
	echo ""
	echo "Test bug program "$j
	echo ""

	echo "" > $resultDir"bugCases.txt"
	for ((i=0; i<$loopMax; i++))
	do
		echo "Case: "$i 
	    python3 $generateInputPy $testCaseNo > "input.txt"
		g++ -fprofile-arcs -ftest-coverage -fPIC -O0 $bugProgram$cpp -o $bugProgram
		"./"$correctProgram < "input.txt" > "output.txt"
		"./"$bugProgram < "input.txt" > "outputBug.txt"
		cmp -s "output.txt" "outputBug.txt"
		if [ $? -ne 0 ]
		then
			echo $i >> $resultDir"bugCases.txt"
		fi
		gcov $bugProgram -r > $tempTrash
		mv $bugProgram$cppGcov $resultDir"example"$i".gcov"
	done

	cd ..
	python CoverageInfor.py $loopMax > "test_coverage/coverage_"$testCaseNo"_"$j".txt"
done

#<<rmUseless
cd $testDir
rm $tempTrash
rm "input.txt"
rm "output.txt"
rm "outputBug.txt"
rm *.gcda
rm *.gcno
cd  $resultDir
rm *.gcov
rm "bugCases.txt"
cd ../..
#rmUseless

