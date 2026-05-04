# file path : loop\\while_sample.py
# module : loop.while_sample
# while문 사용 테스트 스크립트
'''
while 반복에 대한 조건식:
    반복 실행할 구문

반복에 대한 조건식은 무한 루프가 되지 않게 작성할 것
만약, 조건식 대신 True를 사용한다면 반드시 while문 안에 종료에 대한 break 조건문을 작성할 것
while True:
    반복 실행할 구문
    if 종료에 대한 조건식:
        break
'''

def test_while():
    num = 5
    while (num > 0):
        print(f'num : {num}')
        num -= 1
    return

# 횟수가 정해지지 않은 반복에 주로 씀
# 예) 문자 하나를 입력받아서 그 문자의 유니코드를 반복 출력 실행
# 단, 문자 '0'이 입력되면 반복 종료
def print_unicode():
    ch = input('문자 하나 입력(0 입력 시 종료) :')
    while ch != '0':
        print(f'{ch} is unicode : {ord(ch)}')
        ch = input('문자 하나 입력(0 입력 시 종료) :')
    # while end -------------------------------
    return
# print_unicode end ---------------------------