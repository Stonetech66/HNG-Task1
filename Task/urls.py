from django.urls import path 
from .import views
urlpatterns=[ 
    path('task1/', views.View.as_view())
]