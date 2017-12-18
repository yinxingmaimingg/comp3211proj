from operator import itemgetter

def getSuspiciousnessForEachStatement(statementStatistic):
    passed = statementStatistic[0];
    if passed == 0:
        passed = 1;
    totalPassed = statementStatistic[1] + passed;
    failed = statementStatistic[2];
    if failed == 0:
        failed = 1;
    totalFailed = statementStatistic[3] + failed;
    hue = (passed / totalPassed) / (passed / totalPassed + failed / totalFailed);
    suspiciousness = 1 - hue;
    return suspiciousness;

def rankBySuspiciousness(statementStatistic):
    suspiciousness = [];
    i = 0;
    for statement in statementStatistic:
        if statement[0] != -1:
            suspiciousness.append([i,getSuspiciousnessForEachStatement(statement)]);
        i += 1;
    sus = sorted(suspiciousness, key = itemgetter(1),reverse = True)
    return sus;

def deleteUnuse(origin, out):
    f = open(origin,'r');
    o = open(out, 'w');
    for line in f:
        str = '';
        for i in line:
            if i == "{" or i == "}" or i == ",":
                continue;
            else:
                str += i;
        o.write(str);
    f.close();
    o.close();

def preProcess(doc):
    f = open(doc, 'r');
    statistic = [[-1,-1,-1,-1,-1]] * 1000;
    max = -1;
    for line in f:
        lineElement = line.split();
        index = int(lineElement[0][:-1]);
        if index > max:
            max = index;
        element1 = int(lineElement[1][1:]);
        element2 = int(lineElement[2]);
        element3 = int(lineElement[3]);
        element4 = int(lineElement[4][:-1]);
        statistic[index] = [element1, element2, element3, element4];
    return statistic, max;

for i in range(10):
    statistic, max = preProcess("../coverage/coverage_1_" + str(i) + ".txt");
    rank = rankBySuspiciousness(statistic);
    print("\nProblem 1 Bug Program:" + str(i) + ": ");
    for item in rank:
        print(str(item[0]) + ": " + str(item[1]));


for i in range(10):
    statistic, max = preProcess("../coverage/coverage_2_" + str(i) + ".txt");
    rank = rankBySuspiciousness(statistic);
    print("\nProblem 2 Bug Program:" + str(i) + ": ");
    for item in rank:
        print(str(item[0]) + ": " + str(item[1]));
