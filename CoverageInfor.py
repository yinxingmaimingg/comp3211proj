#!/usr/bin/env python
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
		file = open("example/example1.cpp.gcov", "r")
		info = self.make2dList(self.file_len("example/example1.cpp.gcov"), 4)
		infoDict = {} 
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

		#print info[5:]
		print infoDict
 		#print file.read()
		

temp = CoverageInfor()
temp.readGcov()
