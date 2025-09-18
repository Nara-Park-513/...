public class Str_7 {
    
    public static void main(String[] args) {
int randomNum = (int)(Math.random() * 46);
int randomNum2 = (int)(Math.random() * 46);
int randomNum3 = (int)(Math.random() * 46);
int randomNum4 = (int)(Math.random() * 46);
int randomNum5 = (int)(Math.random() * 46);
int randomNum6 = (int)(Math.random() * 46);
System.out.println(randomNum);
System.out.println(randomNum2);
System.out.println(randomNum3);
System.out.println(randomNum4);
System.out.println(randomNum5);
System.out.println(randomNum6);

System.out.println(Math.random());

String New = "We are the so-called \"Viking\" from the north";
System.out.println(New);

String txt = "abcdefg";
System.out.println("txt 변수의 문자수는 : " + txt.length());

String upper = "hello world";
System.out.println(upper.toUpperCase());

//문자열에서 문자 찾기 문자열이 처음 나타나는 위치 => indexOf
String find = "Please locate where 'locate' occurs!";
//
System.out.println(find.indexOf("locate"));

//charAt() 문자열의 특정위치에 있는 문자에 엑세스를 할 수 있다
//H(0)e(1)l(2)l(3)o(4)
String gt = "hello";
System.out.println(gt.charAt(0));
System.out.println(gt.charAt(4));

//문자열 비교
String txt1 = "Hello";
String txt2 = "hello";
System.out.println(txt1.equals(txt2));
String hi1 = "Gt";
String hi2 = "Gt";
System.out.println(hi1.equals(hi2));

//trim() 앞뒤에 공백을 제거
String ba = "   hello world     ";
System.out.println("Before: [" + ba + "]");
System.out.println("After: [" + ba.trim() + "]");
    }
}
