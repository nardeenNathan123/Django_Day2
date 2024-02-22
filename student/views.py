from django.shortcuts import render
from django.http import HttpResponse 
from django.http import JsonResponse
from django.shortcuts import redirect
from student.models import Student,User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

import json 
# Create your views here.
def home(request):
    return render(request,'student/home.html')
def contact(request):
    return render(request,'student/contact.html')
def about(request):
    return render(request,'student/about.html')


# def student(request):
    # students=Student.objects.all()
    # all=[]
    # for student in students:
    #     all.append({"id":student.id,
    #                 "name":student.l_name,
    #                 "age":student.age})
    
    #return JsonResponse(json.dumps(all),safe=True)

    #students=Student.objects.get(id=1)
    #students=Student.objects.filter(id=1).delete()

    #add student to students
    # mystudent=Student()
    # mystudent.id=6
    # mystudent.f_name="mohsn"
    # mystudent.l_name="ali"
    # mystudent.age=45
    # mystudent.save()
    #anther way
    # Student.objects.create(id=5,f_name="omr",l_name="ahmed",age=8)

    # return  HttpResponse('hi')

def student(request):
    if request.session.get('name'):
    # if request.session.name:    
        students=Student.objects.all()
        context={}
        context['students']=students
        return render(request,'student/home.html',context)
    else:
        return redirect ('signin')

def delete_student(request,id):
    Student.objects.get(id=id).delete()
    return redirect('student')

def signup(request):
    if request.method=='GET':
        return render(request,'student/signup.html')

    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['psw']
        name=request.POST['name']
       # print(email,password,name)
        val=User.objects.filter(email=email)
        if val:
            context = {
                    'error_message': "Invalid email pleas try again"
                }
            return render(request,'student/signup.html',context)
            
        User.objects.create_user(username=name,password=password,email=email)
   
        #User.objects.create(email=email,password=password,name=name)

        return redirect('student')
    
def signin(request) :
    if request.method == 'GET':
        
        return render(request,'student/login.html')
    
    if request.method == 'POST':
        name=request.POST['name']
        password=request.POST['psw']
        
       # myuser=User.objects.filter(email=email,password=password)
        
        # if myuser:
        #     return redirect("student")
        # else:
        #     context={'error_message':'Incorrect email or password'}
        #     return render(request,'student/login.html' ,context)
        auth=authenticate(username=name,password=password)
        if auth:
            login(request,auth)
            request.session['name']=name
            return redirect('student')
        else:
             context={'error_message':'Incorrect email or password'}
             return render(request,'student/login.html' ,context)
        
        #return render(request,'student/login.html')  
        

        

def signout(request):
    request.session.clear()
    logout(request)
    return redirect('login')         
        

def create(request) :
    if request.method=='GET':
        return render(request,'student/create_student.html')

    if request.method=='POST':
        f_name=request.POST['fname']
        l_name=request.POST['lname']
        age=request.POST['age']
        
           
        Student.objects.create(f_name=f_name,l_name=l_name,age=age)

        return redirect('student')

def updatee(request,id) :
    student=Student.objects.get(id=id)
    context={}
    context['students']=student 
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        age = request.POST['age']
        
        
        student.f_name = fname
        student.l_name = lname
        student.age = age
        student.save()
        return redirect('student')
    # print(student.f_name)
    return render(request,'student/updatee.html',context)





# def dataUpdate(request):
#     if request.method=='GET':
#         return render(request,'student/updatee.html')
#     if request.method=='POST':
#         f_name=request.POST['fname']
#         l_name=request.POST['lname']
#         age=request.POST['age']
#         Student.objects.update(f_name=f_name,l_name=l_name,age=age)
#         return redirect('student')



   

        
