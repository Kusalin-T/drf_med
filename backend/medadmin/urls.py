from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.medadmin_detail_view)
]