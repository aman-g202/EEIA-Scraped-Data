from bs4 import BeautifulSoup
import requests
import json
import csv

courses = {}
temp=1
count=0
for i in range(1,8):

	url = 'https://www.coursera.org/courses?languages=en&query=electronics&start='+str(count)
	r = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data,'lxml')

	mydivs = soup.findAll("div", {"class": "rc-SearchResults"})
	# print(mydivs[0])
	anchors = mydivs[0].findAll("a",{"data-track-component": "offering_card"})
# # print(str(anchors[2]).find("specialization-course-count"))
	

	for j in range(len(anchors)):
		if(str(anchors[j]).find("specialization-course-count") != -1):
			continue
		url = anchors[j].get('href')
		content = anchors[j].find("div",{"class": "offering-info flex-1"})
		name = content.find("div",{"class": "horizontal-box"}).text
		university = content.find("div",{"class": "offering-partner-names"}).text

		courses['course'+str(temp)] = {}
		courses['course'+str(temp)]['coursename'] = name
		courses['course'+str(temp)]['url'] = "https://www.coursera.org"+url
		courses['course'+str(temp)]['university'] = university
		temp+=1
	count+=20
			
with open('ec.txt', 'w') as outfile:
    json.dump(courses, outfile)