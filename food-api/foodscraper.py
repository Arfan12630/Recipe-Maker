from bs4 import BeautifulSoup
import requests
from sqlalchemy.dialects.postgresql import ARRAY
from app import User, db


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

if '\n' in timePrep[3]:
 splitting1 = timePrep[3].replace('\n', ' ')
 timePrep.pop(3)
 timePrep.append(splitting1)
 

print(timePrep)
recipe['metadata']['name'] = header
recipe['metadata']['preps'] = timeHeading


# class Info(db.Model):
#     id=db.Column()
#     header=db.Column(db.String(50), nullable=False )
#     timeHeading=db.Column(ARRAY(db.String))
#     prepTime = db.Column(ARRAY(db.String))
