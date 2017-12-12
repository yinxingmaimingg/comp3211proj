from operator import itemgetter

def getSuspiciousnessForEachStatement(statementStatistic):
    passed = statementStatistic[0];
    totalPassed = statementStatistic[1] + passed;
    failed = statementStatistic[2];
    totalFailed = statementStatistic[3] + failed;
    hue = (passed / totalPassed) / (passed / totalPassed + failed / totalFailed);
    suspiciousness = 1 - hue;
    return suspiciousness;

def rankBySuspiciousness(statementStatistic):
    suspiciousness = [];
    i = 0;
    for statement in statementStatistic:
        i += 1;
        if statement[0] != -1:
            suspiciousness.append([i,getSuspiciousnessForEachStatement(statement)]);
    sorted(suspiciousness, key = itemgetter(1),reverse = True)
    return suspiciousness;

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
deleteUnuse("./SourceStatisticData/test.txt");
