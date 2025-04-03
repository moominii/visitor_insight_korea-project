# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 04:24:08 2025

@author: Jiyeon Baek
"""

import pandas as pd
import folium
import json

# 통계 데이터 불러오기
seoul_sgg_stat = pd.read_excel('C:/Users/Admin/Desktop/JY/Python/20250219/starbucks_location/files/seoul_sgg_stat.xlsx', 
                               thousands=',')

# 시군구 행정 경계 지도 파일
sgg_geojson_file_path = 'C:/Users/Admin/Desktop/JY/Python/20250219/starbucks_location/maps/seoul_sgg.geojson'
seoul_sgg_geo = json.load(open(sgg_geojson_file_path, encoding = 'utf-8'))

# 주민등록인구수 단계구분도 지도 시각화
starbucks_choropleth = folium.Map(location=[37.573050, 126.979189],
                              tiles = 'CartoDB dark_matter',
                              zoom_start=11)

folium.Choropleth(geo_data=seoul_sgg_geo,
                  data = seoul_sgg_stat,
                  columns=['시군구명', '주민등록인구'],
                  fill_color = 'YlGn',
                  fill_opacity=0.7,
                  line_opacity=0.5,
                  key_on = 'properties.SIG_KOR_NM'
                  ).add_to(starbucks_choropleth)

starbucks_choropleth.save('starbucks_choropleth_pop.html')



# 사업체 수 단계구분도 지도 시각화
starbucks_choropleth = folium.Map(location=[37.573050, 126.979189],
                              tiles = 'CartoDB dark_matter',
                              zoom_start=11)

folium.Choropleth(geo_data=seoul_sgg_geo,
                  data = seoul_sgg_stat,
                  columns=['시군구명', '사업체수_x'],
                  fill_color = 'YlGn',
                  fill_opacity=0.7,
                  line_opacity=0.5,
                  key_on = 'properties.SIG_KOR_NM'
                  ).add_to(starbucks_choropleth)

starbucks_choropleth.save('starbucks_choropleth_biz.html')


# 인구 만 명당 스타벅스 매장 수 지도 시각화
seoul_sgg_stat['인구 만 명당 스타벅스 수'] = seoul_sgg_stat['스타벅스_매장수'] / (seoul_sgg_stat['주민등록인구'] / 10000)

# **2. 지도 시각화**
starbucks_choropleth = folium.Map(location=[37.573050, 126.979189],
                              tiles='CartoDB dark_matter',
                              zoom_start=11)

folium.Choropleth(
    geo_data=seoul_sgg_geo,
    data=seoul_sgg_stat,
    columns=['시군구명', '인구 만 명당 스타벅스 수'],
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.5,
    key_on='properties.SIG_KOR_NM'
).add_to(starbucks_choropleth)


starbucks_choropleth.save('starbucks_choropleth_stores_per_10k.html')

































