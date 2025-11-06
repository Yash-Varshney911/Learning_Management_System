from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def index(request):
    if(request.method == "POST"):
        Name = request.POST.get('name')
        Mobile = request.POST.get('mob')
        Email = request.POST.get('email')
        Message = request.POST.get('msg')
        tblcontact(name = Name, mobile = Mobile, email = Email, message = Message).save()
        return HttpResponse("<script> alert('Data saved successfully'); location.href = '/index/' </script>")
    return render(request, "index.html")

def gallery(request):
    data = tblgal.objects.all()
    d = {"gal" : data}
    return render(request, "gallery.html", d)

def team(request):
    data = tblteam.objects.all()
    d = {"team" : data}
    return render(request, "team.html", d)

def register(request):
    if(request.method == "POST"):
        Name = request.POST.get('name')
        Lname = request.POST.get('lname')
        Email = request.POST.get('email')
        Mobile = request.POST.get('mob')
        Whmobile = request.POST.get('wmob')
        Password = request.POST.get('passwd')
        Picture = request.FILES['fu']
        Address = request.POST.get('address')
        tblregister(name = Name, lname = Lname, email = Email, mobile = Mobile, Whatmobile = Whmobile, password = Password, picture = Picture, address = Address, regdate = datetime.now()).save()
        return HttpResponse("<script> alert('Your Registration is confirmed.'); location.href = '/register/' </script>")
    return render(request, "register.html")

def login(request):
    if(request.method == "POST"):
        Email = request.POST.get("email")
        Password = request.POST.get("passwd")
        x = tblregister.objects.all().filter(email = Email, password = Password)
        # if condition is either true than the value of x is 1 because of count function or 0
        if(x.count() == 1):
            # Session Creation
            request.session["name"] = str(x[0].name)
            request.session["lname"] = str(x[0].lname)
            request.session["userpic"] = str(x[0].picture)
            b = x[0].batch
            if b:
                request.session["batch"] = str(x[0].batch.id)
            request.session["email"] = Email
            return HttpResponse("<script> alert('You are successfully logged in. Press OK to get redirected'); location.href = '/student/dashboard/'</script>")
        else:
            return HttpResponse("<script> alert('Your email or password is incorrect'); location.href = '/login/'</script>")
    return render(request, "login.html")

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def service(request):
    return render(request, "service.html")

