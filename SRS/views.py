from .shaencrypt import encrypt_string
from django.shortcuts import render
from django.http import HttpResponseRedirect
#from .image import upload,replace
from .image import sign_up,check_login,savedetails
from requests import sessions,session
from django.contrib import messages
from .models import *

def index(request):
    import datetime,time
    now = datetime.datetime.now()
    format_iso_now = now.isoformat()
    unixtime = time.mktime(now.timetuple())
    c=int(unixtime)
    en = encrypt_string(str(c))
    #print(int(unixtime))
    if request.method == 'POST':# and request.POST.get("Submit_SignUp"):
        username=request.POST.get("Email")
        password=request.POST.get("Password")
        mobile_no=request.POST.get("Mobile")
        sign_up(username,password,mobile_no)
        return HttpResponseRedirect('/')

    if request.session.has_key('username'):
        print("logged in")
        return render(
        request,
        'index.html',{"username" : request.session['username']})

    return render(
        request,
        'index.html')


    #myForm = CustomForm(request.POST)
    '''action=1
    if(action==1):
        upload("Amruta", 3,"/home/super--user/cap.png")
    else:
        replace("Amruta", 2,"/home/super--user/test.png")'''



def myview_job(request):

    return render(
        request,
        'JobOpening.html',
    )


def applicant_details(request):
    if request.session.has_key('username'):
        return render(request,'ApplicantDetails.html',)
    return render(request,'index.html',{"loginfirst" :1 })



def logout(request):
   try:
      del request.session['username']
   except:
      pass
   return render(
       request,
       'index.html',
   )



def login(request):
    username = request.POST.get("Email")
    password = request.POST.get("Password")
    t=check_login(username,password)
    try:
      del request.session['username']
    except:
      pass

    if request.session.has_key('username'):
        return HttpResponseRedirect("index")
    if t==1:
        request.session['username']=username
    else:
        return render(
        request,
        'JobOpening.html',
    )
    return HttpResponseRedirect("index")

def myview_status(request):
    return render(
        request,
        'Status.html',
    )

def savedata(request):
    if request.session.has_key('username'):
        if 'SubmitDetails' in request.POST:
            #savedetails(request)
            instance = user.objects.get(user_name=request.session['username'])
            user_details.objects.create(user_name=instance,first_name=request.POST.get('FirstName'), middle_name=request.POST.get('MiddleName'),last_name=request.POST.get('LastName'), address=request.POST.get('Address'),country=request.POST.get('Country'), state=request.POST.get('State'),gender=request.POST.get('Gender'))
            #p.save()
            return HttpResponseRedirect('index')
        return render(request, 'index.html', {"loginfirst": 1})
    else:
        return HttpResponseRedirect('index')







