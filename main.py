from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep




chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chromeOptions)
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3783187418&distance=25&f_AL=true&geoId=104744733&keywords=Python%20Developer&location=Kolkata&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R')

email = "pritishmajumdar066@gmail.com"
passw = "9732sanu"
sleep(2)
signin_btn = driver.find_element(By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')
signin_btn.click()
sleep(2)


email_field = driver.find_element(By.XPATH,value='//*[@id="username"]')
email_field.send_keys(email)

pass_field = driver.find_element(By.XPATH,value='//*[@id="password"]')
pass_field.send_keys(passw)

fin_sign = driver.find_element(By.XPATH,value='//*[@id="organic-div"]/form/div[3]/button')
fin_sign.click()


save_job = driver.find_element(By.XPATH,value='//*[@id="main"]/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/button')
save_job.click()

