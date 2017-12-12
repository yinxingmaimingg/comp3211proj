#!/usr/bin/env python
import pprint

fileDir = "gcovResult/"
testCaseNum = 5000;

class CoverageInfor:

	def __init__(self):
		# each element is a dictionary, in the format of {"fileName":string, "lno": int} 
		self.inforList = [] 

	def make2dList(self, rows, cols):
	    a=[]
	    for row in range(rows): 
	    	a += [[0]*cols]
	    return a

	def file_len(self, fname):
	    with open(fname) as f:
	        for i, l in enumerate(f):
	            pass
	    return i + 1

	def readGcov(self):
		info = self.make2dList(self.file_len(fileDir + "example0.gcov"), 4)
		infoDict = {}
		result = [];

		# TODO: judge test case result;
		for i in range(testCaseNum):
			result.append('t')
		file = open(fileDir+"bug_cases.txt")
		for line in file:
			result[(int)(line)] = 'f'

		# [t+e; t+ue; f+e; f+ue]
		for j in range(testCaseNum):
			filePathI = "example"
			filePathII = ".gcov"
			filePath = fileDir + filePathI + str(j) + filePathII

			file = open(filePath, "r")		
			if result[j] == "t"	: 
				i = 0
				for line in file:
					tempList = line.split(':', 2 )
					# remove leading space
					tempChar = tempList[0].lstrip(' ')
					if tempChar == "#####": 
						info[i][1] = info[i][1] + 1
						infoDict.update({i-4: info[i]})
					elif tempChar == "-": #ignore
						info[i][0] = info[i][0]
						info[i][1] = info[i][1]
					else:
						info[i][0] = info[i][0] + 1
						infoDict.update({i-4: info[i]})
					#print info[i]
					i  = i+1
			else:
				i = 0
				for line in file:
					tempList = line.split(':', 2 )
					# remove leading space
					tempChar = tempList[0].lstrip(' ')
					if tempChar == "#####": 
						info[i][3] = info[i][3] + 1
						infoDict.update({i-4: info[i]})
					elif tempChar == "-": #ignore
						info[i][2] = info[i][2]
						info[i][3] = info[i][3]
					else:
						info[i][2] = info[i][2] + 1
						infoDict.update({i-4: info[i]})
					#print info[i]
					i  = i+1

		#print info[5:]
		pprint.pprint(infoDict) 
 		#print file.read()
		

temp = CoverageInfor()
temp.readGcov()
