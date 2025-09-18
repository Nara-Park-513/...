#Python Booleans
b = '''
부울은 두 값중에 하나를 나타냅니다 true 또는 false
숫자 0은 거짓된 값이라 얘기합니다 0이면 실행이 안됨
숫자 1은 값이 있기 때문에 진실된 값 1이면 실행이 됨
파이선은 문법이 들여쓰기를 해야합니다 그렇지 않으면 오타
'''
print(b)

#진실과 거짓 출력
print(10 > 9)
print(10 == 9)
print(10 < 9)

#파이선은 뛰어쓰기를 지켜야 합니다
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
print("조건문은 첫번째 컨디션이 맞으면 실행 그렇지 않으면 두번째 컨디션 둘 다 틀리면 else 실행")

#문자열과 숫자를 평가합니다
print(bool("hello"))
print(bool(15))

#대부분의 값은 진실입니다 but 아래는 거짓의 값을 보여줍니다
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#아래의 예시는 클래스를 사용하는 것인데 값이 0을 가지고 있습니다
class myclass():#클래스 명
    def __len__(self): #클래스안에 함수가 있습니다
        return 0 #함수는 리턴을 만나면 함수 실행이 종료됩니다

myobj = myclass()
print(bool(myobj))

#아래의 예제는 함수를 만들고 그 함수를 참인지 거짓인지 확인합니다
#파이선에서 함수는 def(자바스크립트는 function)로 시작합니다
def myTrue():
    return True

if myTrue():
    print("Yes")
else:
    print("NO!")

#isinstance() : 지정한 객체가 특정 데이터 유형인지 확인하는데 사용하는 함수
#str, int, True
x = 200
print(isinstance(x, int))
print(isinstance(x, str))