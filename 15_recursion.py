#10 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 + 0

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("이 문제는 잘 나오는 재귀함수 문제입니다 정답은 : ")
tri_recursion(10)





recursion = '''
재귀함수 : 정의된 함수가 자기 자신을 스스로 호출
- 재귀는 일반적인 수학 및 프로그래밍 개념입니다
- 데이터를 반복하여 결과에 도달할 수 있는 장점이 있다
- 종료되지 않게 잘못 설계되면 과도한 메모리 프로세스 성능을 사용
'''