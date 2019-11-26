import requests
import urllib.request
import time
import json
#import pymongo
import datetime
from pymongo import MongoClient
from bs4 import BeautifulSoup
from bs4 import NavigableString
import html5lib


# client = MongoClient()
# db = client.scraping
# collection = db.scraped

url = 'https://cours.uqac.ca/liste_cours.html/horaire'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html5lib')
prettySoup = soup.prettify()

# Writing soup to file for analysis
f = open("wholeSoup.txt", "w")
f.write(prettySoup)
f.close()

# Writing "titrecours" to file for analysis
courses = soup.find_all(class_ = "titrecours")

f = open("courses.txt", "w")
f2 = open("courseInCourses.txt", "w")

horaires = []

for course in courses[:3]:
	tagList = []
	index = 0
	horaire = ""
	titre = course.text
	tagList.append(titre + " ")

	horaire += titre

	for tag in course.next_siblings:

		if type(tag) == NavigableString:
			continue

		if tag.has_attr('class') and tag['class'][0] == 'titrecours':
			break

		index += 1		

		tagList.append(tag.name + " ")
		tagList.append(tag.text + " ")

	for i in tagList:
		print(i)

	# 	if tag.has_attr('class') and tag['class'][0] == 'groupe':
	# 		break

	# 	if tag.name != 'groupe':
	# 		continue
		

	# 	rows = tag.find_all('td')

	# 	for row in rows:
	# 		f2.write(row.text)
	# 		if row.has_attr('class') and row['class'][0] == 'petitmot':
	# 			horaire += row.text#.replace('du', '"beg_date:"').replace('au', '"end_date:"').replace('de', '"beg_time:"').replace('à', '"end_time:"').replace('le', '"single_date:"')
				
	# 		if row.has_attr('class') and row['class'][0] == 'local':
	# 			horaire += row.text#.replace('Local', '"local:"')			

	# print(horaire)
	# f.write(horaire)

f.close()
f2.close()
	
	#print(horaire)
	#dicTest = horaire.to_dict()
	#print(dicTest)
		
		
	#jsoned_horaire = horaire.replace('du', '"beg_date:"').replace('au', '"end_date:"').replace('de', '"beg_time:"').replace('à', '"end_time:"').replace('Local', '"local:"')
	#horaires.append(jsoned_horaire)
	

# for shit in horaires:
# 	print(shit)
# 	f.write(shit)


	#id = collection.insert_one(shit).inserted_id
	#print(id)

#result = collection.insert_many(horaires)



# with open("courses.txt", "r") as f:
# 	dictionary =  json.loads(f.read());

# print(dictionary)

# zeList = []

# for items in schedList:
# 	#print(items)
# 	bloup = {items}
# 	zeList.append(bloup)

# for item in zeList:
# 	print(item)
#preJson_sched = horaire.replace('du', '"beg_date:"').replace('au', '"end_date:"').replace('de', '"beg_time:"').replace('à', '"end_time:"')
#jsoned_sched = json.loads(preJson_sched)
#print(jsoned_sched)



	#except NavigableString: 
	#	pass



