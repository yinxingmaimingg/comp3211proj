import sys
import random

# 10 elements for each case
bugInfor = [
	[
		[6, "return k < 0 ? -k : k;", "return k > 0 ? -k : k;"],
		[18, "if (a[i] == -1 && i < n - 1)", "if (a[i] == -1 || i < n - 1)"],
		[20, "else if (a[i] != 1 || i == n - 1)", "else if (a[i] != 1 && i == n - 1)"],
		[22, "if (i == n - 2) // MARK 1", "if (i <= n - 2) // MARK 1"],
		[24, "else if (i < n - 1) // MARK 1", "else if (i < n + 1) // MARK 1"],
		[25, "cout << \"x^\" << n - i - 1;", "cout << \"x^\" << n - i + 1;"],
		[28, "cout << ' ' << (a[i] < 0 ? '-' : '+') << ' ';", "cout << ' ' << (a[i] < 10 ? '-' : '+') << ' ';"],
		[29, "if (fabs(a[i]) != 1 || i == n - 1)", "if (fabs(a[i]) != 1 && i == n - 1)"],
		[33, "else if (i < n - 1) // MARK 2", "else if (i < n + 1) // MARK 2"],
		[38, "cout << 0;", "cout << 1;"]
	],
	[
		[8, "if (year % 400 == 0)", "if (year % 40 == 0)"],
		[14, "if (year % 4 == 0)", "if (year % 4 != 0)"],
		[15, "return 366; // MARK 1", "return 366; // MARK 1"],
		[23, "if (month == 2){", "if (month == 1){"],
		[24, "if (days_of_year(year)==366)", "if (days_of_year(year)==365)"],
		[25, "return 29;", "return 28;"],
		[32, "case 1: case 3: case 5: case 7: case 8:", "case 1: case 3: case 5: case 7: case 9:"],
		[55, "++year;", "year += 2;"],
		[57, "n -= days_of_month(month, year);", "n += days_of_month(month, year);"],
		[60, "day += n;", "day = n;"]
	]
]

def insBug(programNo, bugNo=-1):
	if (bugNo==-1):
		bugNo = random.randint(0, 9)
	targetBug = bugInfor[programNo-1][bugNo]

	fGood = open("testCase" + str(programNo) + ".cpp", 'r')
	fData = fGood.read()
	fData = fData.replace(targetBug[1], targetBug[2])
	fBug = open("testCase" + str(programNo) + "WithBug" + str(bugNo) + ".cpp", 'w')
	fBug.write(fData);
	fGood.close()
	fBug.close()

	fLocation = open("../coverage/bugLocation_" + str(programNo) + "_" + str(bugNo) + ".txt", 'w')
	fLocation.write(str(targetBug[0]) + "#" + targetBug[1] + "#" + targetBug[2] + "\n");
	fLocation.close()



if __name__=="__main__":
	programNo = (int)(sys.argv[1])
	bugNo = (int)(sys.argv[2])
	insBug(programNo, bugNo)
