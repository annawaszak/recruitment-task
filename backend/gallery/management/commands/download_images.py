import asyncio
import aiohttp
from time import sleep
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from asgiref.sync import sync_to_async
from gallery.models import Image

class Command(BaseCommand):
    help = 'Download images from https://thispersondoesnotexist.com and save to the database'

    def handle(self, *args, **kwargs):
        asyncio.run(self.download_images())

    async def fetch_image(self, session, url, image_id):
        async with session.get(url) as response:
            if response.status == 200:
                content = await response.read()
                await self.save_image(content, image_id)
                self.stdout.write(self.style.SUCCESS(f'Successfully downloaded image {image_id}'))
            else:
                self.stdout.write(self.style.ERROR(f'Failed to download image {image_id}. Status code: {response.status}'))

    async def save_image(self, content, image_id):
        await sync_to_async(self._save_image)(content, image_id)

    def _save_image(self, content, image_id):
        image = Image()
        image.image.save(f'image_{image_id}.jpg', ContentFile(content), save=True)

    async def download_images(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        
        url = 'https://thispersondoesnotexist.com'

        async with aiohttp.ClientSession() as session:
            tasks = []
            for i in range(100):  # Download 100 images
                driver.get(url)
                sleep(2)  # To allow some time for the image to load
                image_element = driver.find_element(By.TAG_NAME, 'img')
                image_url = image_element.get_attribute('src')
                task = asyncio.ensure_future(self.fetch_image(session, image_url, i + 1))
                tasks.append(task)
                sleep(1)  # To avoid being blocked

            await asyncio.gather(*tasks)

        driver.quit()
