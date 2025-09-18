/*
public : 접근제어자 프로젝트 내 어디서든 접근 가능하다
class : 클래스를 정의한다는 키워드
Intro_1 : 클래스명은 최초 작성한 파일명과 완전 동일해야한다

Intro_1이라는 이름을 가진 공개 클래스 선언
 */

public class Intro_1 {
    //자바를 시작할 때는 반드시 파일명과 같은 명칭의 클래스를 사용해야 한다
    public static void main(String[] args){
//특별한 이벤트가 발생하지 않는 한 여기서 출력을 한다 
        int num = 10; //여기서 10 정수 리터럴
        String message = "곧 쉬는 시간";
        boolean isActive = true;

        System.out.println(num);
        System.out.println(message);
        System.out.println(isActive);
        System.out.println("hello world");
/*
System : 자바의 표준 라이브러리 클래스 (java.lang.System)
out : System 클래스가 제공하는 정적(static)출력 스트림(PrintStream)
println() 출력 후 줄바꿈을 하는 메서드
"hello world" 문자열 리터럴
 */
    }
}
/*
public : 어디서나 호출가능해야 
하므로 공개 접근제어자 사용
static : 객체를 생성하지 않아도 실행할 수 있도록 해줌 jvm이
클래스 로딩 후 바로 실행 가능
void : 리턴 값 없음
리턴이 들어가면 변수 타입이 붙는다
main : 프로그램 시작점(entry point)로 인식되는 메서드 이름
(String[] args) : 명령줄 인자(command line arguments)를
배열로 전달받음

즉 프로그램 실행이 시작되는 특별한 메소드 정의
 */