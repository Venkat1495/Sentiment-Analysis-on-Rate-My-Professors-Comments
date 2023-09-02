import requests
from bs4 import BeautifulSoup
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


browser = webdriver.Chrome(executable_path='/Users/venky/Documents/chromedriver_mac_arm64/chromedriver.exe')
Load_xpath = "//button[contains(text(),'Load More Ratings')]"
url = []
js_code = "arguments[0].scrollIntoView({'block':'center','inline':'center'});"
file = open("reviews.txt","a")
text_num_review_g = 0

with open('newdoc.txt', 'r') as file_url:
    for line in file_url:
        # Process the line
        url.append(line.strip()) # Example: Print the line after removing leading/trailing whitespaces

def check_exists_by_xpath(xpath):
    try:
        browser.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

def proff_reviews(num):
    # df = pd.read_csv("out.csv")
    # df.columns = ['comments','student_star','student_difficult']
    # columns = "comments,student_star,student_difficult"
    # file.write(f"{columns}\n")
    if (check_exists_by_xpath("//a[@href='#ratingsList']")):
        num_review = browser.find_element(By.XPATH, "//a[@href='#ratingsList']")
        text_num_review = num_review.text
        text_num_review = text_num_review.split(" ")
        text_num_review = int(text_num_review[0])
        num = num + text_num_review


        while(check_exists_by_xpath(Load_xpath)):
            Load_element = browser.find_element(By.XPATH, "//button[contains(text(),'Load More Ratings')]")
            # actions = ActionChains(browser)
            # actions.move_to_element(Load_element).perform()
            # Execute the JS script
            browser.execute_script(js_code, Load_element)
            time.sleep(3)
            Load_element.click()
            time.sleep(3)

        comments = browser.find_elements(By.XPATH, "//div[@class='Comments__StyledComments-dzzyvm-0 gRjWel']")
        quality = browser.find_elements(By.XPATH, "//div[contains(text(),'Quality')]/following-sibling::div")
        difficulty = browser.find_elements(By.XPATH, "//div[contains(text(),'Difficulty')]/following-sibling::div")

        text_comments = []
        text_quality = []
        text_difficulty = []
        
        for i in comments:
            text_comments.append(i.text)
        
        for i in quality:
            text_quality.append(i.text)
        
        for i in difficulty:
            text_difficulty.append(i.text)

        if len(text_comments) == len(text_quality) and len(text_comments) == len(text_difficulty):
            for i in range(0,len(text_comments)):
                # new_row = "text_comments[i], text_quality[i], text_difficulty[i]"
                file.write(f"{text_comments[i]},{text_quality[i]},{text_difficulty[i]}\n")
    return num
        


# browser.get("https://www.ratemyprofessors.com/professor/234221")
# text_num_review_g = proff_reviews(text_num_review_g)



for i in range(0,100):
    browser.get(url[i])
    text_num_review_g = proff_reviews(text_num_review_g)
    print(url[i])

print(text_num_review_g)
file.close()

browser.quit()

    



# def scrapeUniversity():

#     file = open("word.txt","a")
#     profs = browser.find_elements(By.CLASS_NAME,"TeacherCard__StyledTeacherCard-syjs0d-0")
#     for i in profs:
#         print(i.get_attribute("href"))
#         file.write(str(i.get_attribute("href"))+ "\n")
#     file.close()
#     return {}

# def scrapeProfessor(url):
#     return {}


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