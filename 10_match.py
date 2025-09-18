#if Statements as Guards
month = 5
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _: #디폴트
        print("No match")


#Combine Values 값을 결합하는 이유는
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 :
        print("오늘은 평일")
    case 6 | 7:
        print("오늘은 주말")



day = 4

match day:
    case 1:
        print("월")
    case 2:
        print("화")
    case 3:
        print("수")
    case 4:
        print("목")
    case 5:
        print("금")

'''
python Match :
다양한 조건에 따라 다양한 작업을 수행하는데 사용된다
여러개의 가독성 없는 문장보다 switch나 match을 사용
syntax
'''