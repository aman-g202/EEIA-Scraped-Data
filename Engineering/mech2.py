from bs4 import BeautifulSoup
# from urllib.request import Request,urlopen
# import urllib
# import urllib.request
import requests
import json
import csv

url = 'https://www.academiccourses.com/Courses/Mechanical-Engineering/'
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data,'lxml')

mydivs = soup.findAll("div", {"class": "list-item"})

courses = {}
temp=58

for div in mydivs:
	details = div.find("div", {"class": "school-info"})
	url = details.find("h4").find("a").get("href")
	name = details.find("h4").find("a").text
	university = details.find("h5").find("span").text

	courses['course'+str(temp)] = {}
	courses['course'+str(temp)]['coursename'] = name
	courses['course'+str(temp)]['url'] = url
	courses['course'+str(temp)]['university'] = university
	temp+=1

with open('mech.txt', 'a') as outfile:
    json.dump(courses, outfile)		
	
