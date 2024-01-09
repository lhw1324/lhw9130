list =[15,20,30,90]
#list 의 길이를 재라 --> len 쓰진말래

a=0
for x in list:
    a=a+1
    print(a)

    aaaa=0
    for X in list :
        aaaa+=X

    #list 의 평균 (합계/계수)을 출력하세요
hap=0
size=0
for k in list:
    hap= hap +k
    size= size+1