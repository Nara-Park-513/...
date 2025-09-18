#include <stdio.h>

int sum(int k);

    int main() {
        int result = sum(10);//숫자형변수 result는 = 함수 sum에 매개값 10을 대입
        printf("%d", result);
        return 0;
    }

int sum(int k) {
    if(k > 0) {//만약 k값이 존재 한다면
return k + sum(k - 1);//k의 임의의 수에 예를 들어 9면 9 + (9-1)
    }else{
        return 0;//0에서 종료
    }
}


/*
Recursion
- 재귀는 함수 호출 자체를 만드는 기법이다
- 이 기법은 복잡한 문제를 해결하기 쉬운 간단한 문제로 분해
하는 간단한 기법이다
- 재귀는 이해하기 어려울 수 있다[그건 당신의 사정] . 그래서 가장 좋은 방법은
직접 많이 해보는 것이다
*/