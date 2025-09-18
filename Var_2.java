public class Var_2 {

    public static void main(String[] args) {
//여러 변수 선언 여러 개를 사용할 경우 구분자로 구분
//끝날 때는 ;으로 마감
int x = 5, y = 6, z = 10;
System.out.println(x + y + z);
//변수의 명칭은 다른데 값이 같을 경우는
int a,b,c;
a = b = c = 50;
System.out.println(a+b+c);

        //syntax : type variableName = value;
final int myNum2 = 20; //중요한 변수는 최종이라고 표기
//최종변수
//myNum2 = 15;
System.out.println(myNum2);

int myNum = 5;
float myFloatNum = 5.99f;
char myLetter = 'D';
boolean myBool = true;
String myText = "Hello";

System.out.println(myNum);
System.out.println(myFloatNum);
System.out.println(myLetter);
System.out.println(myBool);
System.out.println(myText);

String Varia = "변수는 데이터 값을 저장하는 컨테이너이다 \n"+
" java에는 아래와 같은 여러 유형의 변수가 있다 \n"+
" String => 텍스트를 저장 큰따옴표로 묶는다 \n"+
" int => 소수점이 없는 정수(123 또는 -123) \n"+
" float => -19.99 or 19.99 \n"+
" char => a A와 같은 단일 문자를 저장 \n"+
" boolean => 참 또는 거짓을 저장 \n";
System.out.println(Varia);
    }
}
