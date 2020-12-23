#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import re
import pandas as pd
import numpy as np
import random
from configparser import ConfigParser

pip install webdriver-manager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())

def Enter_City_Page(City):
    cfg = ConfigParser()
    r = cfg.read('password.ini')
    username = cfg.get('username', 'username')
    password = cfg.get('password', 'password')
    driver.get('https://ezproxy.stevens.edu/login?qurl=https%3a%2f%2fwww.referenceusa.com')
    driver.find_element_by_name('user').send_keys(username) 
    driver.find_element_by_name('pass').send_keys(password)
    click_xpath='/html/body/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td[2]/table/tbody/tr[6]/td[3]/input'
    driver.find_element_by_xpath(click_xpath).click()
    time.sleep(1)
    driver.find_element_by_class_name('moreInfoSearchBtn').click()
    time.sleep(1)
    driver.find_element_by_class_name('advancedSearch').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="cs-MajorIndustryGroup"]').click()
    driver.find_element_by_xpath('//*[@id="cs-CityState"]').click()
    #driver.find_element_by_xpath('//*[@id="NixieOnly"]').click()
    #driver.find_element_by_xpath('//*[@id="VerifiedOnly"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="migTreeView"]/ul/li[7]/div').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="migTreeView"]/ul/li[7]/ul/li[3]/div').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="migTreeView"]/ul/li[7]/ul/li[3]/ul/li[1]/label/input').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="filterCityState"]').send_keys(City)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="SearchCityState"]/span/span').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="availableCityState"]/ul/li[2]/div[1]/span/span[1]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="dbSelector"]/div/div[2]/div[1]/div[3]/div/a[1]').click()
    time.sleep(1)

def collect_url():
        print("collecting url from page{}".format(k))
        source = driver.page_source
        time.sleep(2)
        url_page = re.findall(r'data-tagged-url="(.*?)">', source, re.S)
        for i in url_page:
            real_url= "https://ezproxy.stevens.edu:4146{}".format(i)
            company_url.append(real_url)

def anti_crawler_list():
    while True:
        try:
            driver.find_element_by_id('captchaHelpText').text == "Please enter only the answer for the above math equation."
            driver.find_element_by_class_name("captchaTextWidth").clear()
            print("Enter the answer")
            x=input()
            driver.find_element_by_name("ResultViews.Attempt").send_keys(x)
            driver.find_element_by_xpath('//*[@id="captchaValidation"]/a[2]/span/span').click()
            time.sleep(3)
        except:
            break

def anti_crawler_company():
    while True:
        try:
            driver.find_element_by_id('captchaHelpText').text == "Please enter only the answer for the above math equation."
            driver.find_element_by_class_name("captchaTextWidth").clear()
            print("Enter the answer")
            x=input()
            driver.find_element_by_name("ResultViews.Attempt").send_keys(x)
            driver.find_element_by_xpath('//*[@id="captchaValidation"]/a/span/span').click()
            time.sleep(3)
        except:
            break

def collect_company_info():
        company_name=driver.find_element_by_id('businessName').text
        company_address=driver.find_element_by_xpath('//*[@id="LocationInfo"]/div/div[2]/div/table[1]/tbody/tr[2]/td[1]').text 
        company_SIC_name=driver.find_element_by_xpath('//*[@id="IndustryProfile"]/div/div[2]/div/table/tbody/tr[2]/td[2]').text
        company_SIC_number = driver.find_element_by_xpath('//*[@id="IndustryProfile"]/div/div[2]/div/table/tbody/tr[2]/td[1]').text
        company_updated=driver.find_element_by_xpath('//*[@id="BusinessDemographics"]/div/div[2]/div/table[1]/tbody/tr[7]/td[2]').text
        return company_name, company_address, company_SIC_name, company_SIC_number, company_updated
                

company_url=[]
Enter_City_Page('Hoboken')
k = 0
max_page=int(driver.find_element_by_class_name('data-page-max').text)
while True:
    k=k+1
    anti_crawler_list()
    collect_url()
    if k==max_page:
        print("complete data collection")
        break
    else:   
        driver.find_element_by_xpath('//*[@id="searchResults"]/div[1]/div/div[1]/div[2]/div[3]').click()
        time.sleep(2)

with open('url_ubs_hoboken.txt', 'w') as filehandle:
    for listitem in company_url:
       filehandle.write('%s\n' % listitem)

file_input = open("url_ubs_hoboken.txt",'r')
company_url = file_input.readlines()

start = 2500
end = 3000

df=pd.DataFrame(columns = ['company_name','company_address','company_SIC_name','company_SIC_number','company_updated'], index=range(len(company_url)))

for url in company_url[start:end]:
    driver.get(url)
    time.sleep(2)
    print("collecting data from company No.{}".format(row_number))
    try:
        driver.find_element_by_id('captchaHelpText').text == "Please enter only the answer for the above math equation."
        anti_crawler_company()
        time.sleep(4)
        try: 
            driver.find_element_by_id('captchaHelpText').text == "Please enter only the answer for the above math equation."
            print("Wrong Answer, Only One Chance Left!!!!!!!")
            driver.find_element_by_class_name("captchaTextWidth").clear()
            anti_crawler_company()
            time.sleep(2)
            company_name, company_address, company_SIC_name, company_SIC_number, company_updated = collect_company_info()
        except:
            company_name, company_address, company_SIC_name, company_SIC_number, company_updated =collect_company_info()
    except:
        company_name, company_address, company_SIC_name, company_SIC_number, company_updated =collect_company_info()
    finally:    
        df.iloc[row_number,0]=company_name
        df.iloc[row_number,1]=company_address
        df.iloc[row_number,2]=company_SIC_name
        df.iloc[row_number,3]=company_SIC_number
        df.iloc[row_number,4]=company_updated

        if row_number == len(company_url):
            break
        else:
            row_number = row_number + 1

df.to_csv("ubs_refer.csv")
