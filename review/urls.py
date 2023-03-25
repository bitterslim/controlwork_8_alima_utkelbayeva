from django.urls import path

from review.views.review_view import ReviewCreateView, ReviewUpdateView, ReviewDeleteView
from review.views.base import IndexView
from review.views.products_view import ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("product/<int:pk>", ProductDetailView.as_view(), name='product_detail'),
    path("product/add/", ProductCreateView.as_view(), name='product_add'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path("product/<int:pk>/review/add/", ReviewCreateView.as_view(), name="review_add"),
    path("product/<int:pk>/review/update/", ReviewUpdateView.as_view(), name="review_update"),
    path("product/<int:pk>/review/delete/", ReviewDeleteView.as_view(), name="review_delete"),
]
