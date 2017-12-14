
testCaseNo=$1

testDir="testFolder/"


cd $testDir
for ((i=0; i<10; i++))
do
	python insertBug.py $1 $i
done
cd ..