from selenium import webdriver
import time

# 1. Chrome 브라우저 실행
driver = webdriver.Chrome('chromedriver')

# 2. 파파고 사이트에 접속 (자동번역 해제)
driver.get('https://papago.naver.com/')

time.sleep(1)

auto_complete_btn = driver.find_element_by_css_selector('#sourceEditArea > label')
auto_complete_btn.click()

time.sleep(1)

# 3. 입력창 지정 후 '안녕하세요' 입력
input_area = driver.find_element_by_css_selector('textarea#txtSource')
input_area.send_keys('안녕하세요')

# 4. '번역하기' 버튼 클릭
translation_btn = driver.find_element_by_css_selector('button#btnTranslate')
translation_btn.click()

time.sleep(1)

# 5. 번역된 결과 출력
output_area = driver.find_element_by_css_selector('div#txtTarget').text
print(output_area)

time.sleep(3)

driver.close()