from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ProductListView.as_view(), name='product_list' ),
    path('create/', views.ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/detail/', views.ProductDetailView.as_view(), name='product_detail'),
    path('<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
]