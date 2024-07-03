===================================
On https://thispersondoesnotexist.com/, you can see AI-generated human faces. Your task is to create a service to manage these images.

Backend (Django)

Create an API that provides the following endpoints:

/human/{id}
Returns a full-size image for a given ID (the same image for the same ID every time).

/gallery/preview/{index}
Returns a preview (200x200) image for a given index.

/gallery/{index}
Allows the user to set the image displayed at a given index in the gallery. Accepts {"type": "human", "id": 40}.

Frontend (React + TypeScript)

Create a frontend that displays the image gallery. Add pagination and display 20 images per page. Use the preview images (200x200) in the gallery and show a full-size image in a modal when the user clicks on an image. Allow the user to change the ID of each image in the gallery using the PUT endpoint.

Bonus:
Dockerize the application in a simple way so it can be easily run using Docker.
===================================

Commands"
- To initially download 100 images: "python manage.py download_images" or alternatively using docker: "docker-compose exec backend python manage.py download_images"

Limitations: 
- Currently downloading only 100 images. I would improve that to initiate a download of additional 20 each time the user goes to the next page.


