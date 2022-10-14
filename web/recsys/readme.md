---
excerpt: "recsys"
slug: "recsys"

category: "recsys"
lang: en
tags: ["recsys"]
date: 2022-10-14
draft: false
---

# [수행 과제2] 친환경 제주여행 루트 추천 시스템 구축과 팁 제안
[!button target="blank" text="친환경 제주여행 루트 추천 시스템 구축과 팁 제안"](https://underthelights-recommend-tour-input-recommend-input-k4wcm6.streamlitapp.com/)
- [취향 저격 Hexagon [링크]](https://underthelights-recommend-tour-input-recommend-input-k4wcm6.streamlitapp.com/)
    - ![whole-hexagon](https://user-images.githubusercontent.com/46957634/195742267-78b2e5c1-abc3-45ff-8b59-4b2d77c97429.gif)
- 대학생 3인이 봄·가을에 떠나는 3박4일 친환경 제주여행 루트 추천 시스템 구축과 팁 제안
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