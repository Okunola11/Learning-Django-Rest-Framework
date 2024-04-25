from django.urls import path

from . import views

urlpatterns = [
    path('', views.product_mixin_view),
    path('<int:pk>/', views.product_mixin_view),
    path('update/<int:pk>/', views.product_update_view),
    path('delete/<int:pk>/', views.product_destroy_view),
]
