from selenium import webdriver
import time

#Cargamos el driver del navegador
driver = webdriver.Firefox()
driver.get("http://www.google.es")
assert "Google" in driver.title

#cerramos el driver
driver.close()