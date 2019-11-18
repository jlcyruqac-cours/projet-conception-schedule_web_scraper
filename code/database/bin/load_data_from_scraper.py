import re

from models import courses

if __name__ == '__main__':
    with open('courses_list.txt', 'r', encoding='iso-8859-1') as scraped_data:
        line = scraped_data.readline()
        cnt = 1
        while line:
            # print("Line {}: {}".format(cnt, line.strip()))
            x = re.search('\d\w\w\w\d\d\d',line)
            print(x)
            line = scraped_data.readline()
            cnt += 1