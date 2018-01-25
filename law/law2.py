from bs4 import BeautifulSoup
import requests
import json
import csv

url = 'https://www.futurelearn.com/courses/categories/law-courses?all_courses=1'
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data,'lxml')

mydivs = soup.findAll("div", {"class": "m-new-card"})
# print(len(mydivs))

courses = {}
temp=33

for div in mydivs:
	url = "https://www.futurelearn.com"+div.find("a").get("href")
	# print(url)
	university = div.find("a").find("div",{"class": "a-item-title"}).text
	name = div.find("a").find("div",{"class": "m-new-card__title"}).text
	
	courses['course'+str(temp)] = {}
	courses['course'+str(temp)]['coursename'] = name
	courses['course'+str(temp)]['url'] = url
	courses['course'+str(temp)]['university'] = university
	temp+=1

with open('law.txt', 'a') as outfile:
    json.dump(courses, outfile)	

