import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import requests
import re
import pymysql

connect = pymysql.connect(host="13.125.242.115", user="root", password="rootroot", db="skku_calender", charset='utf8mb4')
cursor = connect.cursor()

### 테이블을 생성하는 코드 ###
# cursor.execute(
#     "CREATE TABLE " + table_name + "(name_kor varchar(10), belong varchar(30), major mediumtext, education mediumtext, career mediumtext, link mediumtext, hospital_code varchar(6));")
# connect.commit()

# 테이블을 생성합니다.
# cursor.execute('DROP TABLE IF EXISTS drinks')

# # 테이블 구조를 만듭니다.
# # id에 auto_increment를 추가하여 자동으로 생성되며 기본키로 지정했습니다.
# cursor.execute('''
#     CREATE TABLE drinks(
#     id MEDIUMINT AUTO_INCREMENT PRIMARY KEY,
#     drink_name VARCHAR(50),
#     main VARCHAR(30),
#     amount1 DEC(4,2),
#     second VARCHAR(30),
#     amount2 DEC(4,2),
#     directions VARCHAR(100))
# ''')

raw=requests.get("https://www.skku.edu/skku/edu/bachelor/ca_de_schedule.do")
html=BeautifulSoup(raw.text,"html.parser")
container=html.select_one("textarea").text

jsonObject = json.loads(container)

for i in range(1,13,1):
    dict_temp=eval(str(jsonObject['bachelor_'+str(i)][0]).replace("\'","\""))
    # 몇 번째 요소인지
    num=1
    for attribute in dict_temp:
        print(attribute) # example usage
        print(dict_temp[attribute])

        if(attribute[:2]=="sd"):
            startdate=dict_temp[attribute]
            if(startdate==""):
                startdate=None
        elif(attribute[:2]=="ed"):
            enddate=dict_temp[attribute]
            if(enddate==""):
                enddate=startdate
        elif(attribute[:2]=="co"):
            postname=dict_temp[attribute]
        else:
            break
        if(num%3==0):
            # 3의 배수일때, 다 채웠을 때
            # post_id, user_id, nickname, post_name, start_date,end_date, place,link, memo, alarm, alarm_time, color
            cursor.execute("INSERT INTO post_schedule (user_id,nickname, post_name, start_date,end_date, color) values (%s,%s, %s, %s, %s, %s);",("0","public",postname,startdate,enddate,"green"))
            connect.commit()
        num=num+1
connect.close()

