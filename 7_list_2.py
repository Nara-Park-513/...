#정렬 기능의 사용자 정의
def myNums(n):
    return abs(n -50) #숫자가 50에 가까운지에 따라 목록에 정렬하세요

#파이선에서 오름차순을 사용하시려면 sort(reverse = True)
nums = [100, 50, 65, 82, 23]
nums.sort(reverse = True)
print(nums)

order = ["orange","mango","kiwi","pineapple","banana"]
order.sort()
print(order)

nums = [100, 50, 65, 82, 23]
nums.sort()
print(nums)

#5) 목록 정렬 sort 오름차순 내림차순으로 정렬하는 것
# list 기본적으로 목록을 오름차순
# Ascending 작은 값에서 큰 값 1,2,3
# Descending 내림차순 큰값이 가장 먼저 과거에 쓴 것이 제일 뒤
# sql desc asc
rem = ["a","C","b","c","last"]
rem.remove("c") #제거를 하되 첫번째를 제거 할 것
print(rem)
rem.pop()
print(rem)
del rem[0] #rem변수의 첫번째 항목을 삭제
print(rem)
rem.clear()
print(rem) #[]
#del rem
#print(rem)

del2 = '''
- 목록 항목 제거 -
remove() : 지정된 항목을 제거 합니다

pop() : 마지막 항목 제거
pop(2) : 지정된 인덱스를 제거 합니다

del = 완전 삭제 흔적이 없이 사라지는 것 인덱싱을 사용하면 그 순번을 삭제할 수 있다

clear = [] 안에 내용물이 없이 껍데기만 남은 것
'''