from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

f = open("../../info.txt", "r")
secret1 = f.readline().strip()
secret2 = f.readline().strip()
f.close()

class ClockOut:
  def __init__(self, email, password):
    self.email = email
    self.password = password

  def run(self):
    PATH = "../../chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://megapayusa.myfileguardian.com/PostOffice/Main.aspx")

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME,"postOfficeSignIn"))).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID,"txtEmail"))).send_keys(self.email)

    # must click on body to refresh page and find password field by id
    driver.find_element_by_xpath("//body").click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID,"txtPassword"))).send_keys(self.password)

    driver.find_element_by_id("ctl00_ctl00_holderMain_holderMain_btnSignIn").click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "hub-master")))
    driver.switch_to.frame(driver.find_element_by_id("ifrWebClock"))
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID,"ClockOut"))).click()

clockout = ClockOut(secret1, secret2)
clockout.run()