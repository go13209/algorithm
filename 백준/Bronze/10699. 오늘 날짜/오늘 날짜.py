# 백준 10699 오늘 날짜
import datetime
# datetime 모듈을 활용한다.

date = datetime.datetime.today() + datetime.timedelta(hours = 9)
print(date.strftime('%Y-%m-%d'))
# datetime 객체의 today 메서드를 사용하여 현재 날짜와 시간을 불러온다.
# 문제에 따르면 채점 서버의 시간대는 UTC+0으로 우리나라가 9시간 더 빠르다.
# 따라서 timedelta 메서드를 사용하여 9시간을 더해 서울의 오늘 날짜를 구해야 한다.
# today 메서드는 날짜뿐 아니라 시간까지도 불러오므로 strtfime 메서드를 활용해 연-월-일만 출력한다.