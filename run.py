    # 교육부 건강상태 자가진단 시스템 / 학생자가진단 시스템
    # 해당 소스를 사용하실려면 아래 모듈을 설치해주세요
    # pip install selenium
    # 해당 시스템은 학교검색에 첫번쩨 학교만 할 수 있습니다.
    # 추후 업데이트 해드리겠습니다!
    # 자유롭게 사용이 가능하며 블로그, 카페, 페이스북, SNS 등등 소스코드 업로드, 리뷰 목적 사용 시에는 꼭 GitHub링크 남겨주세요!
    # https://github.com/MeatRoast
    # !!! 본 코드의 라이선스는 MeatRoast 에게 있습니다 !!!
    # 해당 레포지토리 : https://github.com/MeatRoast/health-condition-self-check-Auto-system

import time, datetime
from selenium import webdriver
from datetime import datetime



def task():
    city = a
    level = b
    school = c
    named = d
    bh = e
    pw = f
    # 해당 변수의 사용법은 원본 레포지토리를 확인해주세요
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument("disable-gpu")
    bb = webdriver.Chrome(executable_path="크롬드라이브 경로", options=options) # !!! 이 친구도 수정 해야 함 !!!
    bb.get("https://hcs.eduro.go.kr/#/loginHome") # 웹 사이트 접속 
    bb.find_element_by_id("btnConfirm2").click() # 자가진단하기 클릭
    bb.find_element_by_xpath('//*[@id="schul_name_input"]').click() #학교찾기 클릭
    bb.find_element_by_xpath(f'//*[@id="sidolabel"]/option[{city}]').click() # 시/도 선택
    bb.find_element_by_xpath(f'//*[@id="crseScCode"]/option[{level}]').click() #유초중고특 선택
    bb.find_element_by_id('orgname').send_keys(school) # 학교명 입력
    bb.implicitly_wait(0.5)
    bb.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').click() #해당 학교 검색
    bb.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul').click() # 첫번쩨에 있는 학교 불러오기
    bb.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a').click() # 학교 선택하기
    bb.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click() # 이름 입력하기 클릭
    bb.find_element_by_xpath('//*[@id="user_name_input"]').send_keys(named) # 이름 입력
    bb.find_element_by_xpath('//*[@id="birthday_input"]').send_keys(bh) # 생년월일 입력
    bb.find_element_by_xpath('//*[@id="btnConfirm"]').click() # 확인 클릭
    print('학교 통과 완료')
    time.sleep(0.5)
    bb.find_element_by_id('container') # 해당 id 찾기
    bb.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr/td/input').send_keys(pw) # 페스워드 입력
    time.sleep(1)
    bb.find_element_by_xpath('//*[@id="btnConfirm"]').click() #확인하기 클릭
    print('페스워드 입력완료')
    time.sleep(1)
    bb.find_element_by_xpath('//*[@id="container"]/div/section[2]/div[2]/ul/li/a/em').click() # 확인 클릭
    bb.find_element_by_xpath('//*[@id="survey_q1a1"]').click() # 자가진단 아니요 클릭
    bb.find_element_by_xpath('//*[@id="survey_q2a1"]').click() # 자가진단 아니요 클릭
    bb.find_element_by_xpath('//*[@id="survey_q3a1"]').click() # 자가진단 아니요 클릭
    bb.find_element_by_xpath('//*[@id="btnConfirm"]').click() # 확인 클릭
    name = bb.find_element_by_xpath('//*[@id="container"]/div/div[2]/div[1]/p[1]').text # 이름/학교명 텍스트 변화
    day = bb.find_element_by_xpath('//*[@id="container"]/div/div[2]/div[1]/p[2]').text # 자가진단 일시 날짜 참여 상태 텍스트 변화
    te = bb.find_element_by_xpath('//*[@id="container"]/div/div[2]/div[2]/p').text # 등교 가능 여부 텍스트 변화
    print(f'{name}') # name값 출력
    print(f'{day}') # day값 출력
    print(f'{te}') # te값 출력
    print('자가진단 완료')

while(True):
    try:
        date = datetime.now()
        print(date.hour, date.minute, date.second)
        if date.hour == 6 
            print("True")
            task()
            time.sleep(3650)
        else:
            print("False")
            time.sleep(1)
    except KeyboardInterrupt:
        print("종료됨")
        exit()
