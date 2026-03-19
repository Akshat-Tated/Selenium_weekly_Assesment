from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.maximize_window()

driver.get("https://www.facebook.com")

driver.find_element(By.CSS_SELECTOR, "input#R_1h6kqsqppb6amH1").send_keys("Akshat")
driver.find_element(By.CSS_SELECTOR, "input#R_1hmkqsqppb6amH1").send_keys("123")
driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Log in"').click()






