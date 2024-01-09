#월급을 입력받아 연봉출력
#거기서 소득세 제외한 실수령 계산 소득세는 3.3%
salary = input('월급입력')
year_salary = int(salary)*12
소득세 = (year_salary/1000) * 33
year_salary_소득세 = year_salary-소득세
print(int(year_salary_소득세))

