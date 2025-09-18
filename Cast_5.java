/*
Type Casting
형변환은 하나의 기본 데이터 유형
자바에는 두 가지 유형의 캐스팅이 있다

Widening Casting(automatically) 자동
- 작은 글자를 큰 글자 크기로 변환
byte[1(8)bit] -> short[2] -> char[2] -> int[4] -> long[8] -> float[4] -> double[8]

Narrow Casting(manually) 수동
- 큰 글자를 작은 글자 크기로 변환
double -> float -> long -> int -> char -> short -> byte
*/

public class Cast_5 {
    
    public static void main(String[] args){//jvm 대신 출력에 사용

//아래에는 게임의 최대 점수를 백분율로 계산한다
int maxScore = 500; //게임에서 최고 점수

int userScore = 423; //유저가 얻은 점수
//최초에 사용했던 원시적인 형변환이 아니라
//정수와 더블을 나눌 수 없어서 바인딩의 개념으로 생각
double percentage = (double) userScore / maxScore * 100.0d;
System.out.println("User's percentage is " + percentage);


        //작은 캐스팅 작은것에서 큰것
        int myInt = 9;
        double myDouble = myInt;

        System.out.println(myInt);
        System.out.println(myDouble);

        //작은 캐스팅은 언제 사용하냐면 숫자를 스트링[파싱]이나 또는 위에서 보는 것처럼 바꿀때
        
        double myD = 93.11d;
        int myI = (int)myD;

        System.out.println(myD);
        System.out.println(myI);
    }

}
