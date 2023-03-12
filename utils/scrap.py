from bs4 import BeautifulSoup
import requests

def scrapImages(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")
  return soup.find_all("img")