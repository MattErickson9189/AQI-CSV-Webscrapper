from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import os
import time
import shutil

browser = webdriver.Firefox()

URL = "https://www.epa.gov/outdoor-air-quality-data/air-quality-statistics-report"
path = "./Data/"
downloads = '/home/matt/Downloads/'
#Array to store the desired dates
#dates = ["1980","1985","1990","1995","2000","2005","2010","2015","2019"]
#dates = ["1981","1982","1983","1984","1986","1987","1988","1989","1991","1992","1993","1994","1996","1997","1998","1999"]
dates = years = ["1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000"]
timeout = 10

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

for i in range(len(dates)):
    year = Select(browser.find_element_by_id('year'))
    year.select_by_visible_text(dates[i])
    time.sleep(6)
    for j in range(50):

        try:
            state = Select(browser.find_element_by_id('state'))
            state.select_by_visible_text(states[j])


            time.sleep(4)
            try:
                browser.find_element_by_css_selector('#sumlevel > div:nth-child(2) > label').click()
            except Exception:
                print("Trying Again")
                time.sleep(5)
                browser.find_element_by_css_selector('#sumlevel > div:nth-child(2) > label').click()

            time.sleep(4)
            try:
                browser.find_element_by_css_selector('#launch > input[type="button"]').click()
            except Exception:
                print("Trying Again")
                time.sleep(5)
                browser.find_element_by_css_selector('#launch > input[type="button"]').click()

            time.sleep(10)
            try:
                browser.find_element_by_css_selector('#results > p:nth-child(2) > a:nth-child(4)').click()
            except Exception:
                print("Trying again")
                time.sleep(5)
                browser.find_element_by_css_selector('#results > p:nth-child(2) > a:nth-child(4)').click()

            if not os.path.exists(path + dates[i] + '/'):
                os.mkdir(path + dates[i] + '/')

            destPath = path + dates[i] + '/' + states[j] + dates[i] + ".csv"
            srcPath = downloads + 'conreport' + dates[i] + '.csv'
            #Moves the file
            time.sleep(2)
            shutil.move(srcPath,destPath)
        except Exception:
            print("Something went wrong...Trying again")
            j -= 1