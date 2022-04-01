from email import header
from turtle import width
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
starturl='https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
bowser=webdriver.Chrome('C:/Users/askmb/Downloads/chromedriver_win32/chromedriver')
bowser.get(starturl)
time.sleep(10)
def scrap():
    header=['name','light_years_from_earth','planet_mass','stellar_magnitude','discovery_date']
    planet_data=[]
    for i in range(0,3):
        soup=BeautifulSoup(bowser.page_source,'html.parser')
        for ul_tag in soup.find_all('ul',attrs={'class','exoplanet'}):
            li_tags=ul_tag.find_all('li')
            temp_list=[]
            for index,li_tag in enumerate(li_tags):
                if index==0:
                    temp_list.append(li_tag.find_all('a')[0].contents[0])
                else:
                    temp_list.append(li_tag.contents[0])
            planet_data.append(temp_list)
        bowser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open('data.csv','w',newline='') as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow(header)
        csvwriter.writerows(planet_data)

scrap()