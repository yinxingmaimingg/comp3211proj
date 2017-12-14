import random
import sys

# case no. variable

def generateInput1():
	for i in range(9):
		result = random.randint(0, 1)
		if (result==1):
			result = random.randint(-1, 5)
			if (result>1):
				result = random.randint(-100, 100)
		print(result, end=" ")
	print()


def generateInput2():
	result = random.randint(0, 200)
	if (result>170):
		result = random.randint(365, 700)
		if (result>500):
			result = random.randint(0, 60000)
	print(result)
	print(-1)



if __name__=="__main__":
	testCaseNo = (int)(sys.argv[1])
	if (testCaseNo==1):
		generateInput1()
	if (testCaseNo==2):
		generateInput2()