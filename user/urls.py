from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserViewSet.as_view({
        'post': 'create',
    })),
    path('<int:pk>/', views.UserViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy',
    })),
    path('login/', views.login),
    path('deposite/', views.deposite)
]