from selenium import webdriver
import time
# from selenium.webdriver.chrome.options import Options

# options = Options()
# options.binary_location = r"C:\Program Files (x86)\Naver\Naver Whale\Application\whale.exe"
#
#

# driver = webdriver.Chrome(chrome_options=options, executable_path= 'chromedriver')
driver = webdriver.Chrome(executable_path= 'chromedriver')
driver.get('https://papago.naver.com/')

time.sleep(5)

driver.close()