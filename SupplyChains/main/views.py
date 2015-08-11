from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
from django.contrib.auth import forms
from django.contrib.auth import views
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import *
from main import models

# Create your views here.

admin = 'administrator'

def manage_view(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    if not request.user.get_username() == admin:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        return Http404

def login(request):
    if request.user.is_authenticated():
        if request.user.get_username() == admin:
            return HttpResponseRedirect('/manager/')
        return HttpResponseRedirect('/')
    return views.login(request)

def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            auth.login(request, user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password1']))
            return HttpResponseRedirect('/successful/?op=reg')
    else:
        form = forms.UserCreationForm()
    return render_to_response('registration/register.html', {
        'form': form,
    }, context_instance=RequestContext(request))
