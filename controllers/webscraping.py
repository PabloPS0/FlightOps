import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuração do ChromeDriver com a opção 'detach'
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Evita que o navegador feche automaticamente

driver = webdriver.Chrome()

# Acesse a página de login
driver.get("https://www.airlines-manager.com/")

# Aumente o tempo de espera e use o 'clickable' para garantir que o campo de e-mail seja clicável
wait = WebDriverWait(driver, 300)  # Espera até 5 segundos

email_field = driver.find_element(By.NAME, "_username")  # ou outro método de localização
password_field = driver.find_element(By.NAME, "_password") # ou use XPath se necessário

# Preencha os campos de login
email_field.send_keys("mastergames268@gmail.com")
password_field.send_keys("LP020221$")

password_field.send_keys(Keys.RETURN)

# Aguarde a página carregar após o login (pode ser um link ou elemento de página)
wait.until(EC.presence_of_element_located((By.ID, "loaderBox_row")))

popup_initial = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "word-of-day-popup")))
image_close = driver.find_element(By.CSS_SELECTOR, "img[src='/images/staff/iata/IATA_POPUP_close.png']")
image_close.click()

time.sleep(2)

alliance = wait.until(EC.presence_of_element_located((By.ID, "pictoAlliance")))
alliance.click()

time.sleep(2)

# alliance_accounting = driver.find_element(By.XPATH, '//*[contains(@href, "https://tycoon.airlines-manager.com/alliance/accounting")]')
alliance_accounting = driver.find_element(By.XPATH, '//*[@id="catMenu"]/a[2]/img')
alliance_accounting.click()

time.sleep(2)

# O navegador continuará aberto após o código terminar
print("Teste completo!")
