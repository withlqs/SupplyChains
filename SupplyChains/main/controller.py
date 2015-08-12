from main import models


def getUSEU(username, period):
    return float(models.Para.objects.get(Username=username, Para='USEU', Period=period).Value)


def getTPDCUS(username, period):
    if period <= 1:
        return 0
    period -= 1
    return float(models.Para.objects.get(Username=username, Para='TPDCUS', Period=period).Value)


def getTPDCEU(username, period):
    if period <= 1:
        return 0
    period -= 1
    return float(models.Para.objects.get(Username=username, Para='TPDCEU', Period=period).Value)


def getTPUSEU(username, period):
    if period <= 1:
        return 0
    period -= 1
    return float(models.Para.objects.get(Username=username, Para='TPUSEU', Period=period).Value)


def getTPEUUS(username, period):
    if period <= 1:
        return 0
    period -= 1
    return float(models.Para.objects.get(Username=username, Para='TPEUUS', Period=period).Value)


def Set(username, para, period, value):
    models.Para(Username=username, Param=para, Period=period, Value=value).save()


def getDCEU(username, period):
    return float(models.Para.objects.get(Username=username, Para='DCEU', Period=period).Value)


def getDCUS(username, period):
    return float(models.Para.objects.get(Username=username, Para='DCUS', Period=period).Value)


def getProd(username, period):
    return float(models.Para.objects.get(Username=username, Para='Prod', Period=period).Value)


def getN():
    return int(models.Attr.objects.get(Attri='N').Value)


def getDCInv(username, period):
    if period == 0:
        return 0
    return float(models.Para.objects.get(Username=username, Para='DCInv', Period=period).Value)


def getUSInv(username, period):
    if period == 0:
        return 0
    return float(models.Para.objects.get(Username=username, Para='USInv', Period=period).Value)


def getEUInv(username, period):
    if period == 0:
        return 0
    return float(models.Para.objects.get(Username=username, Para='EUInv', Period=period).Value)


def getSalesUS(username, period):
    if period == 0:
        return 0
    return float(models.Para.objects.get(Username=username, Para='SalesUS', Period=period).Value)


def getSalesEU(username, period):
    if period == 0:
        return 0
    return float(models.Para.objects.get(Username=username, Para='SalesEU', Period=period).Value)


def getProfit(username, period):
    if period == 0:
        return 0
    return float(models.Para.objects.get(Username=username, Para='Profit', Period=period).Value)


def ClearPeriod(username):
    models.Para.objects.filter(Username=username).delete()
