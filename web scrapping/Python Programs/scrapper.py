import requests
from bs4 import BeautifulSoup
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By



browser = webdriver.Chrome(executable_path='/Users/venky/Documents/chromedriver_mac_arm64/chromedriver.exe')

def scrapeUniversity():

    file = open("word.txt","a")
    profs = browser.find_elements(By.CLASS_NAME,"TeacherCard__StyledTeacherCard-syjs0d-0")
    for i in profs:
        print(i.get_attribute("href"))
        file.write(str(i.get_attribute("href"))+ "\n")
    file.close()
    return {}

def scrapeProfessor(url):
    return {}


# for i in range(1,2):
#     scrapeUniversity(f'https://www.ratemyprofessors.com/search/teachers?query=*&sid={i}')

# browser.get("https://www.ratemyprofessors.com/search/teachers?query=*&sid=1")
# print("Jello 1")
# print(browser.page_source)
# result = browser.find_elements(By.CLASS_NAME, "TeacherCard__StyledTeacherCard-syjs0d-0")
# print("--------------------------------")

# print(result)
# for i in result:
#     print(i.get_attribute("href"))
# browser.quit()

for i in range(10,20):
    browser.get(f'https://www.ratemyprofessors.com/search/teachers?query=*&sid={i}')
    scrapeUniversity()
