from selenium import webdriver
from pathlib import Path
from time import sleep


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument('start-fullscreen')

driver = webdriver.Chrome( options=options ,executable_path= Path.cwd() / 'chromedriver')

while True:
    driver.get("http://form10dash.herokuapp.com/")
    sleep(120)
    driver.get('https://www.accuweather.com/en/us/tampa/33602/weather-forecast/347937')
    sleep(120)
    driver.get('https://form10.com/')
    sleep(120)
    driver.get('http://form10dash.herokuapp.com/applus')
    sleep(120)
    driver.get('https://form10.com/about-us')
    sleep(120)
    driver.get('https://form10.com/our-services')
    sleep(120)
    driver.get('https://form10.com/')
    sleep(120)