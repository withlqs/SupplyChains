import os

from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
from django.contrib.auth import forms
from django.contrib.auth import views
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import *
from openpyxl.reader.excel import load_workbook

from SupplyChains.settings import BASE_DIR
from main.controller import *


# Create your views here.

admin = 'administrator'


def log(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/')
    username = request.user.get_username()
    if not username == admin:
        raise Http404
    models.Para.objects.raw(
        "SELECT Username,Param,Period,Value INTO OUTFILE '/tmp/log.csv' FROM SupplyChains.main_para;")
    file = open('/tmp/log.csv', 'rb').read()
    response = HttpResponse(file)
    response['Content-Disposition'] = "attachment; filename=%s" % 'log.csv'
    return response


def choose(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/')
    username = request.user.get_username()
    render_list = {}
    if username == admin:
        render_list['admin'] = True
    else:
        render_list['admin'] = False
    return render_to_response('choose.html', render_list)

def logout(request):
    if request.user.is_authenticated():
        auth.logout(request)
    return HttpResponseRedirect('/accounts/login/')


def getAttribute(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/')
    file = open(os.path.join(BASE_DIR, 'tmp/t.xlsx'), 'rb').read()
    response = HttpResponse(file)
    response['Content-Disposition'] = "attachment; filename=%s" % 'attribute.xlsx'
    return response


def simulate2(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/')
    username = request.user.get_username()
    if request.method == 'GET':
        if 'now' not in request.GET:
            return HttpResponseRedirect('/simulate2/?now=1')
        now = int(request.GET['now'])
        render_list = {
            'now': str(now),
            'last': str(now - 1)
        }
        if not now <= getN():
            render_list['form_disp'] = False
        else:
            render_list['form_disp'] = True
        if now != 1:
            render_list['info_disp'] = True
            render_list['TPDCUS'] = getTPDCUS2(username, now - 1)
            render_list['DCUSInv'] = getDCUSInv2(username, now - 1)
            render_list['SalesUS'] = getSalesUS2(username, now - 1)
            render_list['USInv'] = getUSInv2(username, now - 1)
            render_list['DCEUInv'] = getDCEUInv2(username, now - 1)
            render_list['TPDCEU'] = getTPDCEU2(username, now - 1)
            render_list['SalesEU'] = getSalesEU2(username, now - 1)
            render_list['EUInv'] = getEUInv2(username, now - 1)
            render_list['Profit'] = getProfit2(username, now - 1)
            lst = []
            for period in range(1, now):
                lst.append(getProfit2(username, period))
                # lst.append({
                #     'id': period,
                #     'profit': getProfit2(username, period)
                # })
            render_list['ProfitData'] = lst
            setGraphProfitVals(username,2,1.1314)
        else:
            render_list['info_disp'] = False
        return render_to_response('simulate2.html', render_list, context_instance=RequestContext(request))
    else:
        period = int(request.POST['now'])
        ClearData2(username, period)
        models.Para(Username=username, Param='EUProd', Period=period, Value=float(request.POST['ProdEU'])).save()
        models.Para(Username=username, Param='USProd', Period=period, Value=float(request.POST['ProdUS'])).save()
        Set(
            username,
            'USInv2',
            period,
            getUSInv2(username, period - 1)
            + getTPDCUS2(username, period - 1)
            - getSalesUS2(username, period - 1)
        )
        Set(
            username,
            'EUInv2',
            period,
            getEUInv2(username, period - 1)
            + getTPDCEU2(username, period - 1)
            - getSalesEU2(username, period - 1)
        )
        Set(
            username,
            'SalesUS2',
            period,
            min(getDemandUS(period), getUSInv2(username, period))
        )
        Set(
            username,
            'SalesEU2',
            period,
            min(getDemandEU(period), getEUInv2(username, period))
        )
        Set(
            username,
            'Profit2',
            period,
            (1 + getRate()) * getProfit2(username, period - 1)
            + getPriceUS() * getSalesUS2(username, period)
            + getRateEU(period) * getPriceEU() * getSalesEU2(username, period)
            - getRateCNY(period) * getCostProd(2) * (getUSProd(username, period) + getEUProd(username, period))
        )
        # username = request.user.get_username() #to change list: test to delete this line
        updateUserActivity(username)
        return HttpResponseRedirect('/simulate2/?now=' + str(period + 1))


def simulate(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/')
    username = request.user.get_username()
    if request.method == 'GET':
        if 'now' not in request.GET:
            return HttpResponseRedirect('/simulate/?now=1')
        now = int(request.GET['now'])
        render_list = {
            'now': str(now),
            'last': str(now - 1)
        }
        if not now <= getN():
            render_list['form_disp'] = False
        else:
            render_list['form_disp'] = True
        if now != 1:
            render_list['info_disp'] = True
            render_list['transUSEU'] = getUSEU(username, now - 1)
            render_list['transEUUS'] = getEUUS(username, now - 1)
            render_list['transDCUS'] = getDCUS(username, now - 1)
            render_list['transDCEU'] = getDCEU(username, now - 1)
            render_list['DCInv'] = getDCInv(username, now - 1)
            render_list['USInv'] = getUSInv(username, now - 1)
            render_list['EUInv'] = getEUInv(username, now - 1)
            render_list['SalesUS'] = getSalesUS(username, now - 1)
            render_list['SalesEU'] = getSalesEU(username, now - 1)
            render_list['Profit'] = getProfit(username, now - 1)
            lst = []
            for period in range(1, now):
                lst.append({
                    'id': period,
                    'profit': getProfit(username, period)
                })
            render_list['ProfitData'] = lst
            setGraphProfitVals(username,1,lst)
        else:
            render_list['info_disp'] = False
        return render_to_response('simulate.html', render_list, context_instance=RequestContext(request))
    else:
        period = int(request.POST['now'])
        ClearData1(username, period)
        models.Para(Username=username, Param='Prod', Period=period, Value=float(request.POST['Prod'])).save()
        models.Para(Username=username, Param='DCUS', Period=period, Value=float(request.POST['DCUS'])).save()
        models.Para(Username=username, Param='DCEU', Period=period, Value=float(request.POST['DCEU'])).save()
        models.Para(Username=username, Param='USEU', Period=period, Value=float(request.POST['USEU'])).save()
        models.Para(Username=username, Param='EUUS', Period=period, Value=float(request.POST['EUUS'])).save()
        Set(
            username,
            'DCInv',
            period,
            getDCInv(username, period - 1)
            + getProd(username, period - 1)
            - getDCUS(username, period - 1)
            - getDCEU(username, period - 1)
        )
        Set(
            username,
            'USInv',
            period,
            getUSInv(username, period - 1)
            + getTPDCUS(username, period - 1)
            + getTPEUUS(username, period - 1)
            - getUSEU(username, period - 1)
            - getSalesUS(username, period - 1)
        )
        Set(
            username,
            'EUInv',
            period,
            getEUInv(username, period - 1)
            + getTPDCEU(username, period - 1)
            + getTPUSEU(username, period - 1)
            - getEUUS(username, period - 1)
            - getSalesEU(username, period - 1)
        )
        Set(
            username,
            'SalesUS',
            period,
            min(getDemandUS(period), getUSInv(username, period) - getUSEU(username, period))
        )
        Set(
            username,
            'SalesEU',
            period,
            min(getDemandEU(period), getEUInv(username, period) - getEUUS(username, period))
        )
        Set(
            username,
            'Profit',
            period,
            (1 + getRate()) * getProfit(username, period - 1) + getPriceUS() * getSalesUS(username, period) + getRateEU(
                period) * getPriceEU() * getSalesEU(username, period) - getRateCNY(period) * getCostProd(1) * getProd(
                username, period) - getCostTranship() * (getUSEU(username, period) + getEUUS(username, period))
        )
        username = request.user.get_username()
        updateUserActivity(username)
        return HttpResponseRedirect('/simulate/?now=' + str(period + 1))


def success(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/')
    username = request.user.get_username()
    updateUserActivity(username)
    return render_to_response('success.html', context_instance=RequestContext(request))


def manage_view(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/')
    if not request.user.get_username() == admin:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        models.Attr.objects.all().delete()
        file = request.FILES.get('file')
        file_name = os.path.join(BASE_DIR, 'tmp/t.xlsx')
        keys = open(file_name, 'wb')
        for chunk in file.chunks():
            keys.write(chunk)
        keys.close()
        wb = load_workbook(file_name)
        N = int(wb['System']['A3'].value)
        ProdCost1 = float(wb['System']['B3'].value)
        ProdCost2 = float(wb['System']['C3'].value)
        PriceUS = float(wb['System']['D3'].value)
        PriceEU = float(wb['System']['E3'].value)
        Trans = float(wb['System']['F3'].value)
        Rate = float(wb['System']['G3'].value)
        models.Attr.objects.all().delete()
        models.Attr(Attri='N', Period=0, Value=N).save()
        models.Attr(Attri='CostProd1', Period=0, Value=ProdCost1).save()
        models.Attr(Attri='CostProd2', Period=0, Value=ProdCost2).save()
        models.Attr(Attri='PriceUS', Period=0, Value=PriceUS).save()
        models.Attr(Attri='PriceEU', Period=0, Value=PriceEU).save()
        models.Attr(Attri='CostTranship', Period=0, Value=Trans).save()
        models.Attr(Attri='Rate', Period=0, Value=Rate).save()
        for i in range(0, 15):
            models.Attr(Attri='DemandUS', Period=int(i + 1), Value=float(wb['Demand']['B' + str(3 + i)].value)).save()
            models.Attr(Attri='DemandEU', Period=int(i + 1), Value=float(wb['Demand']['C' + str(3 + i)].value)).save()
            models.Attr(Attri='RateCNY', Period=int(i + 1), Value=float(wb['Rate']['B' + str(3 + i)].value)).save()
            models.Attr(Attri='RateEU', Period=int(i + 1), Value=float(wb['Rate']['C' + str(3 + i)].value)).save()
        return HttpResponseRedirect('/success/')


    else:
        # users=getallusers()
        users= User.objects.all()
        para= getallusers()
        activities=getallactivities()
        graphs=getallgraphs()
        return render_to_response('manage.html', {'allusers':users,'para':para,'activities':activities,'graphs':graphs},context_instance=RequestContext(request))
        # return render_to_response('manage.html', )



def login(request):
    if request.user.is_authenticated():
        if request.user.get_username() == admin:
            return HttpResponseRedirect('/manage/')
        return HttpResponseRedirect('/')
    return views.login(request)


def profile(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    return HttpResponseRedirect('/accounts/login/')


def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            auth.login(request, user=authenticate(username=form.cleaned_data['username'],
                                                  password=form.cleaned_data['password1']))
            createUserActivity(form.cleaned_data['username'],timezone.now())
            return HttpResponseRedirect('/manage/')
    else:
        form = forms.UserCreationForm()
    return render_to_response('registration/register.html', {
        'form': form,
    }, context_instance=RequestContext(request))
