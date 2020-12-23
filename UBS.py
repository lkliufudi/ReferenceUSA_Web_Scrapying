#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import re
import pandas as pd
import numpy as np
import random
from configparser import ConfigParser


# In[2]:


pip install webdriver-manager


# In[42]:


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())


# In[20]:


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


# In[44]:


def collect_url():
        print("collecting url from page{}".format(k))
        source = driver.page_source
        time.sleep(2)
        url_page = re.findall(r'data-tagged-url="(.*?)">', source, re.S)
        for i in url_page:
            real_url= "https://ezproxy.stevens.edu:4146{}".format(i)
            company_url.append(real_url)


# In[4]:


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


# In[5]:


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


# In[6]:


def collect_company_info():
        company_name=driver.find_element_by_id('businessName').text
        company_address=driver.find_element_by_xpath('//*[@id="LocationInfo"]/div/div[2]/div/table[1]/tbody/tr[2]/td[1]').text
        company_city_state=driver.find_element_by_xpath('//*[@id="LocationInfo"]/div/div[2]/div/table[1]/tbody/tr[3]/td[1]').text
        company_phone=driver.find_element_by_class_name('firstTd').text
        company_metro_area=driver.find_element_by_xpath('//*[@id="LocationInfo"]/div/div[2]/div/table[1]/tbody/tr[3]/td[2]').text
        
        company_SIC_name=driver.find_element_by_xpath('//*[@id="IndustryProfile"]/div/div[2]/div/table/tbody/tr[2]/td[2]').text
        company_SIC_number = driver.find_element_by_xpath('//*[@id="IndustryProfile"]/div/div[2]/div/table/tbody/tr[2]/td[1]').text
        
        company_location_employees=driver.find_element_by_xpath('//*[@id="BusinessDemographics"]/div/div[2]/div/table[1]/tbody/tr[1]/td[1]').text
        company_corporate_employees=driver.find_element_by_xpath('//*[@id="BusinessDemographics"]/div/div[2]/div/table[1]/tbody/tr[2]/td[1]').text
        company_type_of_business=driver.find_element_by_xpath('//*[@id="BusinessDemographics"]/div/div[2]/div/table[1]/tbody/tr[3]/td[1]').text
        company_parent_company=driver.find_element_by_xpath('//*[@id="BusinessDemographics"]/div/div[2]/div/table[1]/tbody/tr[5]/td[1]').text
        company_years_in_database=driver.find_element_by_xpath('//*[@id="BusinessDemographics"]/div/div[2]/div/table[1]/tbody/tr[8]/td[1]').text
        company_square_footage=driver.find_element_by_xpath('//*[@id="BusinessDemographics"]/div/div[2]/div/table[1]/tbody/tr[9]/td[1]').text
        company_home_business=driver.find_element_by_xpath('//*[@id="BusinessDemographics"]/div/div[2]/div/table[1]/tbody/tr[10]/td[1]').text
        company_location_sales_volume=driver.find_element_by_xpath('//*[@id="BusinessDemographics"]/div/div[2]/div/table[1]/tbody/tr[1]/td[2]').text
        company_corporate_sales_volume=driver.find_element_by_xpath('//*[@id="BusinessDemographics"]/div/div[2]/div/table[1]/tbody/tr[2]/td[2]').text
        company_location_type=driver.find_element_by_xpath('//*[@id="BusinessDemographics"]/div/div[2]/div/table[1]/tbody/tr[3]/td[2]').text
        company_last_updated_on=driver.find_element_by_xpath('//*[@id="BusinessDemographics"]/div/div[2]/div/table[1]/tbody/tr[7]/td[2]').text
        company_year_established=driver.find_element_by_xpath('//*[@id="BusinessDemographics"]/div/div[2]/div/table[1]/tbody/tr[8]/td[2]').text
        company_credit_rating=driver.find_element_by_xpath('//*[@id="BusinessDemographics"]/div/div[2]/div/table[1]/tbody/tr[10]/td[2]').text
        
        company_labor_expenditures=driver.find_element_by_xpath('//*[@id="BusinessExpenditures"]/div/div[2]/div/table/tbody/tr[3]/td[1]').text
        company_rent_lease_expenditures = driver.find_element_by_xpath('//*[@id="BusinessExpenditures"]/div/div[2]/div/table/tbody/tr[7]/td[1]').text
        company_technology = driver.find_element_by_xpath('//*[@id="BusinessExpenditures"]/div/div[2]/div/table/tbody/tr[7]/td[2]').text
        
        return company_name,company_address,company_city_state,company_phone, company_metro_area,company_SIC_name,company_SIC_number,company_location_employees,company_corporate_employees,company_type_of_business,company_parent_company,company_years_in_database,company_square_footage,company_home_business,company_location_sales_volume,company_corporate_sales_volume,company_location_type,company_last_updated_on,company_year_established,company_credit_rating,company_labor_expenditures,company_rent_lease_expenditures,company_technology
                


# In[57]:


company_url=[]


# In[59]:


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


# In[60]:


company_url


# In[61]:


with open('url_ubs_hoboken.txt', 'w') as filehandle:
    for listitem in company_url:
       filehandle.write('%s\n' % listitem)


# In[64]:


df=pd.DataFrame(columns = ['company_name','company_address','company_city_state','company_phone'], index=range(len(company_url)))


# In[65]:


row_number=0
for url in company_url:
    driver.get(url)
    anti_crawler_company()
    time.sleep(2)
    company_name,company_address,company_city_state,company_phone, company_metro_area,company_SIC_name,company_SIC_number,company_location_employees,company_corporate_employees,company_type_of_business,company_parent_company,company_years_in_database,company_square_footage,company_home_business,company_location_sales_volume,company_corporate_sales_volume,company_location_type,company_last_updated_on,company_year_established,company_credit_rating,company_labor_expenditures,company_rent_lease_expenditures, company_technology = collect_company_info()
    df.iloc[row_number,0]=company_name
    df.iloc[row_number,1]=company_address
    df.iloc[row_number,2]=company_city_state
    df.iloc[row_number,3]=company_phone
    row_number=row_number+1
    print(row_number)


# In[12]:


if __name__ == "__main__":
    collect_url()
    for i in range(len(company_url)):
        if ms365.iloc[i,1] != "None":
            url=ms365.iloc[i,1]
            driver.get(url)
            time.sleep(2)
            anti_crawler_company()
            company_name,company_address,company_city_state,company_phone, company_metro_area,company_SIC_name,company_SIC_number,company_location_employees,company_corporate_employees,company_type_of_business,company_parent_company,company_years_in_database,company_square_footage,company_home_business,company_location_sales_volume,company_corporate_sales_volume,company_location_type,company_last_updated_on,company_year_established,company_credit_rating,company_labor_expenditures,company_rent_lease_expenditures, company_technology = collect_company_info()
            ms365.iloc[i,2]=company_name
            ms365.iloc[i,3]=company_address+" "+company_city_state
            ms365.iloc[i,4]=company_phone
            ms365.iloc[i,5]=company_metro_area
            ms365.iloc[i,6]=company_SIC_name
            ms365.iloc[i,7]=company_SIC_number
            ms365.iloc[i,8]=company_location_employees
            ms365.iloc[i,9]=company_corporate_employees
            ms365.iloc[i,10]=company_type_of_business
            ms365.iloc[i,11]=company_parent_company
            ms365.iloc[i,12]=company_years_in_database
            ms365.iloc[i,13]=company_square_footage
            ms365.iloc[i,14]=company_home_business
            ms365.iloc[i,15]=company_location_sales_volume
            ms365.iloc[i,16]=company_corporate_sales_volume
            ms365.iloc[i,17]=company_location_type
            ms365.iloc[i,18]=company_last_updated_on
            ms365.iloc[i,19]=company_year_established
            ms365.iloc[i,20]=company_credit_rating
            ms365.iloc[i,21]=company_labor_expenditures
            ms365.iloc[i,22]=company_rent_lease_expenditures
            ms365.iloc[i,23]=company_technology


# In[66]:


df.to_csv("ubs_refer.csv")


# In[ ]:




