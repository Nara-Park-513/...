#break
for x in range(6):
    if x == 3: break #지정한 숫자를 미포함하고 그 전에 끝남
    print(x)
else:
    print("Finally finished")


#nest loop
adj = ["red","big","tasty"]
fruits = ["apple","banana","cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

#알파베티컬 개별 출력
for x in "abcdefghigklmnopqrstuvwxyz":
    print(x)

#(2, 30, 3) 시작은 2로 해서 30에서 끝나지만 3씩 증가한다
for x in range(1, 29, 3):
    print(x)

print("------------------")

#코드가 아주 간결해짐
for x in range(101):
    print(x)


#시작 매개변수 사용
for x in range(50, 101):
    print(x)

'''
for 루프는 시퀀스(리스트, 튜플, 사전, 집합 또는 문자열)를 반복하는데 사용한다
이는 다른 프로그래밍의 for와 덜 비슷함
다른 객체지향의 프로그래밍에 반복자 메서드와 더 비슷하다

Sequence : 여러개의 값을 순서대로 저장할 수 있는 자료형
값들이 일정한 순서를 가지고 나열되어 있는 자료구조
시퀀스의 공통 특징
1.인덱싱
2.슬라이싱
3.반복(iteration)
4.len
5.멤버쉽 테스트 in
6.연결 및 반복
'''