from django.shortcuts import render

# Create your views here.

def admin(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/');
    
