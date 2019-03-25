from selenium import webdriver
import sys, os
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

browser.find