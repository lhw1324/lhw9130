#1.값추가  --> input  
#2.리스트 출력
# 999 종료 : 감사합니다 -> 종료

list =[]
while True :
    print("1 값 추가")
    print("2 list 출력")
    print("3 합계 출력")
    print("4 리스트의 평균 출력")
    print("999 종료")
    select =input('번호를 선택하세요')
    if select =='1':
         num= int ( input ('숫자입력:'))
         list.append(num)
    elif select == '2':
        print(f'{list} 출력')

    elif select=='3':
        print(f'입력값의 합계 : {sum (list )}')

    elif select=='4':
            print(f'입력값의 합계 : {sum(list)/len(list)}')
    elif select == '999' :
        print ('감사합니다.')
        break
else :
    print('메뉴를 정확하게 입력하세요')