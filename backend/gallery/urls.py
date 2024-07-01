from django.urls import path
from .views import image_preview, human_image, set_gallery_image

urlpatterns = [
    path('preview/<int:index>/', image_preview, name='image_preview'),
    path('human/<int:id>/', human_image, name='human_image'),
    path('set_gallery_image/<int:index>/', set_gallery_image, name='set_gallery_image'),
]
