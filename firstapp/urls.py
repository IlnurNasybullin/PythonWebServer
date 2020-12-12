from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('about', views.about_info, name='about_info'),
    path('list/', views.index, name="index_list"),
    path('list/new', views.save, name='new'),
    path('students', views.students, name='students'),
    path('students/edit/<int:id>', views.edit_student, name='edit_student'),
    path('students/remove/<int:id>', views.remove_student, name='remove_student')
]