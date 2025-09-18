#include <stdio.h>

//함수
void myF(){//개발자가 만드는 함수
    printf("저는 호출할때만 실행됨");
}

//함수2
void calculateSum(){
int x = 5; int y = 10; int sum = x + y;
printf("계산의 합은 %d", sum);
}

int main(){//출력함수
    calculateSum();
    myF();//호출
    return 0;
}

/*
C function
- 호출 될 때만 실행되는 코드 블록
- 매개변수라고 하는 데이터를 함수에 전달할 수 있다
- 함수는 특정작업을 수행하는데 사용되며
- 코드를 재사용하는데 중요합니다
- 코드를 한번 정의하면 여러번 사용할 수 있다
- void는 반환값이 없음을 의미하며 스스로 할 수 없다는 것
syntax
void myFunction(){
//code
}
*/