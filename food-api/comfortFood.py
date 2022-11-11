from bs4 import BeautifulSoup
import requests
from sqlalchemy.dialects.postgresql import ARRAY
from app import User, db
from mongodbConnect import *

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

ingredientHeader = document.find('h3' , class_="section__title section__title--bold-underline").get_text()
methodHeader = document.find_all('h3', class_="section__title section__title--bold-underline")[1].get_text()

lists = document.find_all('li', class_="structured-ingredients__list-item")
listprep = [(li.get_text()) for li in lists]

orderList = []
for li in listprep:
 if '\n' in li:
     newli =li.replace('\n', '')
     orderList.append(newli)

print(orderList)


if '\n' in timePrep[3]:
 splitting1 = timePrep[3].replace('\n', ' ')
 timePrep.pop(3)
 timePrep.append(splitting1)
 

recipe['metadata']['name'] = header
recipe['metadata']['headings'] = timeHeading
recipe['metadata']['timeprep'] = timePrep
recipe['metadata']['lisprep'] = orderList
# class Info(db.Model):
#     id=db.Column()
#     header=db.Column(db.String(50), nullable=False )
#     timeHeading=db.Column(ARRAY(db.String))
#     prepTime = db.Column(ARRAY(db.String))
db_collection_dinner.insert_one(recipe)