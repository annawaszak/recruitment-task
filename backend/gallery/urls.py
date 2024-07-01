from django.urls import path
from .views import image_preview

urlpatterns = [
    path('preview/<int:index>/', image_preview, name='image_preview'),
]
