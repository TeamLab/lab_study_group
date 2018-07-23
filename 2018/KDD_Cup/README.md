#  KDD Cup 2018 Competition
- Purpose of the repoistory
  - Master Students will learn to analyze time series data by participating in KDD CUP Conference and enhance coding capabilities.
- Competition source
  - [KDD CUP of Fresh Air - 2018](https://biendata.com/competition/kdd_2018/)

###  Competition theme
- 이 대회의 주제는 기상 자료에 기초하여 5월에 두 도시의 대기 오염 수준을 예측하는 것이다. 이 두 도시 중 한 도시는 베이징이며 다른 한 도시는 영국 런던이다.
- 주최자는 지난 1년 동안의 두 도시의 기상 데이터를 제공하고 분석자는 베이징도시에는 PM2.5, PM10, O3(오존)를, 런던은 PM2.5, PM10 을 예측해야한다. 4월 30일 까지 주최측에서 지속적으로 제공해주는 데이터를 바탕으로 모델링을 하고 5월 1일 부터 다음날 과 다다음날인 향후 48시간의 대기오염 수준을 5월 31일 까지 매일매일 예측한다.

### Contest Rules
- 총 10 개의 대회규칙이 제시되어 있으며 가장 눈여겨 보아야할 사항은 7번 사항임
- 실제로 주최측에서 제공되는 기상데이터에는 상당히 많은 결측치가 존재함
- 더 나은 예측값을 제시하기 위해서는 외부데이터를 활용하는 방안이 필요
- 실제로 PM10 같은 경우 데이터의 3분의 1 이상이 결측치인 만큼 결측치 추정에는 제한사항이 많음

#### Reference - the rule from the competition
1. All participants must register in competition platform.
2. Participants can choose to form teams on the platform. Each team much consist no more than 10 members.
3. Each team appoints a leader and selects a team title of no more than 15 characters.
4. Each participant can join only one team. Multiple accounts will lead to disqualification of all teams joined by the participant.
5. Teams are allowed to combine before the team merge deadline but teams may not split. Combined teams must consist of no more than ten members.
6. Participants are allowed to use open-source codes or tools but are not permitted to use any code or tools that have not been publicly released or authorized.
7. *External data is allowed to use for this competition. However, using external data has to satisfy the following criteria:<br> The external data has to be publicly accessible. You have to post in the competition forum before April 30th on how to access the external data, and provide sample codes in Python. After April 30th, no new external data can be used.*
8. Privately sharing code or data outside of teams is not allowed
9. Teams can submit their prediction results anytime during the completion up to three times a day.
10. The competition organizers reserve the right to update the competition timeline if they deem it necessary.

###  Data
총 2개의 csv 파일이 제공되며 공기질 데이터와 기상 데이터가 제공된다.
- Air Quality Data
  - 최근 1년 간의 PM2.5, PM10, NO2, CO, O3 and SO2 의 1시간 단위 데이터가 제공됨
- Weather Data
  - Temperature, Pressure, humidity, Wind_speed, Wind_direction, Weather 의 1시간 단위 시계열 데이터가 제공
  - 이러한 각 수치들은 시간별로 도시의 각 구의 측정소에서 따로따로 측정되어 데이터를 제공함
  - 데이터에는 상당히 많은 결측치가 존재하며 또한 온도 나 풍속 데이터에서 상당한 이상치 데이터도 있는만큼 각별한 데이터 전처리가 중요

### Evaluation
- 주최측은 SMAPE(대칭 평균 절대 오류) 값을 기준으로 평가를 실시함
- 보통 시계열 데이터에서는 MAPE 를 쓰지만 실제값이 0일 때 측정값이 정의되지않는 등 제한 사항이 있는 만큼 본 대회에서는 SMAPE 를 사용
- 실제값과 예측값의 차이가 0 에 가까울수록 SMAPE 값은 0 에 수렴
- 최종 점수는 31일 중 SMAPE Score 가 가장 낮은 5일을 제외한 나머지 일수의 평균으로 책정되며 상위 10개 팀이 이 대회 우승 팀으로 선정됨

###  Issues
- 대회 게시판에 질의한 결과 베이징과 런던의 날씨 예측이 아니라 정확히는 Air Quality Data 에 있는 베이징과 런던에 있는 모든 관측소의 기상을 예측함.
- 제공된 베이징 Air Quality 데이터에는 총 35개의 관측소, 런던에는 총 13개의 관측소에서 측정한 Air Quality 데이터가 있으며 우리는 모든 관측소 지점의 대기오염 수준을 예측해야함.
