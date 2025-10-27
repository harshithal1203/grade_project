from django.urls import path
from . import views

urlpatterns=[
    path('',views.grade_distribution, name='grade_distribution'),

]