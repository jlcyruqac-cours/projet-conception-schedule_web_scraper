import re


# class courses:
#     def __init__(self):
#         self.sigle = None
#         self.name = None
from models.courses import Course

def load_courses():
    courses_list = []
    with open('courses_list.txt', 'r', encoding='iso-8859-1') as scraped_data:
        line = scraped_data.readline()
        cnt = 1
        while line:
            # print("Line {}: {}".format(cnt, line.strip()))
            course = Course()
            sigle = re.search('\d\w\w\w\d\d\d', line)
            line_without_sigle = line[8:]

            splited_line = line_without_sigle.split('(')
            # print(result)
            if sigle:
                course.sigle = (sigle.group())
                course.name = splited_line[0]

                print(course.sigle)
                print(course.name)
                course.save()


            else:
                if line.strip() == "du":
                    for index in range(12):
                        if index == 1 or index == 2 or index == 4 or index == 5 or index == 7 or index == 9 or index == 11:
                            # print(line)
                            a=1
                        line = scraped_data.readline()
            courses_list.append(course)
            line = scraped_data.readline()
