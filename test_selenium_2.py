from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Cargamos el driver Firefox
driver = webdriver.Firefox()
driver.get("http://localhost/prepara_pedido.html")
assert "Pizzas Full Stack" in driver.title
# Buscamos el elemento nombre y lo cumplimemtamos
elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nombre")))
elem.clear()
elem.send_keys("Pedro")
elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "enviar")))
#elem = driver.find_element_by_id("enviar")
elem.click()
# Damos una pausa para que la web se ejecute
time.sleep(1)
# No hemos cmplimentado los apellidos, testeamos que se colorea en rojo
elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "labelApellidos")))
#elem = driver.find_element_by_id("apellidos")
color = elem.value_of_css_property("color")
assert color == "rgb(255, 0, 0)"
# Cerramos el driver Firefox
driver.close()
