from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = 'https://www.thesun.co.uk/sport/football/'
path = "C:\Program Files (x86)\chromedriver.exe"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)
