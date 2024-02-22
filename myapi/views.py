from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from company.models import Employee
from myapi.serializers import EmployeeSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(["GET", "POST"])
def EmployeesFunBaseView(request):
    
    if request.method == 'GET':
        employees=Employee.objects.all()
        seralizer=EmployeeSerializer(employees,many=True)
        return Response(seralizer.data)
    
    if request.method == 'POST':
        data=request.data
        seralizer=EmployeeSerializer(data=data)
        if seralizer.is_valid():
            seralizer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "POST"])
class EmployeesFunBaseView2(APIView):
    
    def get(self,request):
        employees=Employee.objects.all()
        seralizer=EmployeeSerializer(employees,many=True)
        return Response(seralizer.data)
    
    def post(self,request):
        data=request.data
        seralizer=EmployeeSerializer(data=data)
        if seralizer.is_valid():
            seralizer.save()
            employees=Employee.objects.all()
            all_data=EmployeeSerializer(seralizer.data)
            return Response({"emplyees":all_data.data},status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
        
class EmployeesFunBaseView3(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()