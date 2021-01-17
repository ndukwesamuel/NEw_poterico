from django.urls import path
from .views import (
    HomeView,
    ProductDetail,
    add_to_cart,
    remove_from_cart,
    test,
    OrderSummaryView,
    remove_single_from_cart,
    CheckoutView,
    

)


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('order-summary/', OrderSummaryView.as_view(), name='order_summary'),

    path('product/<slug>/', ProductDetail.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add_to_cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('test/', test, name='test'),
    path('remove_from_cart/<slug>/', remove_from_cart, name='remove_from_cart'),
    path('remove_single_from_cart/<slug>/', remove_single_from_cart, name='remove_single_from_cart'),

]
