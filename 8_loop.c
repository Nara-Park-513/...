#include <stdio.h>

int main(){
//2) 숫자 321을 세고 새해 복 많이 받으세요
int countdown = 3;//초기값은 3

    while (countdown > 0){//3,2,1 실행하고 0일때 중지
    printf("%d\n", countdown);//최초에 3이 나옴
    countdown--;//2, 1
    }

printf("새해 복 많이 받으세요!");





    
    int i = 0; //변수 i에 0을 대입 start
    
    while (i < 1001) {//조건에 end
        printf("%d\n", i);
        i++;//지정된 범위 만큼 반복
    }

    return 0;//종료
}

/*
loop : 루프는 지정된 조건에 도달하는 한 코드블록을 실행할 수 있다
루프를 사용하는 이유 => 시간을 절약하고 오류를 줄이고 가독성을 높여주기 때문에 편리하다

1)while
syntax

while(condition) {

}

2)do {

}while (condition)

*/