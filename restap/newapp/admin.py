from django.contrib import admin
from newapp.models import Emp,StudentData,Student

# Register your models here.
@admin.register(Student)
class ModelViewStudent(admin.ModelAdmin):
    list_display = ['id','name','age']


admin.site.register(Emp)
admin.site.register(StudentData)

