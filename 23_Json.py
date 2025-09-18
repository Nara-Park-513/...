import json #예약어는 변수명으로 쓸 수 없다

#파이선 dict를 json으로
x = {
    "name":"john","age":30,"city":"new york"
}
# convert into json
y = json.dumps(x)

print(y)

#약간의 json
x = '{"name":"류지태","age":40, "city":"안산"}'

#parse x 사용처에 맞게 형식을 바꾸는 것 파싱
y = json.loads(x)

print(y["age"], y["name"])
js = '''
Java Script Object Notation
인간이 보는 데이터를 전송할 때 가장 많이 사용하는 경량 데이터 교환 형식
자바스크립트 문법을 바탕으로 했지만 python, java, c, go등 대부분 언어에서 사용가능
가볍고 간단해서 내트워크 전송이나 API 응답 형식에 많이 사용한다
key-value 구조: 데이터를 이름 : 값 형태로 표현한다
'''