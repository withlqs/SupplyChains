from main import models

def getProfit2(username, period):
    if period == 0:
        return 0
    return float(models.Para.objects.get(Username=username, Param='Profit2', Period=period).Value)

def getUSInv2(username, period):
    if period == 0:
        return 0
    return float(models.Para.objects.get(Username=username, Param='USInv2', Period=period).Value)

def getEUInv2(username, period):
    if period == 0:
        return 0
    return float(models.Para.objects.get(Username=username, Param='EUInv2', Period=period).Value)

def getSalesUS2(username, period):
    if period == 0:
        return 0
    return float(models.Para.objects.get(Username=username, Param='SalesUS2', Period=period).Value)

def getSalesEU2(username, period):
    if period == 0:
        return 0
    return float(models.Para.objects.get(Username=username, Param='SalesEU2', Period=period).Value)

def getDCUSInv2(username, period):
    if period == 0:
        return 0
    return getUSProd(username, period-1)

def getDCEUInv2(username, period):
    if period == 0:
        return 0
    return getEUProd(username, period-1)

def getTPDCUS2(username, period):
    if period <= 1:
        return 0
    period -= 1
    return getDCUSInv2(username, period)

def getTPDCEU2(username, period):
    if period <= 1:
        return 0
    period -= 1
    return getDCEUInv2(username, period)

def getEUProd(username, period):
    if period == 0:
        return 0
    return float(models.Para.objects.get(Username=username, Param='EUProd', Period=period).Value)

def getUSProd(username, period):
    if period == 0:
        return 0
    return float(models.Para.objects.get(Username=username, Param='USProd', Period=period).Value)

def getCostTranship():
    return float(models.Attr.objects.get(Attri='CostTranship').Value)

def getCostProd(id):
    return float(models.Attr.objects.get(Attri=('CostProd' + str(id))).Value)


def getRateEU(period):
    return float(models.Attr.objects.get(Attri='RateEU', Period=period).Value)


def getRateCNY(period):
    return float(models.Attr.objects.get(Attri='RateCNY', Period=period).Value)


def getPriceEU():
    return float(models.Attr.objects.get(Attri='PriceEU').Value)


def getPriceUS():
    return float(models.Attr.objects.get(Attri='PriceUS').Value)


def getRate():
    return float(models.Attr.objects.get(Attri='Rate').Value)


def getDemandEU(period):
    if period == 0:
        return 0
    return float(models.Attr.objects.get(Attri='DemandEU', Period=period).Value)


def getDemandUS(period):
    if period == 0:
        return 0
    return float(models.Attr.objects.get(Attri='DemandUS', Period=period).Value)


def getEUUS(username, period):
    if period == 0:
        return 0
    return float(models.Para.objects.get(Username=username, Param='EUUS', Period=period).Value)
def getUSEU(username, period):
    if period == 0:
        return 0
    return float(models.Para.objects.get(Username=username, Param='USEU', Period=period).Value)


def getTPDCUS(username, period):
    if period <= 1:
        return 0
    period -= 1
    return getDCUS(username, period)


def getTPDCEU(username, period):
    if period <= 1:
        return 0
    period -= 1
    return getDCEU(username, period)


def getTPUSEU(username, period):
    if period <= 1:
        return 0
    period -= 1
    return getUSEU(username, period)


def getTPEUUS(username, period):
    if period <= 1:
        return 0
    period -= 1
    return getEUUS(username, period)


def Set(username, para, period, value):
    models.Para(Username=username, Param=para, Period=period, Value=value).save()


def getDCEU(username, period):
    if period == 0:
        return 0
    return float(models.Para.objects.get(Username=username, Param='DCEU', Period=period).Value)


def getDCUS(username, period):
    if period == 0:
        return 0
    return float(models.Para.objects.get(Username=username, Param='DCUS', Period=period).Value)


def getProd(username, period):
    if period == 0:
        return 0
    return float(models.Para.objects.get(Username=username, Param='Prod', Period=period).Value)


def getN():
    return int(models.Attr.objects.get(Attri='N').Value)


def getDCInv(username, period):
    if period == 0:
        return 0
    return float(models.Para.objects.get(Username=username, Param='DCInv', Period=period).Value)


def getUSInv(username, period):
    if period == 0:
        return 0
    return float(models.Para.objects.get(Username=username, Param='USInv', Period=period).Value)


def getEUInv(username, period):
    if period == 0:
        return 0
    return float(models.Para.objects.get(Username=username, Param='EUInv', Period=period).Value)


def getSalesUS(username, period):
    if period == 0:
        return 0
    return float(models.Para.objects.get(Username=username, Param='SalesUS', Period=period).Value)


def getSalesEU(username, period):
    if period == 0:
        return 0
    return float(models.Para.objects.get(Username=username, Param='SalesEU', Period=period).Value)


def getProfit(username, period):
    if period == 0:
        return 0
    return float(models.Para.objects.get(Username=username, Param='Profit', Period=period).Value)


def ClearUserData(username):
    models.Para.objects.filter(Username=username).delete()
