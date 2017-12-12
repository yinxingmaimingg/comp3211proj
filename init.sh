#!/bin/bash  

# define variables
loopMax=5000
testCaseNo=2


# const
testDir="testFolder/"
correctProgram="testCase"$testCaseNo
bugProgram="testCaseWithBug"$testCaseNo
generateInputPy="generateInput.py"
resultDir="../gcovResult/"
cpp=".cpp"
cppGcov=".cpp.gcov"
tempTrash="tempTrash.txt"

# commands
cd $testDir
g++ $correctProgram$cpp -o $correctProgram
g++ -fprofile-arcs -ftest-coverage -fPIC -O0 $bugProgram$cpp -o $bugProgram
echo "" > $resultDir"bugCases.txt"

for ((i=0; i<$loopMax; i++))
do
	echo "Case: "$i 
    python $generateInputPy $testCaseNo > "input.txt"
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

#<<rmUseless
rm $tempTrash
rm "input.txt"
rm "output.txt"
rm "outputBug.txt"
rm *.gcda
rm *.gcno
#rmUseless


cd ..
python CoverageInfor.py $loopMax > coverage.txt
echo ""
echo "Coverage Information (coverage.txt): "
cat coverage.txt