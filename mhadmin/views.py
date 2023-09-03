from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from mhadmin.models import servicedb,designdb,projectdb,jobdb
from mhuser.models import contactdb,Applicantdb


# Create your views here.
def index_page(req):
    return render(req,"index.html")

def addserv(req):
    return render(req,"addservice.html")

def serviceadd(req):
    if req.method=="POST":
        snam=req.POST.get('sname')
        desc=req.POST.get('sdescript')
        img=req.FILES['image']
        obj=servicedb(service_name=snam,Description=desc,Image=img)
        obj.save()
        messages.success(req,"SERVICE ADDED SUCCESSFULLY")
        return redirect(addserv)

def displayservc(req):
    data=servicedb.objects.all()
    return render(req,"displayservice.html",{'data':data})


def editservc(req,servcid):
    service=servicedb.objects.get(id=servcid)
    return render(req,"editservice.html",{'service':service})

def updateservc(req,servcid):
    if req.method=="POST":
        snam = req.POST.get('sname')
        desc = req.POST.get('sdescript')
    try:
        im=req.FILES['image']
        fs=FileSystemStorage()
        file=fs.save(im.name,im)
    except MultiValueDictKeyError:
        file=servicedb.objects.get(id=servcid).Image
    servicedb.objects.filter(id=servcid).update(service_name=snam,Description=desc,Image=file)
    messages.success(req, "SERVICE UPDATE SUCCESSFULLY")
    return redirect(displayservc)

def deleteservc(req,servcid):
    data=servicedb.objects.filter(id=servcid)
    data.delete()
    return redirect(displayservc)


def adddesign(req):
    data=servicedb.objects.all()
    return render(req,"adddesign.html",{'data':data})


def designadd(req):
    if req.method=="POST":
        snam=req.POST.get('sname')
        dnam=req.POST.get('dname')
        dscp=req.POST.get('sdescript')
        dimg=req.FILES['image']
        obj2=designdb(Service=snam,Design_Name=dnam,Description=dscp,Image=dimg)
        obj2.save()
        messages.success(req,"DESIGN ADDED SUCCESSFULLY")
        return redirect(adddesign)

def displaydesign(req):
    data=designdb.objects.all()
    return render(req,"displaydesign.html",{'data':data})

def editdesign(req,desid):
    design=designdb.objects.get(id=desid)
    return render(req,"editdesign.html",{'design':design})

def updatedesign(req,desid):
    if req.method == "POST":
        snam = req.POST.get('sname')
        dnam = req.POST.get('dname')
        dscp = req.POST.get('sdescript')
    try:
        dm = req.FILES['image']
        fs = FileSystemStorage()
        file = fs.save(dm.name, dm)
    except MultiValueDictKeyError:
        file=designdb.objects.get(id=desid).Image
    designdb.objects.filter(id=desid).update(Service=snam,Design_Name=dnam,Description=dscp,Image=file)
    messages.success(req, "DESIGN UPDATED SUCCESSFULLY")
    return redirect(displaydesign)

def deldesign(req,desid):
    data=designdb.objects.filter(id=desid)
    data.delete()
    messages.success(req, "DESIGN DELETED SUCCESSFULLY")
    return redirect(displaydesign)


def addproject(req):
    return render(req,"addproject.html")

def projectadd(req):
    if req.method=="POST":
        pnam=req.POST.get('pnam')
        pdscp=req.POST.get('pdescript')
        pimg=req.FILES['image']
        obj3=projectdb(Project_name=pnam,Description=pdscp,Image=pimg)
        obj3.save()
        messages.success(req,"PROJECT ADDED SUCCESSFULLY")
        return redirect(addproject)

def displayproject(req):
    data=projectdb.objects.all()
    return render(req,"displayproject.html",{'data':data})

def editproject(req,proid):
    project=projectdb.objects.get(id=proid)
    return render(req,"editproject.html",{'project':project})

def updateproject(req,proid):
    if req.method=="POST":
        pnam = req.POST.get('pnam')
        pdscp = req.POST.get('pdescript')
    try:
        dm = req.FILES['image']
        fs = FileSystemStorage()
        file = fs.save(dm.name, dm)
    except MultiValueDictKeyError:
        file=projectdb.objects.get(id=proid).Image
    projectdb.objects.filter(id=proid).update(Project_name=pnam,Description=pdscp,Image=file)
    messages.success(req, "PROJECT UPDATED SUCCESSFULLY")
    return redirect(displayproject)

def deleteproject(req,proid):
    data = projectdb.objects.filter(id=proid)
    data.delete()
    messages.success(req, "PROJECT DELETED SUCCESSFULLY")
    return redirect(displayproject)


def adlogin(req):
    return render(req,"login.html")

def adminlogin(req):
    if req.method=="POST":
        un=req.POST.get("uname")
        pd=req.POST.get("pwd")
        if User.objects.filter(username__contains=un).exists():
            user=authenticate(username=un,password=pd)
            if user is not None:
                login(req,user)
                req.session['username']=un
                req.session['password']=pd
                messages.success(req, "LOGIN SUCCESSFULLY")
                return redirect(index_page)
            else:
                messages.error(req, "INVALID USERNAME OR PASSWORD")
                return redirect(adlogin)

        else:
            messages.error(req, "INVALID USERNAME OR PASSWORD")
            return redirect(adlogin)

def adlogout(req):
    del req.session['username']
    del req.session['password']
    messages.success(req, "LOGOUT SUCCESSFULLY")
    return redirect(adlogin)

def contactdisplay(req):
    data=contactdb.objects.all()
    return render(req,"displaycontact.html",{'data':data})


def search(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = contactdb.objects.filter(Subject=query)
    return render(request, 'displaycontact.html', {'results': results, 'query': query})


def deletecontact(req,cid):
    data=contactdb.objects.filter(id=cid)
    data.delete()
    messages.success(req, "CONTACT DELETED SUCCESSFULLY")
    return redirect(contactdisplay)


def jobb_pg(req):
    return render(req,"jobopen.html")

def addjob(req):
    if req.method=="POST":
        post=req.POST.get('post')
        des=req.POST.get('descp')
        obj=jobdb(Position=post,Description=des)
        obj.save()
        return redirect(jobb_pg)

def disp_job(req):
    data=jobdb.objects.all()
    return render(req,"display_job.html",{'data':data})

def delete_job(req,jobid):
    data=jobdb.objects.filter(id=jobid)
    data.delete()
    return redirect(disp_job)

def display_applicant(req):
    data=Applicantdb.objects.all()
    return render(req,"displayapplicant.html",{'data':data})

def delete_appli(req,apid):
    data=Applicantdb.objects.filter(id=apid)
    data.delete()
    return redirect(display_applicant)




