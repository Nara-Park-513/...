class G7:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("지태씨를 보며")

class Jitae(G7):
    pass

class Jiwon(G7):
    def move(self):
        print(" 커피가 G7인걸 보고 거절")