from django.urls import path
from .views import home, Details, CheckoutSessionView, CancelView, SuccessView

urlpatterns = [
    path('',home.as_view(),name= 'home'),
    path('create-checkout-session/', CheckoutSessionView.as_view(), name='create-checkout-session'),
    path('product-detail/<int:pk>',Details.as_view(),name= 'product-detail'),

    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
]

