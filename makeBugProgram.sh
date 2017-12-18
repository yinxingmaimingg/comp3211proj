
testCaseNo=$1

testDir="testFolder/"


cd $testDir
for ((i=0; i<10; i++))
do
	python insertBug.py $1 $i
	echo "Generate bug program \"testCase"$1"WithBug"$i".cpp\" complete."

done
cd ..