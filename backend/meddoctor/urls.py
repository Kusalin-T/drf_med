from django.urls import path

from . import views

urlpatterns = [
    path('', views.meddoctor_listcreate_view),
    path('<int:pk>/', views.meddoctor_retrieveupdatedestroy_view)
]