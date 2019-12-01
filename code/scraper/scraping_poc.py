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
		'09:00': '00',
		'09:15': '00',
		'09:30': '01',
		'10:45': '01',
		'11:00': '02',
		'12:00': '02',
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
	#print(course_names)
	

	for course in course_names[:100]:
		course.group = []
		course.horaires = []
		list_horaire = []
		course.titre = ""
		index1=0
		index2=0
		index3=0

		course.titre = course.text
		
		for element in course.next_siblings:
			#print("index1 = " + str(index1))
			#index1+=1
			if type(element) == NavigableString:
				#print("boobs")
				continue

			if element.has_attr('class') and element['class'][0] == "titrecours":
				#print("patate")
				break

			if element.name == "p":
				#print("bitch")
				for child in element.children:
					#print(child.name)

					if type(child) != NavigableString and child.name != "a":
						course.group.append(child.text)
		
			if element.name == "table":
				course.horaire = []
				print("########################################################")
				rows = element.find_all('td')
				for row in rows:
					
					course.horaire.append(row.text)
					#print(course.horaire)

				#print(course.horaire)
						
					#course.horaire = str(course.horaire).split()
					#print(course.horaire)
				#print(course.horaire)
				#print(course.horaire)

				indexes = []

				for i, j in enumerate(course.horaire):
					if j == "du":
						patates = 0
						indexes.append(i)

					elif j == "le":
						patates = 1
						indexes.append(i)

				for index in indexes:
					if patates == 0:
						#print(len(course.horaire))
						#print(course.horaire)
						#if course.horaire[index] == "du":
							#if len(course.horaire) > 8:
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
							
					elif patates == 1:
						course.beg_day = course.horaire[index + 1]
						course.beg_date = course.horaire[index + 2]
						course.end_day = course.horaire[index + 4]
						course.end_date = course.horaire[index + 5]
						course.local = course.horaire[index + 7]
						course.horaires.append([dayTimeToCodes(course.beg_day, course.beg_time, course.end_time), course.local])

					else:
						course.horaire.append(["À déterminer"])

					# elif course.horaire[0] == "le":
					# 	course.beg_day = course.horaire[1]
					# 	course.beg_date = course.horaire[2]
					# 	course.beg_time = course.horaire[4]
					# 	course.end_time = course.horaire[6]
					# 	course.local = course.horaire[8]
					# 	course.horaire = [dayTimeToCodes(course.beg_day, course.beg_time, course.end_time), course.local]
						
					# else:
					# 	course.horaire = ["À déterminer"]	
						
					# list_horaire.append(course.horaire)

		print(course.titre)
		print(course.group)
		print(course.horaires)

# if len(course.group) == len(list_horaire) + 1:
# 	list_horaire.append("Horaire non disponible")

		# jsoned = 'titre' + ':' + str(course.titre)

		# # vector = [course.titre]
		# # for i in range(len(course.group)):
		# # 	vector.append(course.group[i])
		# # 	vector.append(list_horaire[i])
		# # print(vector)


		# for i in range(len(course.group)):

		# 	if len(list_horaire) != 0:
		# 		jsoned += " " + 'group' + ':' + " " + str(course.group[i]) + " " + 'horaire' + ':' + " " + str(list_horaire[i])

		# #print(jsoned)

	return 

scraper()







