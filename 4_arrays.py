from xmlrpc.client import boolean

import numpy as np

#데이터 유형을 정수에서 불리언으로 변경
arr = np.array([1,0,3])
newT = arr.astype(boolean)
print(newT)

#기존 데이터 유형을 변환
arr = np.array([1.1, 2.1, 3.1]) #실수를 정수로 바꿀 .astype('i')
newarr = arr.astype('i')
print(newarr)

#정의된 데이터 유형으로 배열 만들기
arr = np.array([1,2,3,4], dtype='S')
print(arr)

#상황에 따른 변환 오류 Nan or value 에러
a = np.array(['2','3'], dtype='i')
print(a)

'''넘버인 숫자가 바이트타입인 ASCII코드로 표현된 1byte 문자열로 바뀜'''


arr = np.array([1,2,3,4])
a = np.array([True, False])
b = np.array([1.0, 2.5])
c = np.array([1+2j, 3+4j])
d = np.array(['Hello'])
print(arr.dtype, a.dtype, b.dtype, c.dtype, d.dtype)

#시간 간격
delta = np.timedelta64(5, 'D')
print(delta)

#두 날짜의 차이

d1 = np.datetime64('2025-09-19')
d2 = np.datetime64('2025-09-24')
print(d2-d1)

'''
NumPy 데이터 유형
String : 텍스트 데이터를 나타내는 것
integer : 정수
float : 실수
boolean : 참하고 거짓을 나타냄
complex : 복소수[실수+허수] 1.0 + 2.0j 1.5 + 2.5j
공학,전자,물리학,신호 처리,제어,프랙탈 등의 이미지 생성
넘파이의 추가 데이터 유형
dtype : 데이터 유형을 리턴
i : integer 음수와 양수를 포함한 정수
보통 int8, int16, int32, int64 등과 같이 비트 크기 명시
b : boolean
u : unsigned integer(부호 없는 정수)
음수가 없는 정수 0이상의 수만 표현 가능 0, 5, 255
uint 8, uint 16 등으로 표현
f : float 부동소수점 실수형 데이터, 소수점을 포함한 숫자
3.14 -0.001 float32, float64 비트 수에 따라 정밀도가 달라짐
c : complex float (복소수)
실수부 + 허수부를 가지는 수 예 1.0 + 2.0j
complex64, complex128 등으로 크기를 명시할 수 있다 
m : timedelta(시간 간격) 날짜 또는 시간의 차이 3일, 2시간, 15분 등
시간 간격 계산에 사용됨
M : datetime : 절대적인 날짜와 시간을 나타냄 2025-09-19T13:45:00
O : object : 다양한 파이선 객체를 배열에 저장할 수 있으나 느리고 메모리를 더 사용함
s : string
U : 유니코드 문자열 : 다양한 언어와 특수문자를 표현할 수 있음
V : void(raw data) 다른 유형에 대한 고정 메모리
구조체나 사용자 정의 복합 자료형을 표현할 때 사용되고 일종의 빈틀로 다른 구조체 타입을
정의 할 수 있다
'''