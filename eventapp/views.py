from django.shortcuts import render
from .models import Participant, ParticipantAdmin
# Create your views here.
def home(request):
    context={}
    return render(request,"eventapp/home.html",context)

def register(request):
    context={}
    if request.method == 'POST':
        p1 = Participant()
        p1.name = request.POST.get('username','-')
        p1.inst = request.POST.get('institute','-')
        p1.email = request.POST.get('emailid','-')
        p1.contnum = request.POST.get('phnumber','000')

        if len(Participant.objects.all()) > 10:
            return render(request, 'eventapp/failure.html',context)
        else:
            p1.save()
            return render(request, 'eventapp/success.html',context)

    if request.method == 'GET':
        context['name'] = ''
        context['inst'] = ''
        context['email'] = ''
        context['contnum'] = ''

    return render(request,"eventapp/register.html",context)
    
def listofparticipants(request):
    context={}
    context['participants'] = Participant.objects.all()
    return render(request,"eventapp/participants.html",context)


def success(request):
    context={}
    return render(request,"eventapp/success.html",context)

def fail(request):
    context={}
    return render(request,"eventapp/failure.html",context)
