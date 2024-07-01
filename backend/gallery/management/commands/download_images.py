# backend/gallery/management/commands/download_images.py

import requests
from time import sleep
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from gallery.models import Image

class Command(BaseCommand):
    help = 'Download images from https://thispersondoesnotexist.com and save to the database'

    def handle(self, *args, **kwargs):
        # Set up Selenium WebDriver
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        
        url = 'https://thispersondoesnotexist.com'

        for i in range(100):  # Download 100 images
            driver.get(url)
            sleep(2)  # Allow some time for the image to load
            image_element = driver.find_element(By.TAG_NAME, 'img')
            image_url = image_element.get_attribute('src')

            response = requests.get(image_url)
            if response.status_code == 200:
                image = Image()
                image.image.save(f'image_{i+1}.jpg', ContentFile(response.content), save=True)
                self.stdout.write(self.style.SUCCESS(f'Successfully downloaded image {i+1}'))
            else:
                self.stdout.write(self.style.ERROR(f'Failed to download image {i+1}. Status code: {response.status_code}'))
            sleep(1)  # To avoid being blocked

        driver.quit()
