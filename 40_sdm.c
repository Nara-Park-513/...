/*
1.자동차 구조체 정의
2. 그 구조체에 대한 메모리를 동적으로 할당
3. 값을 설정
4. 메모리 해제하고 종료
*/


#include <stdio.h> //입출력 함수
#include <stdlib.h> //메모리 할당/해제
#include <string.h> //문자열 처리 함수 (strcpy)

struct Car{
    char brand[50]; //최대 49자 + null 종료 문자(\0)
    int year; //자동차의 연식(정수)
};

int main(){

    //구조체의 크기 만큼 메모리를 동적으로 할당
    //그 메모리 주소를 ptr 포인터에 저장
    //(struct Car*) malloc 이 변환하는 void*를 struct Car*로 명시적 형변환
    //malloc 은 요청된 size 만큼 메모리를 힙영역에서 할당하고 반환값의 자료형은 void*
    //void*는 타입이 지정되지 않는 포인터 즉 어떤 타입의 포인터로도 변환(cast)할 수 있다
    struct Car *ptr = (struct Car*) malloc(sizeof(struct Car));

    //메모리 할당이 실패할 경우를 대비
    if (ptr == NULL){
        printf("메모리 적재 실패\n");
        return 1;
    }//오류 메세지 출력하고 프로그램을 종료 합니다

    //ptr이 가리키는 구조체의 값을 설정 brand 는 현대 문자열을 복사
    //year는 2025를 저장
    strcpy(ptr -> brand, "hyundai");
    ptr -> year = 2025;

    //구조체에 저장된 값을 저장
    printf("Brand: %s\n", ptr -> brand);
    printf("Brand: %s\n", ptr -> year);

    //malloc에 할당된 메모리 해제 메모리 누수 방지를 위해 꼭 필요함
    free(ptr);

    return 0;



}

/*
malloc() : 구조체에 대한 메모리를 할당
초기화 되지 않은 메모리를 할당
값을 할당하기 전까지 내용이 정의되지 않음


strcpy() : 문자열을 brand필드에 복사하는데 사용
포인터를 통해 멤버에 접근

free() : 메모리를 해제하기 위해 끝에서 사용


구조체와 다이나믹 메모리
- 미리 필요한 구조체의 수를 알 수 없는 경우나 
필요한 것만 할당해서 메모리를 절약하려는 경우
(자동차 대수가 고정되어 있지 않는 자동차 판매점
프로그램)에 유용
*/