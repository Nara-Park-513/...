//1)표준 입출력 라이브러리 설정
#include <stdio.h>//Standard Input Output Header file

int main() {//변수나 출력값을 출력해주는 메인함수
    printf("Hello world");//세미콜론으로 마감을 하지 않으면 일이 끝나지 않은 것처럼 구분이 되질 않아서 오타가 생긴 걸로 인지하다
    return 0;//메인 함수가 종료됨을 의미 리턴함수
}
/*
printf() 출력, scanf() 입력, 
getChar(엔터키를 칠때까지 기다림) 문자 하나의 
아스키[American Standard Code for Information Interchange] 문자를 숫자로 표현하기 위해 사용하는 표준코드체계 값
putChar() 문자 하나를 화면에 출력
*/
/*
c 변수 type
int : 소수점 이하 자릿수 없이 정수를 리턴
float : 소수점이 있는 숫자 -19.99 20.19
char : 'a' 단일 문자를 저장

syntax = 통사론
type variableName = value;
*/