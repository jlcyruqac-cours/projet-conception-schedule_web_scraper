import requests
import urllib.request
import time
import json
import datetime
from pymongo import MongoClient
from bs4 import BeautifulSoup
from bs4 import NavigableString
import html5lib


url = 'https://cours.uqac.ca/liste_cours.html/horaire'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html5lib')
prettySoup = soup.prettify()

# Writing soup to file for analysis
f = open("wholeSoup.txt", "w")
f.write(prettySoup)
f.close()

# list_courses returns 1 huge item containing all courses
list_courses = soup.find(id = "liste_horaire")

# Function to convert day/time to codes
def dayTimeToCodes(day, begTime, endTime):
	switcher = {
		'lundi': '0',
		'mardi' : '1',
		'mercredi': '2',
		'jeudi': '3',
		'vendredi': '4',
		'samedi': '5',
		'dimanche': '6',
		'08:00': '00',
		'09:15': '00',
		'09:30': '01',
		'10:45': '01',
		'11:00': '02',
		'12:15': '02',
		'13:00': '03',
		'14:15': '03',
		'14:30': '04',
		'15:45': '04',
		'16:00': '05',
		'17:15': '05',
		'17:30': '06',
		'18:45': '06',
		'19:00': '07',
		'20:15': '07',
		'20:30': '08',
		'21:45': '08'
	}

	begtime_code = switcher.get(begTime, "begTime Error!!")
	endtime_code = switcher.get(endTime, "endTime Error!!")
	day_code = switcher.get(day, "day Error!!")

	# Check if course spans more than 1 period and return
	# code(s) accordingly
	if begtime_code != endtime_code:
		codes = day_code + begtime_code + " " + day_code + endtime_code

	else:
		codes = day_code + begtime_code

	return(codes)

##########################################################################################
# SCRAPER
##########################################################################################

def scraper():
	course_names = list_courses.find_all(class_ = "titrecours")

	for course in course_names[:200]:
		course.group = []
		course.horaire = []
		list_horaire = []

		course.titre = course.text
		
		for element in course.next_siblings:


			if type(element) == NavigableString:
				continue

			if element.has_attr('class') and element['class'][0] == "titrecours":
				break

			if element.name == "p":

				for child in element.children:

					if type(child) != NavigableString and child.name != "a":
						course.group.append(child.text)
		
			if element.name == "table":
	
				
				for child in element.children:
					

					if type(child) != NavigableString:
						this_horaire = child.text.split()

						if this_horaire[0] == "du":
							if len(this_horaire) > 8:
								course.beg_day = this_horaire[1]
								course.beg_date = this_horaire[2]
								course.end_day = this_horaire[4]
								course.end_date = this_horaire[5]
								course.beg_time = this_horaire[7]
								course.end_time = this_horaire[9]
								course.local = this_horaire[11]
								#course.horaire.extend([dayTimeToCodes(course.beg_day, course.beg_time, course.end_time), course.local])
								course.horaire = [dayTimeToCodes(course.beg_day, course.beg_time, course.end_time), course.local]
								#test.append([dayTimeToCodes(course.beg_day, course.beg_time, course.end_time), course.local])

							else:
								course.beg_day = this_horaire[1]
								course.beg_date = this_horaire[2]
								course.end_day = this_horaire[4]
								course.end_date = this_horaire[5]
								course.local = this_horaire[7]
								#course.horaire.extend([dayTimeToCodes(course.beg_day, course.beg_time, course.end_time), course.local])
								course.horaire = [dayTimeToCodes(course.beg_day, course.beg_time, course.end_time), course.local]
								#test.append([dayTimeToCodes(course.beg_day, course.beg_time, course.end_time), course.local])

						elif this_horaire[0] == "le":
							course.beg_day = this_horaire[1]
							course.beg_date = this_horaire[2]
							course.beg_time = this_horaire[4]
							course.end_time = this_horaire[6]
							course.local = this_horaire[8]
							#course.horaire.extend([dayTimeToCodes(course.beg_day, course.beg_time, course.end_time), course.local])
							course.horaire = [dayTimeToCodes(course.beg_day, course.beg_time, course.end_time), course.local]
							#test.append([dayTimeToCodes(course.beg_day, course.beg_time, course.end_time), course.local])

						else:
							#course.horaire.extend(["À déterminer"])
							course.horaire = ["À déterminer"]	
							#test.append(["À déterminer"])

						list_horaire.append(course.horaire)		

		if len(course.group) == len(list_horaire) + 1:
			list_horaire.append("Horaire non disponible")

		jsoned = 'titre' + ':' + str(course.titre)

		for i in range(len(course.group)):
			if len(list_horaire) != 0:
				jsoned += " " + 'group' + ':' + " " + str(course.group[i]) + " " + 'horaire' + ':' + " " + str(list_horaire[i])

		print(jsoned)
		print(json.dumps({jsoned}))

	return 


scraper()







