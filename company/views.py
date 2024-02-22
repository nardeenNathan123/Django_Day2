from django.http import HttpResponse
from django.shortcuts import render
from company.forms import EmployeeForm,EmployeeForm2
from django.views import View

from company.models import Employee, Team

# Create your views here.
def EmployeeView(request):
   
    if request.method=='GET':
        myform=EmployeeForm()
        return render(request,'company/create_emp.html',{'form':myform})
    if request.method=='POST':
        myform=EmployeeForm(request.POST)
        if myform.is_valid():
            team=Team.objects.filter(pk=request.POST["team"])[0]
            Employee.objects.create(name=request.POST['name'],salary=request.POST['salary'],title=request.POST['title'],team=team)
        return render(request,'company/create_emp.html',{'form':myform})

    #return HttpResponse('hi')


# def EmployeeView2(request):
#     if request.method=='GET':
#         myform=EmployeeForm2()
#         return render(request,'company/create_team.html',{'form':myform})
#     if request.method=='POST':
#         myform=EmployeeForm2(request.POST)
#         if myform.is_valid():
#             myform.save()
#         return render(request,'company/create_team.html',{'form':myform})

#     return HttpResponse('hi')


class EmployeeClassView(View):
    def get(self,request):
        myform=EmployeeForm2()
        return render(request,'company/create_team.html',{'form':myform})
    def post(self,request):
         myform=EmployeeForm2(request.POST)
         if myform.is_valid():
             myform.save()
         return render(request,'company/create_team.html',{'form':myform})





    
