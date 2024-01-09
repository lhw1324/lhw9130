info= '950228-1030418'
gender= info [7]

# 남자인지 여자인지

if gender == '1':
    print('남자')

else :
     print('여자')

     # 둘중에 하나 if를 한줄로 --> 상황연산자


     print("남자" if gender == '1' else '여자')

     # 복잡한 조건 상황연산은 쓰지말지 --> 스파게티 소스

     
     print("남자" if gender == '1' else 'duwk')

     currentGender = info {7}

     #info 가 1또는 3이면 남자 여자는 2또는 4
"남자 " if gender == '1' or gender == '3' or gender == '5' else "남자 " if gender in (1,3,5,) else '여자'

#주민번호로 나이 출력하기

#올해의 년도
#태어난 년도  주민번호 앞 2자리를 슬라이싱 한다 -->year 주민번호 7번쨰가 '1','2' --> 19+yera  주민번호 7번쨰가 '3','4' --> 20+yera
# 올해의 년도 - int  ( 태어난 년도)

import datetime 

this_year =datetime.datetime.now().year
year= info [0:2]
if info{7} in ['1,''2']:
elif year= int ('19'+year)
year= int ('20'+year)
print(f (this_year) +'세') 


