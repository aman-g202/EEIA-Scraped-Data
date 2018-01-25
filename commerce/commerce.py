from bs4 import BeautifulSoup
import requests
import json
import csv

courses = {}
temp=1
for i in range(1,10):

	url = 'https://www.coursera.org/browse/business/leadership-and-management?languages=en&page='+str(i)
	r = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data,'lxml')

	mydivs = soup.findAll("div", {"class": "main-container"})
	# print(mydivs[0])
	anchors = mydivs[1].findAll("a",{"data-track-component": "offering_card"})
# # print(str(anchors[2]).find("specialization-course-count"))
	

	for j in range(len(anchors)):
		content = anchors[j].find("div",{"class": "offering-info flex-1"})
		
		if(str(anchors[j]).find("specialization-course-count") != -1):
			university = anchors[j].find("span",{"class": "offering-partner-names"}).text
		else:
			university = content.find("div",{"class": "offering-partner-names"}).text
			
		url = anchors[j].get('href')
		name = content.find("div",{"class": "horizontal-box"}).text
		

		courses['course'+str(temp)] = {}
		courses['course'+str(temp)]['coursename'] = name
		courses['course'+str(temp)]['url'] = "https://www.coursera.org"+url
		courses['course'+str(temp)]['university'] = university
		temp+=1

with open('commerce.txt', 'w') as outfile:
    json.dump(courses, outfile)			
	