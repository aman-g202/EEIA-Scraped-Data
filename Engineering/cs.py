from bs4 import BeautifulSoup
# from urllib.request import Request,urlopen
# import urllib
# import urllib.request
import requests
import json
import csv

url = 'https://www.computerscienceonline.org/courses/'
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data,'lxml')

mydivs = soup.findAll("div", {"class": "comp-sci-con-box"})
# gets = mydivs[0].findAll("td")


courses = {}
temp = 1
for typecourse in mydivs:
	gets = typecourse.findAll("td")
	for i in range(len(gets)):
		if(i % 2 == 0):
			name = gets[i].text
			url = gets[i].find('a').get('href')
			courses['course'+str(temp)] = {}
			courses['course'+str(temp)]['coursename'] = name
			courses['course'+str(temp)]['url'] = url
			temp+=1
		else:
			university = gets[i].text
			courses['course'+str(temp-1)]['university'] = university

with open('cs.txt', 'w') as outfile:
    json.dump(courses, outfile)	
# with open('cs.cvv', 'wb') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     wr.writerow(courses)