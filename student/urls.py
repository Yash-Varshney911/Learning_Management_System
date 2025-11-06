from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard),
    path('lectures/', views.lectures),
    path('lecturecat/', views.lecturecat),
    path('enotes/', views.enotes),
    path('profile/', views.profile),
    path('software/', views.software),
    path('signout/', views.signout),
    path('task/', views.task),
    path('submit/', views.tsubmit),
    path('HandS/', views.feedback),
]

