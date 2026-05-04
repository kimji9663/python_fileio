# file path : test_dict\\dict_sample.py
# module : test_dict.dict_sample

# 사전 자료형 : dict
# Java의 map과 같은 구조로 key와 value를 한 쌍으로 저장하는 집합 자료형
# dict에서 key는 변경되지 않는 값이어야 함(한번 지정 시 변경 불가)
# key에 사용할 수 있는 자료형 : tuple
# dict에 저장하는 value는 데이터 제한이 없다.
# json, xml로 변환할 때 자주 사용

def dict_test1():
    # dict 만드는 방법 1: dict() 함수사용
    dct1 = dict()
    print(dct1, type(dct1))
    # dict 만드는 방법 2: {} 사용
    dct2 = {}
    print(dct2, type(dct2))
# dict_test1 end -------------------

# list나 tuple 처럼 인덱스를 사용할 수 없음(인덱스가 없음)
# key를 이용해서 값 변경, 조회, 추가 => 사전변수[키]
# dict 저장 방식 : {키:값, 키:값 ...}
def dict_test2():
    dct1 = {'a':1, 'b':2, 'c':3}
    print(dct1, type(dct1))

    dct2 = {1:'python',  'a':[1, 2, 3], (1, 2):345}
    print(dct2, type(dct2))

    # 값 변경
    dct2['a'] = 77
    print(dct2, type(dct2))

    # 값 추가
    dct2[3] = [11, 12, 13]
    print(dct2, type(dct2))

    # 값 조회
    print(dct2['a'])
# dict_test2 end --------------------------

def dict_function():
    'dict 내장함수 활용' # 함수설명 표기할 수 있음(반드시 함수 바로 밑에 위치해야함)
    dct1 = {
        'a':10,
        'b':25,
        'c':77
    }
    print(dct1, type(dct1))

    # 키에 대한 리스트 만들기 : keys()
    print('dct1의 키 목록 : ', dct1.keys())
    # 값에 대한 리스트 만들기 : values()
    print('dct1의 값 목록 : ', dct1.values())

    # (키, 값)을 item 이라고 함. 아이템들을 리스트로 만들기: items() 함수
    print('dct1의 아이템 목록 : ', dct1.items())

    # 합치기 : update() 함수
    # 사전1.update(사전2) => 사전1을 변경함
    # 사전1과 사전2에 동일한 키가 있을 경우, 사전1의 해당 키의 값이 사전2의 값으로 변경됨
    dct2 = {'name':'갤럭시', 'price':1500000, 'tax':0.15}
    dct3 = {'content':'최신모델입니다.', 'price':880000}
    print('dct2 :', dct2)
    print('dct3 :', dct3)

    dct2.update(dct3)
    print('dct2 :', dct2)

    # pop() 함수 : 해당 키에 대한 값을 제거하고 반환
    tax = dct2.pop('tax')
    print(tax)
    print(dct2)

    # clear() 함수 : 딕셔너리 비움
    dct1.clear()
    print(dct1)

    # copy() 함수 : 깊은 복사
    dct4 = dct3.copy() # 3을 복사해서 4를 만듦
    print('dct3(원본) :', id(dct3)) # 원본
    print('dct4 :', id(dct4)) # 원본과 주소가 다름
    dct5 = dct3 
    print('dct5 :', id(dct5)) # 원본과 주소가 같음

    # in 연산자 : dict 안에 키 또는 값이 존재하는지 확인
    print('name' in dct2) # True
    print('name' in dct3) # False

    # 값 존재여부    
    print('갤럭시' in dct2.values()) # True
    print(1500000 in dct3.values()) # False

    # 키로 값을 조회할 때    
    print(dct2['name']) # 없는 키 조회 시 오류 발생
    print(dct2.get('age')) # 없는 키 조회 시 None 반환(권장)
# dict_function end -----------------


if __name__ == '__main__':
    # dict_test1()
    # dict_test2()
    dict_function()