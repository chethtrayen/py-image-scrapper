from utils.scrap import scrapImages
from utils.image import getImageSources

# Update to site to scrap
URL = "https://kirbyscomicartshop.com/collections/jon-lam"
images = scrapImages(URL)
sources = getImageSources(images)
print(sources)