from django.urls import path
from . import views

urlpatterns = [
    path('', views.data),
    path('<int:data_id>', views.data_list)
]
