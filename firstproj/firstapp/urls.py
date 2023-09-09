from django.urls import path

from . import views
from firstapp.views import * 
app_name = 'firstapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('', HomeView.as_view(), name='home'),
    path("showform/", views.showform, name="showform"), 
    path("showcodeform/", Showcodeform.as_view(), name="showcodeform"),
    path('reg/', views.reghome, name='reg'),
    path('log/', views.loghome, name='log'),
    path('main/', views.main, name='main'),
    path('create/', EmployeeCreate.as_view(), name = 'EmployeeCreate'),
    path('view/', EmployeeList.as_view(), name = 'EmployeeRead'),
    path('show/<int:pk>', EmployeeDetail.as_view(), name = 'EmployeeDetail'),
    path('update/<int:pk>', EmployeeUpdate.as_view(), name = 'EmployeeUpdate'),  
]