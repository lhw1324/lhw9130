a='34'
b=int(a) #34
c=float(a) #34.0
d=str(b) #'34'

ar=[3,4,5]
#ar을 튜플로 변환해 br을 저장하시오
br = tuple(ar) #타입을 바꾸는 형은 언제나 같다 그러나 문자를 숫자로 못바꾸는거처럼 못바꾸는거도 있다

#리스트에 원소추가 : append
ar.append(10) #.은 맴버연산자
#append 는 혼자가 아니고 .에소속된 함수로 메소드이다
ar.append(1000)#ar은 리스트
#br.append(1000)#br은 튜플이므로 .을 찍었을때 어펜드가 없다 따라서 오류
print(ar)
ar.append(1000)#어펜드는 마지막에 추가됨
ar.insert(1,1000)#인서트는 내가 원하는곳에 추가가능 0부터 시작
xr = (10,20,30)
xr = list(xr)
xr.append(40)
xr = tuple(xr)
print(xr)
for xr in xr :
    print(xr) 