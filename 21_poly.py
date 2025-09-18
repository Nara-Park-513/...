class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # 함수
    def move(self):
        print("DC!")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")


car = Car("메세디", "cls450")
boat = Boat("Ibiza","Touring 20")
plane = Plane("Boeing","747")

for x in (car, boat, plane):
    print(x.brand, x.model)
    x.move()


poly = '''
동일한 방법을 사용하는 다양한 클래스
python Polymorphism
- 다형성 : 여러 형태를 의미하며
프로그램밍에서는 여러 개체나 클래스에서 실행될 수 있는 동일한 이름의 메서드
함수 / 연산자를 의미한다

자바에서는 과적이라 한다
'''