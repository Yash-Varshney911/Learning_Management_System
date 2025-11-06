from django.contrib import admin
from .models import *

# Register your models here.



class tblcontactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "mobile", "email", "message")

admin.site.register(tblcontact, tblcontactAdmin)



class tblgalAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "picture")

admin.site.register(tblgal, tblgalAdmin)



class tblteamAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "picture", "post", "exp")

admin.site.register(tblteam, tblteamAdmin)



class tblfeedAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "mobile", "message")

admin.site.register(tblfeed, tblfeedAdmin)



class tblregisterAdmin(admin.ModelAdmin):
    list_display = ("name", "lname", "email", "mobile", "Whatmobile", "password", "picture", "batch", "address", "regdate")

admin.site.register(tblregister, tblregisterAdmin)



class batchAdmin(admin.ModelAdmin):
    list_display = ("id", "batchname")

admin.site.register(batch, batchAdmin)



class categoryAdmin(admin.ModelAdmin):
    list_display = ("id", "picture","title", "batch_name")

admin.site.register(category, categoryAdmin)



class softwarekitAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "software_info", "thumbnail", "download_link", "posted_date")

admin.site.register(softwarekit, softwarekitAdmin)



class mylectureAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "video_info", "vlink", "batch", "category", "posted_date")

admin.site.register(mylecture, mylectureAdmin)



class notesAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "notes_info", "notesfile", "batch", "posted_date")

admin.site.register(notes, notesAdmin)




class mytaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "task_info", "batch", "taskfile", "posted_date")

admin.site.register(mytask, mytaskAdmin)



class submittedtaskAdmin(admin.ModelAdmin):
    list_display = ("id", "userid", "tid", "title", "upload_task", "marks")

admin.site.register(submittedtask, submittedtaskAdmin)



