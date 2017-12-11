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
        i += 1;
        if statement[0] != -1:
            suspiciousness.append([i, getSuspiciousValueForEachStatement(statement)]);
    sorted(suspiciousness, key=itemgetter(1), reverse=True)
    return suspiciousness;

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
    return [[passCover,passNotCover, totalPass], [failCover,failNotCover,totalFail], [totalCover,totalNotCover,totalTest]];
