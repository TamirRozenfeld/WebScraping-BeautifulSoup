from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

soup = BeautifulSoup(html_text,'lxml')
Dis = soup.find('li', class_="clearfix job-bx wht-shd-bx")
company_name = Dis.find('h3', class_= "joblist-comp-name")
print(company_name)

