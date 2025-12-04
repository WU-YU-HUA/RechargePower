from django.urls import path
from . import views

urlpatterns = [
    path('', views.GiftViewSet.as_view({
        'post': 'create',
        'get': 'list'
    })),
    path('<int:pk>/', views.GiftViewSet.as_view({
        'get': 'retrieve',
        'patch': 'update',
        'delete': 'destroy'
    })),
    path('exchange/', views.exchange)
]