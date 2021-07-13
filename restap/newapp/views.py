from django.shortcuts import render,HttpResponse
from newapp.models import Student,Emp,StudentData
from newapp.serializers import StudentSerializer,StudentFile,ImageSerializer,StudentDataSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

def studentinfo(request,pk):
    student=Student.objects.get(id=pk)
    studentjson=StudentSerializer(student)
    return JsonResponse(studentjson.data)


def student_list(request):
    student=Student.objects.all()
    studentjson=StudentSerializer(student,many=True)
    return JsonResponse(studentjson.data,safe=False)

def studentpost(request):
    return HttpResponse("THIS IS POST")


@api_view(['GET','POST','DELETE','PUT'])
#@authentication_classes([BasicAuthentication])
#@permission_classes([IsAuthenticated])
def student_api(request,pk=None):
    if request.method=='GET':
        if pk is not None:
            Studentdata=Student.objects.get(id=pk)
            studentdatatotal=StudentSerializer(Studentdata)
            return Response(studentdatatotal.data)
        student = Student.objects.all()
        studentjson = StudentSerializer(student, many=True)
        return Response(studentjson.data)
    if request.method=='POST':
        studentpost=StudentSerializer(data=request.data)
        if studentpost.is_valid():
            studentpost.save()
            return Response({'msg':'data created'})
        return Response(studentpost.errors)
    if request.method=='DELETE':
        deletestudent=Student.objects.get(id=pk)
        deletestudent.delete()
        return Response({'msg':'student deleted'})
    if request.method=='PUT':
        studentupdate=Student.objects.get(id=pk)
        studentupdateserialize=StudentSerializer(instance=studentupdate,data=request.data,partial=True)
        if studentupdateserialize.is_valid():
            studentupdateserialize.save()
            return Response({'msg':'you have updated successfully'})
        return Response(studentupdateserialize.errors)

@api_view(['GET','POST','DELETE','PUT'])
#@authentication_classes([BasicAuthentication])
#@permission_classes([IsAuthenticated])
def studentfile(request,pk=None):
    if request.method=='GET':
        if pk is not None:
            Studentdata=Student.objects.get(id=pk)
            studentdatatotal=StudentFile(Studentdata)
            return Response(studentdatatotal.data)
        student = Student.objects.all()
        studentjson = StudentFile(student, many=True)
        return Response(studentjson.data)

from rest_framework.parsers import JSONParser,FileUploadParser,FormParser,MultiPartParser,MultiPartParserError,DjangoMultiPartParser,FileUploadParser
@api_view(['GET','POST','DELETE','PUT'])
#@authentication_classes([BasicAuthentication])
#@permission_classes([IsAuthenticated])

def ImageFile(request,pk=None):
    if request.method=='GET':
        if pk is not None:
            Studentdata=Emp.objects.get(id=pk)
            studentdatatotal=ImageSerializer(Studentdata)
            return Response(studentdatatotal.data)
        student = Emp.objects.all()
        studentjson = ImageSerializer(student, many=True)
        return Response(studentjson.data)

    if request.method=='POST':
        data = FormParser().parse(request)
        studentpost=ImageSerializer(data=data)
        if studentpost.is_valid():
            studentpost.save()
            return Response({'msg':'data created'})
        return Response(studentpost.errors)


def image(request):
    emp=Emp.objects.get(id=1)
    pathr=emp.image
    p=emp.image.path
    return render(request,'image.html',{'image':pathr,'p':p})

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
class ImageFileClass(APIView):
    def get(self, request,**kwrgs):
            if kwrgs.get('pk'):
                pk=kwrgs.get('pk')
                Studentdata=Emp.objects.get(id=pk)
                studentdatatotal=ImageSerializer(Studentdata)
                return Response(studentdatatotal.data)
            student = Emp.objects.all()
            studentjson = ImageSerializer(student, many=True)
            return Response(studentjson.data)
    parser_classes = (FileUploadParser,MultiPartParser,FormParser)
    def post(self, request):

        serializer = ImageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

#generic api views/////////////////////////////////////////////////////////////////////////////////////////////////////

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

class Emplist(GenericAPIView,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args,**kwrgs):
        return self.list(request,*args,**kwrgs)



class EmplistRetrive(GenericAPIView, RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwrgs):
        return self.retrieve(request, *args, **kwrgs)



class Emplistcreate(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwrgs):
        return self.create(request, *args, **kwrgs)

class Emplistupdate(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self, request, *args, **kwrgs):
        return self.update(request, *args, **kwrgs)

class Emplistdelete(GenericAPIView, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def delete(self, request, *args, **kwrgs):
        return self.destroy(request, *args, **kwrgs)


#generic list api views//////////////////////////////////////
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class Listempget(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filter_backends=[SearchFilter]
    filterset_fields = ['name','age']
    search_fields=['name']



class StudentData(ListAPIView):
    queryset = StudentData.objects.all()
    serializer_class = StudentDataSerializer



class Listempcreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class Listempretrive(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class Listempupdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


#MODEL VIEW SETS


from rest_framework import viewsets

class Empviewsetmodelview(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer