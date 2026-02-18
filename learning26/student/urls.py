from django.urls import path
from . import views

urlpatterns = [
   path("home/",views.studentHome),
   path("dashboard/",views.studentDashboard),
   path("serviceList/",views.serviceList,name="serviceList"),
   path("createService/",views.createService,name="createService"),
]
