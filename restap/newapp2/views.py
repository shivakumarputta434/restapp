from django.shortcuts import render,HttpResponse
from .models import Emptable,Product,Color,Category,Company,Area,Houses
from django.db.models import Avg,Max ,Aggregate,Min
from datetime import datetime



# Create your views here.
def home(request):
    return render(request,'newapp2/home.html')

def search(request):
    name1=request.GET['q']
    data=Product.objects.filter(name__icontains=name1).order_by("id")
    return render(request, 'newapp2/search.html',{'data':data})


def app(request):
    color=Color.objects.get(id=2)
    qs=color.product_color.all()
    date=Company.objects.get(id=2)

    h = Houses.objects.get(id=2)
    hs=h.housecolor
    print(hs)

    product=Product.objects.filter(name="mirror").update(price=3000)


    return render(request,'newapp2/app.html',{'qs': qs})

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render,get_object_or_404,HttpResponse
from .serializer import Company_Serializer
from rest_framework import status
from datetime import datetime



class Company_Profile(APIView):
    def get(self,request,**kwargs):
        if kwargs.get('pk'):
            pk=kwargs.get('pk')
            company=get_object_or_404(Company.objects.all(),pk=pk)
            com_ser=Company_Serializer(company)
            return Response({'company':com_ser.data})
        else:
            company = Company.objects.all()
            com_ser=Company_Serializer(company,many=True)
            return Response({'company':com_ser.data})
    def post(self,request):
        serializer = Company_Serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




