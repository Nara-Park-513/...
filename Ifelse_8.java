public class Ifelse_8 {
    
    public static void main(String[] args) {
int age = 20;
boolean isCitizen = true;

if (age >= 18){
    System.out.println("나이가 충분해서 투표를 할 수 있어요");
    if (isCitizen) {
    System.out.println("그리고 당신은 시민이므로 투표를 할 수 있음");    
    }else{
    System.out.println("외국인이므로 할 수 없음");    
    }
}else{
    System.out.println("넌 어려서 안돼");
}

//if문에 if넣기
int x = 15; int y = 25;
if(x > 10) {
    System.out.println("x is greater than 10");
    //중첩 if
    if(y > 20){
        System.out.println("y is greater than 20");
    }
}         

//삼항 연산자 variable = (condition) ? expressionTrue : expressionFalse;
int time = 20;
String result = (time < 18) ? "Good day." : "Good evening";
System.out.println(result);

int weather = 2;
        if(weather == 1){
System.out.println("우산을 준비하세요");            
        }else if(weather == 2){
System.out.println("눈이 부시네요");
        }else{
System.out.println("하늘이 어두워요");
        }
    }
}
