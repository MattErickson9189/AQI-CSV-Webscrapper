from selenium import webdriver
from selenium.webdriver.support.ui import Select
import sys, os, time
browser = webdriver.Firefox()

URL = "https://www.epa.gov/outdoor-air-quality-data/air-quality-statistics-report"
path = "./Data/"

#Array to store the desired dates
dates = ["1980","1985","1990","1995","2000","2005","2010","2015","2019"]

#Array to store the desired states
states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]


browser.get(URL)
time.sleep(4)
year = Select(browser.find_element_by_id('year'))
year.select_by_visible_text('1980')

state = Select(browser.find_element_by_id('state'))
state.select_by_visible_text('Alabama')

browser.find_element_by_css_selector('#sumlevel > div:nth-child(2) > label').click()

browser.find_element_by_css_selector('#launch > input[type="button"]').click()

time.sleep(10)

browser.find_element_by_css_selector('#results > p:nth-child(2) > a:nth-child(4)').click()
