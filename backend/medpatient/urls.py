from django.urls import path

from . import views

urlpatterns = [
    path('', views.medpatient_listcreate_view),
    path('<int:pk>/', views.medpatient_retrieveupdatedestroy_view),
    path('<int:pk>/detail', views.medpatient_retrieve_view),
]