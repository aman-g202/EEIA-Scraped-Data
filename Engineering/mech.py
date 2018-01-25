from bs4 import BeautifulSoup
# from urllib.request import Request,urlopen
# import urllib
# import urllib.request
import requests
import json
import csv

# url = 'https://www.coursera.org/browse/physical-science-and-engineering/mechanical-engineering?languages=en'
# r = requests.get(url)
# data = r.text
# soup = BeautifulSoup(data,'lxml')

# mydivs = soup.findAll("div", {"class": "main-container"})
# # print(mydivs[1])
# anchors = mydivs[1].findAll("a",{"data-track-component": "offering_card"})

# courses = {}
# temp=1
# for anchor in anchors:
# 	url = anchor.get('href')
# 	content = anchor.find("div",{"class": "offering-info flex-1"})
# 	name = content.find("div",{"class": "horizontal-box"}).text
# 	university = anchor.find("span",{"class": "offering-partner-names"}).text

# 	courses['course'+str(temp)] = {}
# 	courses['course'+str(temp)]['coursename'] = name
# 	courses['course'+str(temp)]['url'] = "https://www.coursera.org"+url
# 	courses['course'+str(temp)]['university'] = university
# 	temp+=1
# 	print(courses)
# 	break


courses = {}
temp=1
for i in range(1,4):
	url = 'https://www.coursera.org/browse/physical-science-and-engineering/mechanical-engineering?languages=en&page='+str(i)
	r = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data,'lxml')

	mydivs = soup.findAll("div", {"class": "main-container"})
	# print(mydivs[1])
	anchors = mydivs[1].findAll("a",{"data-track-component": "offering_card"})
	

	for j in range(3,len(anchors)):
		url = anchors[j].get('href')
		content = anchors[j].find("div",{"class": "offering-info flex-1"})
		name = content.find("div",{"class": "horizontal-box"}).text
		university = content.find("div",{"class": "offering-partner-names"}).text

		courses['course'+str(temp)] = {}
		courses['course'+str(temp)]['coursename'] = name
		courses['course'+str(temp)]['url'] = "https://www.coursera.org"+url
		courses['course'+str(temp)]['university'] = university
		temp+=1
			
with open('mech.txt', 'w') as outfile:
    json.dump(courses, outfile)		



