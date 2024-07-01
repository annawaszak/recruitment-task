from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Image
from PIL import Image as PILImage
import io

def image_preview(request, index):
    image_instance = get_object_or_404(Image, id=index)
    image = PILImage.open(image_instance.image.path)
    image = image.resize((200, 200))
    response = HttpResponse(content_type="image/jpeg")
    image.save(response, "JPEG")
    return response
    