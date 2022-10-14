---
label: DAVENGERS
icon: home
---
# DAVENGERS


[!button variant="primary" text="[수행 과제1] 여행 관련 탄소발자국 계산기 구축"](../web/carbon/readme.md)

[!button variant="primary" text="[수행 과제2] 친환경 제주여행 루트 추천 시스템 구축과 팁 제안"](../web/recsys/readme.md)

# [빅콘테스트 이노베이션리그] 탄소 발자국 계산기 구축 & 제주도 여행 추천 시스템 개발 (데벤저스 DAVENGERS)

## Project Description
> '제10회 2022 빅콘테스트 이노베이션분야 이노베이션부문 출품작' MZ세대가 떠나는 친환경 ESG 제주여행 루트짜기


## Project Information
- [수행 과제1] 여행 관련 탄소발자국 계산기 구축
- [수행 과제2] 친환경 제주여행 루트 추천 시스템 구축과 팁 제안
- [수행 과제3] 대고객 커뮤니케이션 방안 도출

## Project Result
- [수행 과제1] 여행 관련 탄소발자국 계산기 구축
    - [탄소 발자국 계산기 [링크]](https://underthelights-davengers-codecalccalc-8i6c7h.streamlitapp.com/)
    - ![flight](https://user-images.githubusercontent.com/46957634/195742249-86ae2aae-00c5-4f95-a50d-91c838538663.gif)

- [수행 과제2] 친환경 제주여행 루트 추천 시스템 구축과 팁 제안
    - [취향 저격 Hexagon [링크]](https://underthelights-recommend-tour-input-recommend-input-k4wcm6.streamlitapp.com/)
    - ![whole-hexagon](https://user-images.githubusercontent.com/46957634/195742267-78b2e5c1-abc3-45ff-8b59-4b2d77c97429.gif)

## Project Details
### 탄소 발자국 계산기 구축
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

### 친환경 제주여행 루트 추천 시스템 구축과 팁 제안
- 대학생 3인이 봄·가을에 떠나는 3박4일 친환경 제주여행 루트 설계 완료
    - 출발지 자유 (제주공항 도착 이후)
    - 숙박 필수 (3박)
    - 음식 업종 : 하루 최소 2회
    - 교통 수단 : 하루 최소 2회
    - 제주관광공사 추천 여행지 필수방문
- 배포 (여행자 취향저격 Hexagon) : [[링크]](https://underthelights-recommend-tour-input-recommend-input-k4wcm6.streamlitapp.com)
- 관광지별 지표 점수 계산 (NLP, Word2Vec, t-SNE, Clustering을 통한 Scoring 구현) : [[Colaboratory 링크]](https://colab.research.google.com/drive/1nz9uJD4KzHHdwAb8Lu0sHDP89Q2ofyvz?usp=sharing), [[GitHub 링크]](https://github.com/underthelights/DAVENGERS/blob/main/관광지별_지표_점수_계산.ipynb)
- 여행자 친환경 제주여행 루트 추천 알고리즘 구현 (JEJU_ASSEMBLE) : [[GitHub 링크]](https://github.com/underthelights/DAVENGERS/blob/main/code/rec/jeju_assemble/JEJU_ASSEMBLE.ipynb)
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


## Authors
> 데벤저스 at [Sogang U. INSIGHT](https://insightsg.notion.site/INSIGHT-Sogang-Univ-f5e18d99663c4f47a767dbe29d5ec170) : Sogang Business Big Data Analysis Study Academy

- 하정현 ([@jeonghyunhaaa](https://github.com/jeonghyunhaaa)) 경영학 & 빅데이터사이언스 학사과정, 서강대학교
- 나경훈 ([@rudgnsdl06](https://github.com/rudgnsdl06)) 수학 & 빅데이터사이언스 학사과정, 서강대학교
- 고경주 ([@gingzuu](https://github.com/gingzuu)) 경영학 & 빅데이터사이언스 학사과정, 서강대학교
- 정혜나 ([@77hannah77](https://github.com/77hannah77)) 경영학 & 컴퓨터공학 학사과정, 서강대학교
- 심규환 ([@underthelights](https://github.com/underthelights)) 컴퓨터공학 학사과정, 서강대학교