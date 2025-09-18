class Teacher:#상위 클래스
    def __init__(self, am, pm):
        self.subjects = am
        self.subjects2 = pm
        
    
class Student(Teacher):#하위 클래스 파생
    def __init__(self, am, pm, talk):
        super().__init__(am, pm)
        #새로운 기능 추가
        self.message = talk
        
        
        q = Teacher("파이선", "c")
        w = Student("파이선","c", "너무너무 어려워요")