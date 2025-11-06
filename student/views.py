from django.shortcuts import render, redirect
from Main.models import *
from django.http import HttpResponse
from django.views.decorators.cache import cache_control
# Create your views here.


@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def signout(request):
    user = request.session.get("email")
    if user : 
        del request.session["name"]
        del request.session["userpic"]
        del request.session["email"]
        return redirect("/index/")
    return render(request, "register.html")


@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def lecturecat(request):
    bid = request.session.get("batch")
    cat = category.objects.all().filter(batch_name = bid)
    d = {"categories" : cat}
    return render(request, "student/lecturecat.html", d)


@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def enotes(request):
    bid = request.session.get("batch")
    data = notes.objects.all().filter(batch = bid)
    d = {"notes" : data}
    return render(request, "student/enotes.html", d)


@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def lectures(request):
    x = request.GET.get("cid")
    if x:
        data = mylecture.objects.all().filter(category = x)
    else:
        data = mylecture.objects.all().order_by("-id")
        # data = mylecture.objects.all()
    d = {"vdo" : data}
    return render(request, "student/lectures.html", d)


@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def profile(request):
    user = request.session.get("email")
    data = tblregister.objects.all().filter(email = user)
    d = {"userinfo" : data}
    return render(request, "student/profile.html", d)


@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def software(request):
    data = softwarekit.objects.all()
    d = {"so" : data}
    return render(request, "student/software.html", d)


@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def task(request):
    bid = request.session.get("batch")
    data = mytask.objects.all().filter(batch = bid)
    d = {"da" : data}
    return render(request, "student/task.html", d)


@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def tsubmit(request):
    userid = request.session.get("email")
    if (request.method == "POST"):
        title = request.POST.get("title")
        tid = request.POST.get("tid")
        taskfile = request.FILES["fu"]
        x = submittedtask.objects.all().filter(userid = userid, tid = tid).count()
        if (x == 1):
            return HttpResponse("<script>alert('This task is already submitted.');location.href = '/student/task/'</script>")
        else:
            submittedtask(title = title, tid = tid, upload_task = taskfile, userid = userid).save()
            return HttpResponse("<script>alert('This task is submitted.');location.href = '/student/task/';</script>")
    return render(request, "student/task.html")


@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def feedback(request):
    if(request.method == "POST"):
        Name = request.POST.get('name')
        Mobile = request.POST.get('mob')
        Message = request.POST.get('msg')
        tblfeed(name = Name, mobile = Mobile, message = Message).save()
        return HttpResponse("<script> alert('Thanks For Your Feedback'); location.href = '/feed/' </script>")
    return render(request, "student/HandS.html")


@cache_control(no_store = True,no_cache = True,must_revalidate = True)
def dashboard(request):
    return render(request, "student/dashboard.html")
