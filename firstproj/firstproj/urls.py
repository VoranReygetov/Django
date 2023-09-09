"""
URL configuration for firstproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path 
from firstapp.views import * 
from firstapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', include('firstapp.urls')),
    path('', HomeView.as_view(), name = 'home'),
    path('getuser/', views.qryview, name='qryview'),
    path("myapp/", include('firstapp.urls')),
]
