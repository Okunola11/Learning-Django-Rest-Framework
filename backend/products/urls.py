from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductListCreateApiView.as_view(), name='product-list'),
    path('<int:pk>/', views.product_detail_view, name='product-detail'),
    path('update/<int:pk>/', views.product_update_view, name='product-edit'),
    path('delete/<int:pk>/', views.product_destroy_view),
]
