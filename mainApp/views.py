from django.shortcuts import render,HttpResponseRedirect
from .models import Employee
from django.db.models import Q

def homePage(Request):
    data=Employee.objects.all()
    return render(Request,"index.html",{"data":data})

def addPage(Request):
    try:
        if(Request.method=="POST"):
            e=Employee()
            e.name=Request.POST.get("name")
            e.email=Request.POST.get("email")
            e.phone=Request.POST.get("phone")
            e.dsg=Request.POST.get("dsg")
            e.salary=Request.POST.get("salary")
            e.city=Request.POST.get("city")
            e.state=Request.POST.get("state")
            e.save()
            return HttpResponseRedirect("/")
    except:
        pass
    return render(Request,"add.html")

def deleteEmp(Request,id):
    try:
        data=Employee.objects.get(id=id)
        data.delete()
    except:
        pass
    return HttpResponseRedirect("/")

def updateEmp(Request,id):
    try:
        data=Employee.objects.get(id=id)
        if(Request.method=="POST"):
            data.name = Request.POST.get("name")
            data.email = Request.POST.get("email")
            data.phone = Request.POST.get("phone")
            data.dsg = Request.POST.get("dsg")
            data.salary = Request.POST.get("salary")
            data.city = Request.POST.get("city")
            data.state = Request.POST.get("state")
            data.save()
            return HttpResponseRedirect("/")
        return render(Request,"update.html",{"data":data})
    except:
        pass
    return HttpResponseRedirect("/")

def searchPage(Request):
    if(Request.method=="POST"):
        search = Request.POST.get("search")
        data = Employee.objects.filter(Q(name__icontains=search)|Q
                                       (city__icontains=search)|Q
                                       (state__icontains=search)|Q
                                       (dsg__icontains=search))
        return render(Request,"index.html",{"data":data})
    else:
        return HttpResponseRedirect("/")