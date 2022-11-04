from django.urls import path 
from .import views
urlpatterns=[ 
    path('', views.View.as_view()), 
    path('operation/', views.OperationView.as_view()) 
]
