리스트=[3, 'hello', 5>3 true ]
튜풀=tuple(리스트)

# CRUD - 삭제는 del 연산자
# mehtod : 객체 (파이썬을 구성하는 부품 소속된 함수)
리스트.append(100)
리스트[0]=리스트[0]* 10
print(리스트)
del  리스트[0]
print(리스트)

# SET 중복 불가능하고 순서가 없다 정렬된것처럼  보여도 우연일뿐
set= {1,2,3,4}
print(set)
set.add(5)
print(set )

#리스트나 튜플이 중복가능하고 순서가 있다
list=[1.3.4.6.1.4.2]

list= [1,3,5]

#10 in list :결과가 참거짓 ( 10 이 list에 있니 없니)
#list 의 원소를 하나씩 꺼내 아이탬에 담는 반복문
for item in list :
    print(item)
index=0
while  index <3 :
    print (list[index])
    index+=1