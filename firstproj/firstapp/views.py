from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.utils.decorators import staticmethod
from rest_framework import viewsets
# Create your views here.
from django.http import HttpResponse
from .forms import ApplicationForm
from .models import *


class HomeView(TemplateView): 
    template_name = 'basedhome/testhome.html'

def index(request):
    return HttpResponse('MyIndx page')


def qryview(request):  #http://127.0.0.1:8000/getuser/?name=Vova&id=111
    name = request.GET['name'] 
    id = request.GET['id'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id))


def showform(request):
    if request.method == 'GET':
        return render(request, "form.html")
    elif request.method == 'POST':
        name = request.POST['name'] 
        id = request.POST['id'] 
        return HttpResponse(f"Name: {name} UserID: {id}")
        

 
# def showcodeform(request): 
#     if request.method == 'GET':
#        form = ApplicationForm()
#        return render(request, 'codeform.html', {'form': form})
#     elif request.method == 'POST': 
#         form = ApplicationForm(request.POST) 
#         # check whether it's valid: 
#         if form.is_valid(): 
#             name = f"Name: {request.POST['name']}"
#             address = f"Address: {request.POST['address']}"
#             numb = f"Number: {request.POST['numb']}"
#             field = f" Field: {request.POST['field']}"
#             values = [name, address, numb, field]
#             return render(request, 'codeformresp.html', {'formdata': values, 'user': request.POST['name']})      
#         else:   
#             return HttpResponse("Form submitted with invalid data")


class Showcodeform(View):   
    def get(self, request):   
        form = ApplicationForm()
        return render(request, 'codeform.html', {'form': form})
    def post(self, request):
        form = ApplicationForm(request.POST) 
        # check whether it's valid: 
        if form.is_valid(): 
            name = f"Name: {request.POST['name']}"
            address = f"Address: {request.POST['address']}"
            numb = f"Number: {request.POST['numb']}"
            field = f" Field: {request.POST['field']}"
            values = [name, address, numb, field]
            return render(request, 'codeformresp.html', {'formdata': values, 'user': request.POST['name']})      
        else:   
            return HttpResponse("Form submitted with invalid data")
        

def reghome(request):
        if request.method == 'GET':
            form = ApplicationForm()
            return render(request, 'basedhome/register.html', {'form': form})
        
def loghome(request):
        return render(request, 'basedhome/login.html')

def main(request):
        return render(request, 'maintitle.html')


class EmployeeCreate(CreateView):   
    model = Employee    
    fields = '__all__'
    template_name = 'employeetests/employeeCreate.html'
    success_url = "/myapp/view"

class EmployeeList(ListView):   
    model = Employee
    # template_name = 'employeetests/employee_data.html'  // automatically from templates by "employee_list.html"

class EmployeeDetail(DetailView):   
    model = Employee
    template_name = 'employeetests/employee_detail.html'

class EmployeeUpdate(UpdateView):   
    model = Employee   
    fields = '__all__'
    template_name = 'employeetests/employeeCreate.html'
    success_url = "/myapp/view"

from django.contrib.auth.decorators import user_passes_test 
from django.contrib.auth.decorators import permission_required 
def testpermission(user): 
    if user.is_authenticated() and user.has_perm("myapp.change_category"): 
        return True 
    else: 
        return False 

# @user_passes_test(testpermission)
# @permission_required("myapp.change_category") 
    
# def change_ctg(request):
#         # Logic for making change to category of product model instance
