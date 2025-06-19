from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_tenant, name='add_tenant'),
    path('', views.tenant_list, name='tenant_list'),
]
