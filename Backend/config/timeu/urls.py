from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.data),
    path('tasks/<int:data_id>/', views.data_list)
]
