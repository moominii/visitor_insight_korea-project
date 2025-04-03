# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 16:28:21 2025

@author: Jiyeon Baek
과제
메가MGC커피 : https://www.mega-mgccoffee.com/

매장수와 한국인 인구수 비교
매장수와 외국인 인구수 비교
매장수와 업종별 종사자수 비교
=> 업종별 : 상위 5개 업종
"""

# 1.1 크롤링을 이용한 서울시 메가커피 매장 목록 데이터 생성
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time 

driver = webdriver.Chrome()
url = "https://www.mega-mgccoffee.com/store/find/"
driver.get(url)
time.sleep(3)

### webdriver로 ‘서울’ 버튼 요소를 찾아 클릭
# 1. '전체' 버튼 요소를 찾아
local_btn = 'body > div.wrap > div.cont_wrap.find_wrap > div > div.cont_box.find01 > div.map_search_wrap > div > div.cont_text_wrap.map_search_tab_wrap > div > ul > li:nth-child(2)'
driver.find_element('css selector', local_btn).click()
time.sleep(2)

# 2. '서울' 버튼
seoul_btn = '#store_area_search_list > li:nth-child(1)'
driver.find_element('css selector', seoul_btn).click()
time.sleep(2)


# 3. 강남구부터 마지막 구까지 클릭 (2 ~ 27)
for i in range(2, 27):
    district_btn = f"#store_area_search_list_result > li:nth-child({i})"
    try:
        driver.find_element('css selector', district_btn).click()
        time.sleep(2)  # 클릭 후 대기
    except:
        pass


# BeautifulSoup으로 HTML 파서 만들기
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 매장 정보 가져오기
mega_soup_list = soup.select("ul.store_list > li")
print(len(mega_soup_list))

# 데이터 저장 리스트
mega_list = []






















