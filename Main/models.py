from django.db import models

# Create your models here.


class batch(models.Model):
    batchname = models.CharField(max_length=40, null=True)
    def __str__(self):  #this function is defined to show the batchname except batchobject1 or batchobject2
        return self.batchname
    
class category(models.Model):
    title = models.CharField(max_length=50, null=True)
    picture = models.ImageField(upload_to="static/category/", null=True, blank=True)
    batch_name = models.ForeignKey(batch, on_delete=models.CASCADE)
    def __str__(self):  #this function is defined to show the batchname except batchobject1 or batchobject2
        return self.title

class tblcontact(models.Model):
    name = models.CharField(max_length=20, null=True)
    mobile = models.CharField(max_length=15, null=True)
    email = models.EmailField(max_length=40, null=True)
    message = models.TextField(null=True)

class tblgal(models.Model):
    title = models.CharField(max_length=30)
    picture = models.ImageField(upload_to="static/modelgallery/", null=True)

class tblteam(models.Model):
    name = models.CharField(max_length=30)
    picture = models.ImageField(upload_to="static/modelteam/")
    post = models.CharField(max_length=30)
    exp = models.CharField(max_length=30)

class tblfeed(models.Model):
    name = models.CharField(max_length=20, null=True)
    mobile = models.CharField(max_length=15, null=True)
    message = models.TextField(null=True)

class tblregister(models.Model):
    name = models.CharField(max_length=15, null=True)
    lname = models.CharField(max_length=15, null=True)
    email = models.EmailField(primary_key=True, max_length=50)
    mobile = models.IntegerField(null=True)
    Whatmobile = models.IntegerField(null=True)
    password = models.CharField(max_length=20, null=True)
    picture = models.ImageField(upload_to="static/registerpic/", null=True, blank=True)
    batch = models.ForeignKey(batch, on_delete=models.CASCADE, null=True)
    address = models.TextField(null=True)
    regdate = models.DateTimeField(null=True)

class softwarekit(models.Model):
    title = models.CharField(max_length=100, null=True)
    software_info = models.TextField(null=True)
    thumbnail = models.ImageField(upload_to="static/softwarethum/", null=True, blank=True)
    download_link = models.CharField(max_length=500, null=True)
    posted_date = models.DateTimeField(null=True)

class mylecture(models.Model):
    title = models.CharField(max_length=200, null=True)
    video_info = models.TextField(null=True)
    vlink = models.CharField(max_length=300, null=True)
    batch = models.ForeignKey(batch, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(null=True)

class notes(models.Model):
    title = models.CharField(max_length=200, null=True)
    notes_info = models.TextField(null=True)
    batch = models.ForeignKey(batch, on_delete=models.CASCADE, null=True)
    notesfile = models.FileField(upload_to="static/notes/", null=True, blank=True)
    posted_date = models.DateTimeField(null=True)

class mytask(models.Model):
    title = models.CharField(max_length=200, null=True)
    task_info = models.TextField(null=True)
    batch = models.ForeignKey(batch, on_delete=models.CASCADE, null=True)
    taskfile = models.FileField(upload_to="static/task/", null=True, blank=True)
    posted_date = models.DateTimeField(null=True)

class submittedtask(models.Model):
    userid = models.CharField(max_length=50, null=True)
    tid = models.IntegerField(null=True)
    title = models.CharField(max_length=50, null=True)
    marks = models.IntegerField(null=True)
    upload_task = models.FileField(upload_to="static/submittedtasks", null=True, blank=True)

