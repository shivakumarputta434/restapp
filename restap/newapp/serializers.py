from rest_framework import serializers
from newapp.models import Student,Emp,StudentData

class StudentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model= StudentData
        fields=['id','section','StudentInfo']

class StudentSerializer(serializers.ModelSerializer):
    StudentInfo=StudentDataSerializer(many=True,read_only=True)
    class Meta:
        model = Student
        fields = ['id','name','age','StudentInfo']


    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.age=validated_data.get('age',instance.age)
        instance.save()
        return instance








class StudentFile(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Emp
        fields = ('id','name','image')

    def create(self, validated_data):
        return Emp.objects.create(**validated_data)




