from .shaencrypt import encrypt_string
from django.shortcuts import render
from django.http import HttpResponseRedirect
#from .image import upload,replace
from .image import sign_up,check_login,savedetails
from requests import sessions,session
from django.contrib import messages
from .models import *
import datetime,time

def index(request):
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
    try:
        available=jobs.objects.all();
    except:
        return render(
            request,
            'JobOpening.html')
    try:
        if request.session.has_key("username"):
            applied=applied_jobs.objects.filter(user_name_id=user.objects.get(user_name=request.session['username']))
            avails=[]
            appls=[]
            for job in available:
                flag=0
                for ap in applied:
                    if ap.job_id_id==job.job_id:
                        flag=1
                        appls.append(job)
                        break
                print(flag)
                if flag == 0:
                    #print(job)
                    avails.append(job)
            #print(avails)
            return render(
            request,
            'JobOpening.html',{"avails":avails,"appls":appls,"username" : request.session['username']})
        return render(
        request,
        'JobOpening.html',{"available":available})
    except:
        return render(
            request,
            'JobOpening.html')


def applicant_details(request):
    if request.session.has_key('username'):
        try:
            import datetime,time
            now = datetime.datetime.now()
            format_iso_now = now.isoformat()
            unixtime = time.mktime(now.timetuple())
            c=int(unixtime)
            hash = encrypt_string(str(c))
            udata = user_details.objects.get(user_name_id=request.session['username'])
            return render(request, 'ApplicantDetails.html', {"uname":request.session['username'],"data":udata,"hash":hash,"timestamp":c})
        except:
            return render(request,'ApplicantDetails.html',{"uname":request.session['username'],"hash":hash,"timestamp":c})
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
    try:
        all_jobs = jobs.objects.all();
        applied = applied_jobs.objects.filter(user_name=request.session['username'])
        return render(
                request,
                'Status.html',{"username":request.session['username'],"applied" : applied, "all_jobs" : all_jobs})
    except:
        return render(request,'Status.html',{"username":request.session['username'], "applied" : applied})


def savedata(request):
    if request.session.has_key('username'):
        if 'SubmitDetails' in request.POST:
            savedetails(request,1)
        elif 'aadhaar' in request.POST:
            savedetails(request,2)
            #p.save()
        return render(request,'ApplicantDetails.html',{"uname":request.session['username'],"saved":"saved","data":user_details.objects.get(user_name_id=request.session['username'])
   })
    else:
        return render(request, 'index.html', {"loginfirst": 1})

def apply_to_job(request,ID=0):
    if ID == 0:
        return render(request, 'index.html')
    elif request.session.has_key('username'):
        try:
            applied_jobs.objects.create(dof_app=datetime.datetime.today(),status=1,job_id_id=ID,user_name_id=request.session['username'])
            return HttpResponseRedirect("/JobOpenings")
        except:
            return render(request, 'index.html', {"loginfirst": 1})
    else:
        return render(request, 'index.html', {"loginfirst": 1})







