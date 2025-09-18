//변수에서 스트링 "" 단일문자 ''

#include <stdio.h>
#include <string.h>

//구조체 생성
struct myP{
    int myNum; //숫자형 변수 정의
    char myLastName;// 한글자만 출력하는 char를 정의
    char myString[30];//char 문자자료형 1바이트 크기 30바이트
    //문자열과의 관계 29글자 + 문자열 종료문자('\0 ') 널문자
};//0값이 거짓 1이 참인 값

int main(){//정상적인 종료는 0, 비정상적 종료는 다른 숫자
  struct myP s1;
  //add
  struct myP s2;

  //객체를 사용하는 이유 언제든 같은 방법을 재사용
  s1.myNum = 13;
  s1.myLastName = 'P';
  strcpy(s1.myString, "hello world");

  printf(" 나의 숫자는 : %d\n", s1.myNum);
  printf("나의 성은 : %c\n", s1.myLastName);
  printf(" 내가 쓴 문자열은 : %s", s1.myString);

  s2.myNum = 26;
  s2.myLastName = 'W';

  printf(" 나의 숫자는 : %d\n", s2.myNum);
  printf("나의 성은 : %c\n", s2.myLastName);


}



/*
C Structures => 구조체 여러개의 변수를 한곳으로 
그룹화하는 방법이다
배열과 달리 구조체는 다양한 데이터 유형(int, float, char)
등을 포함할 수 있다
struct{
struct 키워드를 사용하여 생성하고 각 멤버를 중괄호 안에 선언한다
}
*/