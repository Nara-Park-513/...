ins = [" 안해서 "," 미안 "]
ins.insert(0, " 예제를 ")
print(ins)

lun = ["점심시간 45"]
ch = ["분 남음"]
lun.extend(ch)
print(lun)

app = ["a","p","p","l"]
app.append("e") #자바스크립트 어팬드로 동일하게 오른쪽에 붙습니다
print(app)

#4) insert Items : 기존의 값을 바꾸지 않고 새로운 목록 항목을 삽입하려면
#insert() 지정된 인덱스에 삽입 / 메서드를 사용합니다 syntax .insert(3, "수박")
#append() : 가장 마지막(오른쪽)에 붙는다
#extend() : 두개의 리스트를 하나의 리스트로 합쳐 줍니다
fruits = ["사과","바나나","체리"]

#3) 리스트 아이템 변경
change = [1,"two","three",4,5,6,7]
change[1:3] = [2,3]
print(change)


thislist = ["사과","banana","체리"]
print(thislist)
print("++++++++++++")
thislist[1] = "바나나"
print(thislist)

#4) 리스트 아이템 추가




#2) 엑세스 목록 : 항목에는 인덱싱이 되어 있으며
# 번호를 참조해서 엑세스 할 수 있다

age = ["이경은","황영일","이기창"] #[0][1][2]
print(age)
print(age[2]) #첫번째 항목의 인덱스는 0입니다

#모든 문자열은 왼쪽부터 오른쪽으로 이동합니다
#만약 리스트 항목중에 가장 마지막만 확인 하고 싶을 경우에는 음수 인덱싱으로 -1
dir = ["left","center","right"]
print(dir[-1])
print(dir[-2])

#Range of Indexes : 항상 lastindex는 미포함 [2:5]
nums = [1,2,3,4,5,6,7] #[0,1,2,3,4,5,6]
print(nums[2:5])

#:시작부터 마지막으로 지정된 범위까지 :4
print(nums[:4]) #시작부터 네번째 까지

#지정된 범위부터 끝까지 [2:]
print(nums[2:]) #세번째 인덱싱부터 끝까지


#파이선에는 리스트가 아닌 변수를 리스트로 바꿔주는 생성자가 있다
#Constructor : 생성자를 사용하는 이유 객체가 생성될 때 자동으로 호출되어
#초기화 작업을 수행하기 위함 숫자로 증가하는 변수를 만들게 되면 초기화는 0
#(튜플)
mytuple = list((1,2,3))#리스트 생성자
print(mytuple) #[](1,2,3) [1,2,3]


thislist = ["apple","banana","cherry"]
print(thislist)

#자동차의 길이 너비 스트링변수에서는 자수라고 얘기합니다 자바스크립트에서는 .length
#len

#중복 허용 : 목록은 인덱싱이 되기 때문에 동일한 값을 갖는 항목이 있을 수 있다
same = ["a","a","b","c","c"] #중복을 허용하지 않는다는 건 중복된건 하나만 나온다
print(same)

Len = [1,2,3,4,5,6,7]
print(len(Len))

#목록은 모든 데이터의 유형이 될 수 있습니다
all = ["str",2,True,False]
print(all)

#정보처리기사 산업기사에서 필기나 실기에 가끔 출제되는 문제
#모든프로그래밍 class와 object
'''
단일변수에 여러 값을 담아주는 것이 array 인데
파이선에서는 numpy 설치전까지 리스트를 사용
목록은 대괄호를 사용하여 생성합니다
index [0][1] 자바, 자바스크립트는 시작을 0부터 합니다
새로운 항목을 추가하면 맨뒤에 추가됩니다 오른쪽
'''


Lists = '''
파이선 컬렉션 (배열) 4가지 컬렉션 데이터 유형을 가지고 있습니다
list(목록) : 정렬되고 변경 가능한 컬렉션 중복된 멤버를 허용합니다
tuple(튜플) : 순서가 있고 변경할 수 없는 컬렉션 중복된 멤버를 허용합니다
set(세트) : 순서가 없고 변경 불가능하며 인덱싱되지 않은 컬렉션 중복된 멤버가 없습니다
dictionary(사전) : 정렬되고 변경 가능한 컬렉션 중복된 멤버가 없습니다
원래는 정렬이 되지 않았지만 파이선 3.7 버전부터 정렬됩니다
'''

'''
Intergrated Development Environment => 통합 개발 환경
VS code, Pycharm, Intellij, 
'''