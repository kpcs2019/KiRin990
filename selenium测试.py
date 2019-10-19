from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
  
driver = webdriver.Ie()  
driver.get("https://www.baidu.com")  
assert "Python" in driver.title  
print(driver.page_source)  
elem = driver.find_element_by_name("q")  
elem.send_keys("pyconect")  
elem.send_keys(Keys.RETURN)  
assert "No result found." not in driver.page_source  
driver.close() 