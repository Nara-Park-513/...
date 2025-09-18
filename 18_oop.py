class Student:
    #생성자는 객체를 초기화 하는 형태 대량으로 생성하기 위해서 편리하게
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money

pobj = Student("유지태", 27, 100000000)
pnr = Student("박나라", 27, 20000)

print(pobj.name, pobj.age)

oop = '''
클래스는 객체의 모양을 정의하고 객체는 해당 클래스를 기반으로 생성된다
class = 과일
object = 사과, 바나나, 망고

클래스와 객체를 사용하여 코드를 구성하여 구성과 재사용성을 개선할 수 있다
- DRY원칙은 같은 코드를 한 번 이상 작성하지 않아야 한다는 것을 의미한다
반복되는 코드는 함수나 클래스로 옮겨 재사용 해라
- 프로그램에 명확한 구조를 제공
- 코드를 유지 관리, 재사용, 디버깅을 쉽게 만든다
- 불필요한 작업을 반복해서 하지 않는다
- 더 적은 코드로 재사용 가능한 어플리케이션을 구축할 수 있다
Don't Repeat Yourself
what is OOP?
Object-Oriented Programing 객체 지향 프로그래밍을 의미 한다
'''