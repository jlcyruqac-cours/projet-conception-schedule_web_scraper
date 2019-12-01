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

# Cooking the soup
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
		'08:30': '00',
		'09:00': '00',
		'09:15': '00',
		'09:30': '01',
		'10:45': '01',
		'11:00': '02',
		'11:45': '02',
		'12:00': '02',
		'12:15': '02',
		'12:30': '02',
		'12:45': '03',
		'13:00': '03',
		'14:00': '03',
		'14:15': '03',
		'14:30': '04',
		'15:00': '04',
		'15:30': '04',
		'15:45': '04',
		'16:00': '05',
		'16:30': '05',
		'16:45': '05',
		'17:00': '05',
		'17:15': '05',
		'17:30': '06',
		'18:00': '06',
		'18:30': '06',
		'18:45': '06',
		'19:00': '07',
		'20:15': '07',
		'20:45': '08',
		'20:30': '08',
		'21:30': '08',
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

	for course in course_names:
		course.group = []
		course.horaires = []
		list_horaire = []
		course.titre = ""
		
		course.titre = course.text
		course.horaires.append(course.titre.strip())
		
		for element in course.next_siblings:
			
			if type(element) == NavigableString:
				continue

			if element.has_attr('class') and element['class'][0] == "titrecours":
				break

			if element.name == "p":

				for child in element.children:

					if type(child) != NavigableString and child.name != "a":
						course.group.append(child.text)
						course.horaires.append(child.text)
		
			if element.name == "table":
				course.horaire = []
				rows = element.find_all('td')

				for row in rows:
					course.horaire.append(row.text)

				#print(course.horaire)

				filtered_list = []

				filtered_list = list(filter(lambda a: a != '\xa0', course.horaire))

				course.horaire = list(filter(lambda a: a != '', filtered_list))

				indexes = []
				indexes1 = []
				indexes2 = []
				test = 0
				test1 = 0
				test2 = 0

				for i, j in enumerate(course.horaire):
					if j == "du":
						test = 0
						indexes.append(i)

					if j == "le":
						test1 = 1
						indexes1.append(i)

					if j == "Horaire à déterminer":
						test2 = 2
						indexes2.append(i)
				
				if test == 0:
					for index in indexes:
					
						if len(course.horaire) > 10:
							course.beg_day = course.horaire[index + 1]
							course.beg_date = course.horaire[index + 2]
							course.end_day = course.horaire[index + 4]
							course.end_date = course.horaire[index + 5]
							course.beg_time = course.horaire[index + 7]
							course.end_time = course.horaire[index + 9]
							course.local = course.horaire[index + 11]
							course.horaires.append([dayTimeToCodes(course.beg_day, course.beg_time, course.end_time), course.local])

						else:
							course.beg_day = course.horaire[index + 1]
							course.beg_date = course.horaire[index + 2]
							course.end_day = course.horaire[index + 4]
							course.end_date = course.horaire[index + 5]
							course.beg_time = "N/A"
							course.end_time = "N/A"
							course.local = course.horaire[index + 7]
							course.horaires.append([course.beg_day, course.beg_date, course.end_day, course.end_date, course.local])
							
				if test1 == 1:
					for index in indexes1:
						course.beg_day = course.horaire[index + 1]
						course.beg_date = course.horaire[index + 2]
						course.beg_time = course.horaire[index + 4]
						course.end_time = course.horaire[index + 6]
						course.local = course.horaire[index + 8]
						course.horaires.append([dayTimeToCodes(course.beg_day, course.beg_time, course.end_time), course.local])

				if test2 == 2:
					for index in indexes2:
						course.horaires.append(["À déterminer"])

		print(course.horaires)

	return(course.horaires)

scraper()







