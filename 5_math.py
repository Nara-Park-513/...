#)그외
import math

'''
하이퍼볼릭 코사인 (다양한 숫자의 역 쌍곡선 코싸인)
math.acosh() 
성질 : 1보다 크거나 같아야 합니다 => 최소 1부터 표기합니다
사용이유 cosh(x)의 결과로 부터 원래의 값 x를 찾기 위함입니다
1보다 커야되는 이유
cosh(x) 함수의 값은 항상 1 이상 이기 때문에 1이상이 나와야 합니다
'''
print(math.acosh(7))
print(math.acosh(56))
print(math.acosh(1))

#print(math.acos(2))
#-1 ~ 1사이의 값
print(math.acos(0.55))
print(math.acos(-0.55))
print(math.acos(0))
print(math.acos(1))
print(math.acos(-1))

#)숫자의 아크코사인 (역코사인 함수) 코사인 함수의 역함수로 어떤 값에 코사인 값이 주어졌을 때 그에 해당하는 각도 라디안 또는 도를 구합니다
# 라디안은 각도를 재는 단위 중 하나로 호(arc)의 길이를 반지름으로 나눈 값
# math.acos() -1 ~ 1 사이여야만 합니다
# math.acos(-1)은 pi값을 반환합니다



#1) 최대 최소 값
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x, y)

#2) 절대값
x = abs(-7.25)
print(x)

#3)거듭제곱
x = pow(4, 3)
print(x)

import math
#4)제곱근
x = math.sqrt(64)
print(x)

#5) 올리고 내리고
x = math.ceil(1.4)
y = math.floor(1.4)

print(x, y)

print("===================")

#6)파이선 상수
print("오일러수", math.e)
print("양의무한대", math.inf)
print("숫자가 아님", math.nan)
print("반지름", math.pi)
print("원의둘레", math.tau)




math = '''
min() : 최소값
max() : 최대값
abs() : 절대값 [음수를 무조건 양수로 바꿔 주는게 절대값 abs(-7.25) 7.25]
pow() : 거듭제곱 pow(4, 3) 4 * 4 * 4
sqrt() square root: 숫자의 제곱근을 리턴합니다 sqrt(64) => 8
ceil() : 올림 1.1 => 2, 1.2 => 2
floor() : 내림 1.6 => 1

수학 상수 : 값이 정해져 있고 변경할 수 없고 참조만 하는 수

math.e : Euler's number 기호 값:약 2.71828... 미분과 적분에 자주 등장
math.inf : 양수의 무한대를 나타냅니다 다른 숫자보다 큰 숫자가 필요할때 사용
math.nan : Not a Number 는 부동소수점 숫자가 아닌 값을 리턴
math.pi : 약 3.14... π
math.tau : 원의 둘레와 반지름의 비율로 정의 됩니다



'''