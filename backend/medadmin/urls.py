from django.urls import path

from . import views

urlpatterns = [
    path('', views.medadmin_listcreate_view),
    path('<int:pk>/', views.medadmin_retrieveupdatedestroy_view)
]