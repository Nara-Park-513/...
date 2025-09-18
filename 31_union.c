#include <stdio.h>

union myUnion{
    int myNum;
    char myLetter;
    char myString[30];
};

int main(){
union myUnion u1;
//엑세스 유니온 멤버
u1.myNum = 1000;
u1.myLetter = 'A';

printf("중요 : 모든 멤버가 동일한 메모리를 공유하므로 하나만 변경하면 다른 멤버에도 영향을 끼친다 마지막으로 할당된 멤버만 유효한 값을 가진다");
printf("myNum: %d\n", u1.myNum);
printf("myLetter: %c\n", u1.myLetter);

return 0;
}
/*
C Unions
- 공용체는 구조체와 유사하며, 서로 다른 데이터 유형의 멤버를
저장할 수 있다
- 하지만 몇가지 차이점이 있다
[구조체는 각 멤버가 자신의 메모리를 가지고 있다
 그런데 공용체는 동일한 메모리 주소를 공유하므로 한번에
 하나의 값만 사용한다
 
 결론은 => 일상적인 프로그램 => 구조체
 메모리를 절약하려는 경우 => 공용체
 ]
*/