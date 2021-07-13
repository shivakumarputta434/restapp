from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('studentapi',views.Empviewsetmodelview,basename='student')



urlpatterns=[

    path('',include(router.urls)),

    path('studentinfo',views.student_list,name="studentinfo"),
    path('studentinfo/<int:pk>',views.studentinfo,name="studentinfo"),
    path('studentpost',views.studentpost,name="studentpost"),



    path('student_api',views.student_api,name="student_api"),
    path('student_api/<int:pk>',views.student_api,name="student_api"),

    path('studentfile', views.studentfile, name="studentfile"),
    path('studentfile/<int:pk>', views.studentfile, name="studentfile"),

    path('ImageFile', views.ImageFile, name="ImageFile"),
    path('ImageFile/<int:pk>', views.ImageFile, name="ImageFile"),

    path('image', views.image, name="image"),

    path('ImageFileClass/', views.ImageFileClass.as_view(), name='ImageFileClass'),
    path('ImageFileClass/<int:pk>', views.ImageFileClass.as_view(), name='update'),

    path('Emplist/', views.Emplist.as_view(), name='Emplist'),
    path('EmplistRetrive/<int:pk>', views.EmplistRetrive.as_view(), name='EmplistRetrive'),
    path('Emplistcreate/', views.Emplistcreate.as_view(), name='Emplistcreate'),
    path('Emplistupdate/<int:pk>', views.Emplistupdate.as_view(), name='Emplistupdate'),
    path('Emplistdelete/<int:pk>', views.Emplistdelete.as_view(), name='Emplistdelete'),

    path('Listempget/', views.Listempget.as_view(), name='Listempget'),
    path('Listempcreate/', views.Listempcreate.as_view(), name='Listempcreate'),
    path('Listempretrive/<int:pk>', views.Listempretrive.as_view(), name='Listempretrive'),
    path('Listempupdate/<int:pk>', views.Listempupdate.as_view(), name='Listempupdate'),


    path('StudentData/', views.StudentData.as_view(), name='StudentData'),


]