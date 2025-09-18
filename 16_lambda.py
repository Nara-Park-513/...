def myNums(n):
    return lambda a : a * n

mydoubler = myNums(2)
mytripler = myNums(3)

print(mydoubler(11))
print(mytripler(11))


def myCalc(n):
    return lambda a : a * n
mydoubler = myCalc(2)

print(mydoubler(11))


x = lambda a, b, c : a * b * c
print(x(5, 6, 2))


x = lambda z: z + 10 #익명 함수를 만드는 표현식
print(x(5))


Lambda ='''
그런데 당최 람다함수는 왜 사용하나요..
람다함수가 아닌 일반함수에서 사용할 때 더 편리하고 고급스럽다
함수이지만 이름이 없고 간결한 함수 익명함수
인수를 많이 받아도 되지만 표현식은 하나만 가질 수 있다

syntax

lambda arguments :expression
'''