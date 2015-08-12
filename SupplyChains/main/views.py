from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
from django.contrib.auth import forms
from django.contrib.auth import views
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import *
from SupplyChains.settings import BASE_DIR
import os
from openpyxl.reader.excel import load_workbook
from main import models

# Create your views here.

admin = 'administrator'


def getN():
    return int(models.Attr.objects.get(Attri='N').Value)


def getDCInv(username, period):
    if period == 0:
        return 0
    return float(models.Para.objects.get(Username=username, Para='DCInv', Period=period).Value)


def getUSInv(username, period):
    return float(models.Para.objects.get(Username=username, Para='USInv', Period=period).Value)


def getEUInv(username, period):
    return float(models.Para.objects.get(Username=username, Para='EUInv', Period=period).Value)


def getSalesUS(username, period):
    return float(models.Para.objects.get(Username=username, Para='SalesUS', Period=period).Value)


def getSalesEU(username, period):
    return float(models.Para.objects.get(Username=username, Para='SalesEU', Period=period).Value)


def getProfit(username, period):
    return float(models.Para.objects.get(Username=username, Para='Profit', Period=period).Value)


def ClearPeriod(username):
    models.Para.objects.filter(Username=username).delete()


def getAttribute(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/')
    file = open(os.path.join(BASE_DIR, 'tmp/s.xlsx'))
    data = file.read()
    file.close()
    filename = 'system_attributes.xlsx'
    response = HttpResponse(data, mimetype='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response


def simulate(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/')
    username = request.user.get_username()
    if request.method == 'GET':
        if 'now' not in request.GET:
            return HttpResponseRedirect('/simulate/?now=1')
        now = int(request.GET['now'])
        render_list = {
            'now': str(now + 1)
        }
        if not now + 1 <= getN():
            render_list['form_disp'] = False
        else:
            render_list['form_disp'] = True
        if now != 1:
            render_list['info_disp'] = True
            render_list['DCInv'] = getDCInv(username, now - 1)
            render_list['USInv'] = getUSInv(username, now - 1)
            render_list['EUInv'] = getEUInv(username, now - 1)
            render_list['SalesUS'] = getSalesUS(username, now - 1)
            render_list['SalesEU'] = getSalesEU(username, now - 1)
            render_list['Profit'] = getProfit(username, now - 1)
        else:
            render_list['info_disp'] = False
            ClearPeriod(username)
        render_to_response('simulate.html', render_list, context_instance=RequestContext(request))
    else:
        period = int(request.POST['now'])
        models.Para(Username=username, Param='Prod', Period=period, Value=float(request.POST['Prod'])).save()
        models.Para(Username=username, Param='DCUS', Period=period, Value=float(request.POST['DCUS'])).save()
        models.Para(Username=username, Param='DCEU', Period=period, Value=float(request.POST['DCEU'])).save()
        models.Para(Username=username, Param='USEU', Period=period, Value=float(request.POST['USEU'])).save()
        models.Para(Username=username, Param='EUUS', Period=period, Value=float(request.POST['EUUS'])).save()


def success(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/')
    return render_to_response('success.html', context_instance=RequestContext(request))

def manage_view(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/')
    if not request.user.get_username() == admin:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
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
        models.Attr(Attri='N', Period=0, Value=N).save()
        models.Attr(Attri='ProdCost1', Period=0, Value=ProdCost1).save()
        models.Attr(Attri='ProdCost2', Period=0, Value=ProdCost2).save()
        models.Attr(Attri='PriceUS', Period=0, Value=PriceUS).save()
        models.Attr(Attri='PriceEU', Period=0, Value=PriceEU).save()
        models.Attr(Attri='Trans', Period=0, Value=Trans).save()
        models.Attr(Attri='Rate', Period=0, Value=Rate).save()
        for i in range(0, 15):
            models.Attr(Attri='DemandUS', Period=int(i+1), Value=float(wb['Demand']['B'+str(3+i)].value)).save()
            models.Attr(Attri='DemandEU', Period=int(i+1), Value=float(wb['Demand']['C'+str(3+i)].value)).save()
            models.Attr(Attri='RateCNY', Period=int(i+1), Value=float(wb['Rate']['B'+str(3+i)].value)).save()
            models.Attr(Attri='RateEU', Period=int(i+1), Value=float(wb['Rate']['C'+str(3+i)].value)).save()
        return HttpResponseRedirect('/success/')
    else:
        return render_to_response('manage.html', context_instance=RequestContext(request))

def login(request):
    if request.user.is_authenticated():
        if request.user.get_username() == admin:
            return HttpResponseRedirect('/manage/')
        return HttpResponseRedirect('/simulate/')
    return views.login(request)

def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            auth.login(request, user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password1']))
            return HttpResponseRedirect('/manage/')
    else:
        form = forms.UserCreationForm()
    return render_to_response('registration/register.html', {
        'form': form,
    }, context_instance=RequestContext(request))
