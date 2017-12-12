import random
import sys

# case no. variable

def generateTestCase2():
	result = random.randint(0, 200)
	if (result>170):
		result = random.randint(365, 700)
		if (result>500):
			result = random.randint(0, 60000)
	print(result)
	print(-1)



if __name__=="__main__":
	testCaseNo = (int)(sys.argv[1])
	if (testCaseNo==2):
		generateTestCase2()