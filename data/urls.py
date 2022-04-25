from . import views
from django.urls import path,re_path

urlpatterns=[
    path('',views.home,name ='home'),
    path('student/<int:student_id>/',views.student,name='student'),
    path('create_student',views.create_student,name='create_student'),
    path('update_student/<student_id>',views.update_student,name='update_student'),
    path('delete_student/<student_id>',views.delete_student,name='delete_student'),
]