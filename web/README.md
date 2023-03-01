---
label: DAVENGERS
icon: home
---
# DAVENGERS


[!button variant="primary" text="[수행 과제1] 여행 관련 탄소발자국 계산기 구축"](../web/carbon/readme.md)

[!button variant="primary" text="[수행 과제2] 친환경 제주여행 루트 추천 시스템 구축과 팁 제안"](../web/recsys/readme.md)

<<<<<<< HEAD
# [빅콘테스트 이노베이션리그] 탄소 발자국 계산기 구축 & 제주도 여행 추천 시스템 개발 (데벤져스 DAVENGERS)

## Project Description
> '제10회 2022 빅콘테스트 이노베이션분야 이노베이션부문 최우수상 (전체 2위, 한국지능정보사회진흥원장상)' MZ세대가 떠나는 친환경 ESG 제주여행 루트짜기
-   [상장 링크](https://drive.google.com/file/d/151VNDxsmgUTVG-jY-S0Un1kOCpXDBjil/view)
- [[서강피플] 
‘데벤져스’팀, ‘제10회 2022 빅콘테스트’ 데이터분석리그 이노베이션 분야 최우수상(한국지능정보사회진흥원장상) 수상](https://www.sogang.ac.kr/gopage/goboard2.jsp?bbsConfigFK=58&pkid=536220)
=======
# [빅콘테스트 이노베이션리그] 탄소 발자국 계산기 구축 & 제주도 여행 추천 시스템 개발 (데벤저스 DAVENGERS)

## Project Description
> '제10회 2022 빅콘테스트 이노베이션분야 이노베이션부문 출품작' MZ세대가 떠나는 친환경 ESG 제주여행 루트짜기

>>>>>>> e45ca3c23602732d17aae3c7080cd86fc63b4e30

## Project Information
- [수행 과제1] 여행 관련 탄소발자국 계산기 구축
- [수행 과제2] 친환경 제주여행 루트 추천 시스템 구축과 팁 제안
- [수행 과제3] 대고객 커뮤니케이션 방안 도출

## Project Result
- [수행 과제1] 여행 관련 탄소발자국 계산기 구축
    - [탄소 발자국 계산기 [링크]](https://underthelights-davengers-codecalccalc-8i6c7h.streamlitapp.com/)
    - ![flight](https://user-images.githubusercontent.com/46957634/195742249-86ae2aae-00c5-4f95-a50d-91c838538663.gif)

<<<<<<< HEAD
- [수행 과제2] 친환경 제주여행 루트와 팁 제안
=======
- [수행 과제2] 친환경 제주여행 루트 추천 시스템 구축과 팁 제안
>>>>>>> e45ca3c23602732d17aae3c7080cd86fc63b4e30
    - [취향 저격 Hexagon [링크]](https://underthelights-recommend-tour-input-recommend-input-k4wcm6.streamlitapp.com/)
    - ![whole-hexagon](https://user-images.githubusercontent.com/46957634/195742267-78b2e5c1-abc3-45ff-8b59-4b2d77c97429.gif)

## Project Details
<<<<<<< HEAD
### [탄소 발자국 계산기 구축](https://underthelights.github.io/DAVENGERS/carbon-footprint/)
=======
### 탄소 발자국 계산기 구축
>>>>>>> e45ca3c23602732d17aae3c7080cd86fc63b4e30
- (과제1) 여행 영역별 탄소발자국 계산기 구축 완료
    - 교통/교통업 (traffic)
    - 음식/요식업 (food)
    - 숙소/숙박업 (accomodation)
    - 관광/관광업 (tourism)
- 배포 (탄소 발자국 계산기) : [[링크]](https://underthelights-davengers-codecalccalc-8i6c7h.streamlitapp.com)

- 탄소 발자국 계산기 (종합)
    ```
    streamlit run code/calc/calc.py
    ```
- 탄소 발자국 계산기 (숙소)
    ```
    streamlit run code/calc/accom.py
    ```
- 탄소 발자국 계산기 (음식)
    ```
    streamlit run code/calc/food.py
    ```
- 탄소 발자국 계산기 (관광지)
    ```
    streamlit run code/calc/tourism.py
    ```

<<<<<<< HEAD
### [친환경 제주여행 루트 추천 시스템 구축과 팁 제안](https://underthelights.github.io/DAVENGERS/recsys/)
=======
### 친환경 제주여행 루트 추천 시스템 구축과 팁 제안
>>>>>>> e45ca3c23602732d17aae3c7080cd86fc63b4e30
- 대학생 3인이 봄·가을에 떠나는 3박4일 친환경 제주여행 루트 설계 완료
    - 출발지 자유 (제주공항 도착 이후)
    - 숙박 필수 (3박)
    - 음식 업종 : 하루 최소 2회
    - 교통 수단 : 하루 최소 2회
<<<<<<< HEAD
    - 제주관광공사 유형별 추천 여행지 필수방문 : 
        - 관광지 : 자연 관련 2곳 이상, 액티비티성 활동 1곳 이상 
        - 음식점 : 2곳 이상
        - 숙박 : 1곳 이상
- 배포 (여행자 취향저격 Hexagon) : [[링크]](https://underthelights-recommend-tour-input-recommend-input-k4wcm6.streamlitapp.com)
- 관광지별 지표 점수 계산 (NLP, Word2Vec, t-SNE, Clustering을 통한 Scoring 구현) : [[Colaboratory 링크]](https://colab.research.google.com/drive/1nz9uJD4KzHHdwAb8Lu0sHDP89Q2ofyvz?usp=sharing), [[GitHub 링크]](https://github.com/underthelights/DAVENGERS/blob/main/관광지별_지표_점수_계산.ipynb)
- 여행자 친환경 제주여행 루트 추천 알고리즘 구현 (JEJU_ASSEMBLE) : [[GitHub Gist 링크]](https://gist.github.com/underthelights/723361b1c00249e0c193bb7fbd896c46)
=======
    - 제주관광공사 추천 여행지 필수방문
- 배포 (여행자 취향저격 Hexagon) : [[링크]](https://underthelights-recommend-tour-input-recommend-input-k4wcm6.streamlitapp.com)
- 관광지별 지표 점수 계산 (NLP, Word2Vec, t-SNE, Clustering을 통한 Scoring 구현) : [[Colaboratory 링크]](https://colab.research.google.com/drive/1nz9uJD4KzHHdwAb8Lu0sHDP89Q2ofyvz?usp=sharing), [[GitHub 링크]](https://github.com/underthelights/DAVENGERS/blob/main/관광지별_지표_점수_계산.ipynb)
- 여행자 친환경 제주여행 루트 추천 알고리즘 구현 (JEJU_ASSEMBLE) : [[GitHub Gist 링크]](https://gist.github.com/underthelights/723361b1c00249e0c193bb7fbd896c46)

"https://gist.github.com/underthelights/723361b1c00249e0c193bb7fbd896c46.js"

>>>>>>> e45ca3c23602732d17aae3c7080cd86fc63b4e30
    ``` 
    사용자 선호도 점수 : 자연 선호 (purpose1), 액티비티 선호 (purpose2), 문화유적 선호 (purpose3)
    - 0에서 1 사이의 실수

    핫플 선호도 점수 (popularity)
    - 0에서 1 사이의 실수

    여행 밀도 점수 (bbak)
    - 0에서 1 사이의 실수
    
    맛집 추구 점수 (bab)
    - 0에서 1 사이의 실수
    
    교통 수단 (car)
    - 0 또는 1 (정수)

    해당 날짜에 여행할 지역 : day1~day4, day속성
    - day속성에 따른 sequence로 정의
    - 각 권역별 넘버링에 따른 day1~day4 값
    ```

## 기술 스택
- Main Language : Python
- Most Used Python Library : [Pandas](https://pandas.pydata.org/), [Streamlit](https://streamlit.io), [Matplotlib](https://matplotlib.org/), [Plotly](https://plotly.com/python/), [Seaborn](https://seaborn.pydata.org/), [NumPy](https://numpy.org/), [GeoPy](https://geopy.readthedocs.io/en/stable/)
- Main Develop Environment : Jupyter Notebook, Google Colaboratory (Windows 10, Mac OS X)
- Deployment : [Streamlit Sharing](https://streamlit.io)


<<<<<<< HEAD
## Authors : 데벤져스 DAVENGERS
- 서강대학교 경영대학 경영데이터분석학회 ["INSIGHT"](https://insight.oopy.io) 소속 프로젝트 팀
![DAVENGERS](https://www.sogang.ac.kr/dataview/board/58/20230119_1730_2710001.jpg)

### 고경주
- 서강대학교 경영학 & 빅데이터사이언스 학사과정 
- GitHub : [@gingzuu](https://github.com/gingzuu)

### 나경훈
- 서강대학교 수학 & 빅데이터사이언스 학사과정 
- GitHub : [@rudgnsdl06](https://github.com/rudgnsdl06)

### 심규환
- 서강대학교 컴퓨터공학 학사과정 
- GitHub : [@underthelights](https://github.com/underthelights)

### 정혜나
- 서강대학교 경영학 & 컴퓨터공학 학사과정 
- GitHub : [@77hannah77](https://github.com/77hannah77)

### 하정현 (팀장)
- 서강대학교 경영학 & 빅데이터사이언스 학사과정 
- GitHub : [@jeonghyunhaaa](https://github.com/jeonghyunhaaa)

## 프로젝트 수행 일정 요약
- 2022년 09월 19일 ~ 09월 23일 : 
    - 프로젝트 소개자료 분석
    - 브레인스토밍
    - 내부 데이터 수집 및 정제
    - 데이터 EDA 진행
- 2022년 09월 24일 ~ 10월 4일 : 
    - 탄소 발자국 계산기 구축을 위한 데이터 수집 (크롤링 등)
    - 여행 분야별 로직 설계
    - 탄소 발자국 계산기 구축 
- 2022년 10월 5일 ~ 10월 9일 : 
    - 탄소 발자국 계산기 프로토타입 구현
    - 친환경 제주여행 루트 추천 알고리즘 아이디에이션
    - 추가 데이터 크롤링 (비짓제주, 네이버 지도 등)
    - 대고객 커뮤니케이션 관련 아이디에이션 
- 2022년 10월 10일 ~ 10월 14일 : 
    - 탄소 발자국 계산기 일부 로직 수정
    - 친환경 제주여행 루트 추천 알고리즘 구현 및 수정
    - 발표 자료 제작 및 완성
=======
## Authors
> 데벤저스 

- 하정현
- 나경훈
- 고경주
- 정혜나
- 심규환
>>>>>>> e45ca3c23602732d17aae3c7080cd86fc63b4e30
