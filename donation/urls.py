from django.urls import path
from .views import PaymentView, donationView, donationFrameView

urlpatterns = [
    path('payment/', PaymentView.as_view(), name='payment'),
    path('donate/', donationFrameView.as_view(), name='donation-frame'),
    path('', donationView.as_view(), name='donation-home'),
    
    # path('payment/<payment_option>/', PaymentView.as_view(), name='payment'), TODO: for other payments gateways
]