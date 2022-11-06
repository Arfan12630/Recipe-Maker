from bs4 import BeautifulSoup
import requests

url = "https://www.simplyrecipes.com/indian_chicken_biryani/"
page = requests.get(url).text
document = BeautifulSoup(page,"html.parser")
print(document.prettify())