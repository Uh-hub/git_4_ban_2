

def decorator(func):
    def decorated(input_text):
        print("함수 시작")
        func(input_text)
        print('함수 끝!')
    return decorated


@decorator

def hello_world(input_text):
    print(input_text)



hello_world("hello world!")


#함수를 인자로 받음 decorator(func)
#함수 앞 뒤를 꾸며줌 func 앞 뒤 print문
#인자로 받은 함수 앞뒤
#감싸진 함수를 다시 리턴