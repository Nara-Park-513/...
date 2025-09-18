#include <stdio.h>

int main() {
    int number;//변수를 선언만 하는 경우

    do {
        printf("키보드에 숫자를 눌러 보아요");
        scanf("%d", &number);
    } while (number > 0);  
    //0을 제외한 숫자를 클릭시 실행되고 0을 누를 때는 종료
return 0;

}