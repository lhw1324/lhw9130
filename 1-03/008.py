#국어 영어 점수를 입력받아 합계와 평균을 출력
kor = input('국어점수입력')
eng = input('영어점수입력')
print(type(kor))
kor=int(kor)
eng=int(eng)
hap = kor+eng
avg = hap/2
print(f'합계는{hap}점 평균은{avg}점입니다')
#f문자열
