from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Image
from django.views.decorators.csrf import csrf_exempt
import json
from PIL import Image as PILImage
import io

def image_preview(request, index):
    image_instance = get_object_or_404(Image, id=index)
    image = PILImage.open(image_instance.image.path)
    image = image.resize((200, 200))
    response = HttpResponse(content_type="image/jpeg")
    image.save(response, "JPEG")
    return response

def human_image(request, id):
    image_instance = get_object_or_404(Image, id=id)
    with open(image_instance.image.path, 'rb') as f:
        return HttpResponse(f.read(), content_type='image/jpeg')

@csrf_exempt
def set_gallery_image(request, index):

    if request.method == 'PUT':
        data = json.loads(request.body)
        image_id = data.get('id')
        image_type = data.get('type')
        if image_type != 'human':
            return JsonResponse({'error': 'Invalid type'}, status=400)
        image_instance = get_object_or_404(Image, id=image_id)
        response_data = {
            'index': index,
            'image_id': image_instance.id,
            'image_url': image_instance.image.url,
        }
        return JsonResponse(response_data, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=400)
