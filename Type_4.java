public class Type_4 {
/*
객체가 아님 -> 메모리에 값 그대로 저장이 된다
Null 불가 -> 원시 타입의 변수는 null 값을 가질 수 없다
성능상 유리 -> 값만 직접 다루기 때문에 연산 속도가 빠르다
앞에 대문자로 바뀌면서 Wrapper 클래스로 존재한다
*/    
    public static void main(String[] args) {

String primitive = "기본데이터 유형\n"+
"byte : -128 ~ 127\n"+
"short : -32,768 ~ 32,767\n"+
"int : -2,147,483,648 to 2,147,483,647\n"+
"long : -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807\n"+
"float : 소수점 6~7 자리 저장\n"+
"double : 소수점 15~16자리 까지 저장\n"+
"boolean : 참1 거짓0\n"+
"char : 단일 문자 또는 ASCII 값을 저장\n"+
"원시값은 가장 기본적인 데이터 타입 객체가 아닌 값 그 자체를 저장하는 타입";

System.out.println(primitive);
    }
}
