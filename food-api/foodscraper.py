from bs4 import BeautifulSoup
import requests

url = "https://www.simplyrecipes.com/recipes/indian_chicken_biryani/"
page = requests.get(url).text
document = BeautifulSoup(page,"html.parser")
recipe = {}
recipe['metadata'] = {}
header = document.find('title').get_text().lstrip().rstrip() #returns "Indian Chicken Biryani Recipe "
spans = document.find_all('span', class_="meta-text__label")
timeHeading  = [(span.get_text())for span in spans]
prepTime = document.find_all('span', class_="meta-text__data")
timePrep = [(prep.get_text())for prep in prepTime]
print(timePrep)
recipe['metadata']['name'] = header
recipe['metadata']['preps'] = timeHeading
