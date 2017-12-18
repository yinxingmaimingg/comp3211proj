from operator import itemgetter

def chiSquare(crossTab):
    ncs = crossTab[0][0];
    nus = crossTab[0][1];
    ns = crossTab[0][2];
    ncf = crossTab[1][0];
    nuf = crossTab[1][1];
    nf = crossTab[1][2];
    nc = crossTab[2][0];
    nu = crossTab[2][1];
    n = crossTab[2][2];
    ecf = nc * nf / n;
    ecs = nc * ns / n;
    euf = nu * nf / n;
    eus = nu * ns / n;
    chiSquareValue = (ncf - ecf) ** 2 / ecf + (ncs - ecs) ** 2 / ecs + (nuf - euf) ** 2 / euf + (nus - eus) ** 2 / eus;
    return chiSquareValue;

def cotingencyCoefficient(chiSquareValue, totalTest):
    return chiSquareValue / totalTest;

def getStatisticValue(crossTab):
    if crossTab[0][0] == 0:
        crossTab[0][0] = 1;
    return (crossTab[1][0] / crossTab[1][2]) / (crossTab[0][0] / crossTab[0][2]);

def getSuspiciousValue(cotingencyCoefficient, statisticValue):
    if statisticValue == 1:
        return 0;
    elif statisticValue > 1:
        return cotingencyCoefficient;
    else:
        return -1 * cotingencyCoefficient;

def getSuspiciousValueForEachStatement(statement):
    crossTableValue = getCrossTableForEachStatement(statement);
    chiSquareValue = chiSquare(crossTableValue);
    contingencyCoefficientValue = cotingencyCoefficient(chiSquareValue, crossTableValue[2][2]);
    suspiciousValue = getSuspiciousValue(contingencyCoefficientValue, getStatisticValue(crossTableValue));
    return suspiciousValue;

def rankBySuspicious(statementStatistic):
    suspiciousness = [];
    i = 0;
    for statement in statementStatistic:
        if statement[0] != -1:
            suspiciousness.append([i, getSuspiciousValueForEachStatement(statement)]);
        i += 1;
    sus = sorted(suspiciousness, key=itemgetter(1), reverse=True)
    return sus;

def getCrossTableForEachStatement(statement):
    passCover = statement[0];
    passNotCover = statement[1];
    failCover = statement[2];
    failNotCover = statement [3];
    totalPass = passCover + passNotCover;
    totalFail = failCover + failNotCover;
    totalCover = passCover + failCover;
    totalNotCover = passNotCover + failNotCover;
    totalTest = totalPass + totalFail;
    if totalCover == 0:
        totalCover += 1;
    if totalNotCover == 0:
        totalNotCover += 1;
    if totalFail == 0:
        totalFail = 1;
    if totalPass == 0:
        totalPass = 1;
    return [[passCover,passNotCover, totalPass], [failCover,failNotCover,totalFail], [totalCover,totalNotCover,totalTest]];

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

for i in range(10):
    deleteUnuse("../coverage/coverage_1_" + str(i) + ".txt", "../CoverageUsed/coverage_1_" + str(i) + ".txt");
    deleteUnuse("../coverage/coverage_2_" + str(i) + ".txt", "../CoverageUsed/coverage_2_" + str(i) + ".txt");
    
for i in range(10):
    statistic, max = preProcess("../CoverageUsed/coverage_1_" + str(i) + ".txt");
    f = open("../coverage/bugLocation_1_" + str(i) + ".txt");
    for line in f:
        lineElement = line.split("#");
        hit = lineElement[0];
    rank = rankBySuspicious(statistic);
    print("\nProblem 1 Bug Program:" + str(i) + ": ");
    previous = 100;
    count = 0;
    final = 0;
    for item in rank:
        if item[1] != previous:
            count += 1;
        previous = item [1];
        if str(item[0]) == str(hit):
            print(str(item[0]) + ": " + str(item[1]) + "     hit ");
            final = count;
        print(str(item[0]) + ": " + str(item[1]));
    print("The buggy line rank: " + str(final));


for i in range(10):
    statistic, max = preProcess("../CoverageUsed/coverage_2_" + str(i) + ".txt");
    f = open("../coverage/bugLocation_2_" + str(i) + ".txt");
    for line in f:
        lineElement = line.split("#");
        hit = lineElement[0];
    rank = rankBySuspicious(statistic);
    print("\nProblem 1 Bug Program:" + str(i) + ": ");
    previous = 100;
    count = 0;
    final = 0;
    for item in rank:
        if item[1] != previous:
            count += 1;
        previous = item [1];
        if str(item[0]) == str(hit):
            print(str(item[0]) + ": " + str(item[1]) + "     hit ");
            final = count;
        print(str(item[0]) + ": " + str(item[1]));
    print("The buggy line rank: " + str(final));

