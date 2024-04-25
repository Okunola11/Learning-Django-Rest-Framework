from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductListCreateApiView.as_view()),
    path('<int:pk>/', views.product_detail_view),
    path('update/<int:pk>/', views.product_update_view),
    path('delete/<int:pk>/', views.product_destroy_view),
]
