from main import models
from django.contrib.auth.models import User, Permission
from django.db.models import Q
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist



def ClearData1(username, period):
    models.Para.objects.filter(Username=username, Period=period, Param='Prod').delete()
    models.Para.objects.filter(Username=username, Period=period, Param='DCUS').delete()
    models.Para.objects.filter(Username=username, Period=period, Param='DCEU').delete()
    models.Para.objects.filter(Username=username, Period=period, Param='USEU').delete()
    models.Para.objects.filter(Username=username, Period=period, Param='EUUS').delete()
    models.Para.objects.filter(Username=username, Period=period, Param='DCInv').delete()
    models.Para.objects.filter(Username=username, Period=period, Param='USInv').delete()
    models.Para.objects.filter(Username=username, Period=period, Param='EUInv').delete()
    models.Para.objects.filter(Username=username, Period=period, Param='SalesUS').delete()
    models.Para.objects.filter(Username=username, Period=period, Param='SalesEU').delete()
    models.Para.objects.filter(Username=username, Period=period, Param='Profit').delete()


def ClearData2(username, period):
    models.Para.objects.filter(Username=username, Period=period, Param='EUProd').delete()
    models.Para.objects.filter(Username=username, Period=period, Param='USProd').delete()
    models.Para.objects.filter(Username=username, Period=period, Param='USInv2').delete()
    models.Para.objects.filter(Username=username, Period=period, Param='EUInv2').delete()
    models.Para.objects.filter(Username=username, Period=period, Param='SalesUS2').delete()
    models.Para.objects.filter(Username=username, Period=period, Param='SalesEU2').delete()
    models.Para.objects.filter(Username=username, Period=period, Param='Profit2').delete()

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

#### Customize Function: Get all
def getallusers():
    # perm = Permission.objects.get(codename='blogger')
    # users = User.objects.filter(Q(groups__permissions=perm) | Q(user_permissions=perm) ).distinct()
    users=models.Para.objects.all()
    return users

def getallactivities():
    activities=models.UserUtil.objects.all()
    return activities
def getallgraphs():
    graphs=models.UserGraphUtil.objects.all()
    return graphs


#### Customize Function: Monitoring Activities
def createUserActivity(username, activitydatetime):
    models.UserUtil(Username=username, last_activity=activitydatetime).save()

def updateUserActivity(username):
    setUserActivity(username,timezone.now())

def setUserActivity(username, activitydatetime):
    try:
        obj=models.UserUtil.objects.get(Username=username)
        obj.last_activity=activitydatetime
        obj.save()
    except ObjectDoesNotExist:
        createUserActivity(username,timezone.now())
    # models.UserUtil(Username=username, last_activity=activitydatetime).save()



#### Customize Function: Monitoring Graphs
def createProfitGraphVals(username,mode,vals):
    models.UserGraphUtil(Username=username,graph_mode=mode,profit_vals=vals).save()

def setGraphProfitVals(username,mode,vals):
    try:
        obj=models.UserGraphUtil.objects.get(Username=username,graph_mode=mode)
        obj.profit_vals=vals
        obj.save()
    except ObjectDoesNotExist:
        createProfitGraphVals(username,mode,vals)


