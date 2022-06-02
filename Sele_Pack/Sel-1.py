
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s=Service(executable_path="c:\\chromedriver.exe")
driver = webdriver.Chrome(service=s)


driver.maximize_window()
driver.get("http://www.amazon.in")
driver.implicitly_wait(10)
driver.find_element(By.XPATH("//input[span@id , 'nav-link-accountList-nav-line-1']")).click()
#st=driver.find_element(By.XPATH("//span[@id='nav-link-accountList-nav-line-1']"))
st.click()
#driver.find_element(By.XPATH("//input[@id = 'twotabsearchtextbox']")).send_keys("Mobiles")
driver.quit()



'''
#syntax for ID
driver.find_element(By.ID,"twotabsearchtextbox").send_keys('Mobiles')
#syntax for Name is:
driver.find_element(By.NAME," ")

#syntax for Class_Name  we will find class tag in web page

driver.find_element(By.CLASS_NAME,"")

#Syntax for Link Text its usually present as text between tags <a ,href a>
driver.find_element(By.LINK_TEXT,"")

#Syntax for Partial Link Text

driver.find_element(By.PARTIAL_LINK_TEXT,"")
#Syntax for Css Selector is:

driver.find_element(By.CSS_SELECTOR, "")

//input[@id=]'''


driver.implicitly_wait(10)

