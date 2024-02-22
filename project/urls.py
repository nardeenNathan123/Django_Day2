"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.db import router
from django.urls import include, path
from myapi.views import EmployeesFunBaseView, EmployeesFunBaseView2
from student.views import create, delete_student, home, student,signup,signin
from student.views import contact
from student.views import about
from student.views import updatee ,signout


from company.views import EmployeeClassView, EmployeeView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name="home"),
    path('contact/',contact,name="contact"),
    path('about/',about,name="about"),
    path('student/',student,name="student"),
    path('delete_student/<int:id>',delete_student,name="delete_student"),
    path('signup/',signup,name="signup"),
    path('login/',signin,name="login"),
    path('create/',create,name="create"),
    path('updatee/<int:id>',updatee,name="updatee"),
    path('signout/',signout,name="signout"),



    path('employee/',EmployeeView,name="employee"),
    # path('team/',EmployeeView2,name="team"),
    path('team/',EmployeeClassView.as_view(),name="employee"),
     path('employees-all/',EmployeesFunBaseView,name="employees-all"),
    path('employees-all-2/',EmployeesFunBaseView2.as_view(),name="employees-all-2"),
    path('employees-all-3/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))







]
