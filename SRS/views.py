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
    available=jobs.objects.all();
    applied=applied_jobs.objects.filter(user_name_id=user.objects.get(user_name=request.session['username']))
    return render(
        request,
        'JobOpening.html',{"available1":available,"applied":applied,"username" : request.session['username']}
    )


def applicant_details(request):
    if request.session.has_key('username'):
        try:
            udata = user_details.objects.get(user_name_id=request.session['username'])
            return render(request, 'ApplicantDetails.html', {"uname":request.session['username'],"data":udata})
        except:
            return render(request,'ApplicantDetails.html',{"uname":request.session['username']})
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

    if t==1:
        request.session['username']=username
    else:
        return render(
        request,
        'index.html',{"loginfailed":1}
    )
    return HttpResponseRedirect("index")

def myview_status(request):
    return render(
        request,
        'Status.html',{"applied":1}
    )

def savedata(request):
    if request.session.has_key('username'):
        if 'SubmitDetails' in request.POST:
            savedetails(request,1)
            #p.save()
            return render(request,'ApplicantDetails.html',{"uname":request.session['username'],"saved":"saved","data":user_details.objects.get(user_name_id=request.session['username'])
   })
    else:
        return render(request, 'index.html', {"loginfirst": 1})







