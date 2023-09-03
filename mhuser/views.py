from django.shortcuts import render,redirect
from django.contrib import messages
from mhuser.models import contactdb,Applicantdb,newsletterdb
from mhadmin.models import servicedb,designdb,projectdb,jobdb
from django.http import JsonResponse




# Create your views here.

def homepage(req):
    data=projectdb.objects.all()
    serv=servicedb.objects.all()

    return render(req,"Home.html",{'data':data,'serv':serv,})
def contact(req):
    serv=servicedb.objects.all()

    return render(req,"contact.html",{'serv':serv})
def savecontact(req):
    if req.method=="POST":
        na=req.POST.get('name')
        em=req.POST.get('email')
        sub=req.POST.get('subject')
        msg=req.POST.get('message')
        obj1=contactdb(Name=na,Email_Id=em,Subject=sub,Message=msg)
        obj1.save()
        return redirect(contact)

def about(req):
    serv=servicedb.objects.all()

    return render(req,"About.html",{'serv':serv})

def servicepg(req):
    data=servicedb.objects.all()
    return render(req,"services.html",{'data':data})

def singleservicepg(req,servname):
    name =servicedb.objects.all()
    servsingle=designdb.objects.filter(Service=servname)
    serv=servicedb.objects.filter(service_name=servname)
    return render(req,"singleservice.html",{'servsingle':servsingle,'name':name,'serv':serv})


def projectpg(req):
    serv=servicedb.objects.all()

    data=projectdb.objects.all()
    return render(req,"project.html",{'data':data,'serv':serv})

def singlepropg(req,proname):
    serv=servicedb.objects.all()

    data=projectdb.objects.filter(Project_name=proname)
    return render(req,"singleproject.html",{'data':data,'serv':serv})





def search_view(request):
    if request.method=="GET":
        query=request.GET.get('query')

        serv=servicedb.objects.filter(service_name__icontains=query)
        proj=projectdb.objects.filter(Project_name__icontains=query)


        return render(request,"search_results.html",{'serv':serv,'proj':proj})



def news_pg(req):
    serv=servicedb.objects.all()

    return render(req, "news.html",{'serv':serv})


def pricing_pg(req):
    serv=servicedb.objects.all()

    return render(req,"pricing.html",{'serv':serv})



def estimate_pg(req):
    serv=servicedb.objects.all()

    return render(req,"estimation.html",{'serv':serv})

def career_pg(req):
    serv=servicedb.objects.all()

    return render(req,"careers.html",{'serv':serv})

def applicant_pg(req):
    if req.method=="POST":
        fname=req.POST.get('fname')
        lname=req.POST.get('lname')
        em=req.POST.get('email')
        mob=req.POST.get('mobile')
        pos=req.POST.get('position')
        res=req.POST.get('resume')
        obj=Applicantdb(Firstname=fname,Lastname=lname,Email=em,Mobile=mob,Position=pos,Resume=res)
        obj.save()
        messages.success(req,"APPLICATION SEND SUCCESSFULLY")

        return redirect(career_pg)


def jobopeening(req):
    serv=servicedb.objects.all()

    data=jobdb.objects.all()
    return render(req,"job_pg.html",{'data':data,'serv':serv})




def addnwsletr(req):
    if req.method=="POST":
        em=req.POST.get('email')
        obj=newsletterdb(email=em)
        obj.save()
        return render(req,"Home.html")



