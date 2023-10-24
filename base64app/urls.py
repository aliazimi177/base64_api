from django.urls import path
from .views import base64_encode_decode

urlpatterns = [
    path('base64/', base64_encode_decode, name='base64'),
]