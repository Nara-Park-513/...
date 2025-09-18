



userInput = '''
파이선에서는 사용자 입력이 가능하다
사용자에게 입력을 요청할 수 있다는 뜻
'''
print("Enter your name: ")
name = input()
print(f"hello {name}")
fav1 = input(" 어떤 동물을 좋아하시나요 ?")
fav2 = input( "좋아하는 색상은요?")
fav3 = input(" what number?")

print(f"Do you want a {fav2}{fav1} with {fav3}")
#f-string을 사용한 구문 파이선 3.6이상부터 사용