#2)매개변수 함수는 호출할 때만 실행하는 코드블럭 똑같은 프로세를 언제든 재활용
#기본 매개변수 값 매개변수가 있는 함수에서 매개변수 값을 쓰지 않으면 디폴트로
def my_c(country = "Korea"):
    print(" 제가 사는 나라는 " + country + " 입니다")

my_c("sweden")
my_c("india")
my_c()

#key, value
def my_family(child3, child1, child2):
    print(" 우리집의 가장 막내는 " + child3 + " 입니다")
my_family(child1 = "chaehyun", child2 = "rian", child3 = "baron")

#임의의 인수 * args
def my_kids(*kids):
    print("둘째의 이름은 " + kids[1])

my_kids("채현","리안","바론")

def my_name(fname):
    print(fname + " 입니다")

Arg = '''
인수 (Argument)
함수의 매개변수는 인수로 전달된다
'''
my_name("Ryu")
my_name("Song")
my_name("Park")

def myfunction():
    print("hello world")

myfunction()
'''
함수는 호출할 때만 실행하는 코드블록

'''