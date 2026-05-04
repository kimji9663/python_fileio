# file path : fileio_sample\\fileio_module2.py
# modlule : fileio_sample.fileio_module2

# 파이썬의 기본파일 입출력은 텍스트 파일 입출력임(*.txt)
# 텍스트가 아닌 자료형의 파일을 다룰때는 pickle 모듈을 활용
# 바이너리(binary : 이진 데이터) 형식의 파일
# 파일 열기 모드 : wb, rb, ab로 표기

import os
import pickle

def test_binary_fileio():
    data = {1:'python', 2:'you need'}
    f = open('btest.dat', 'wb') # 바이너리 형태로 파일 생성
    # write(str) 문자 형태 사용 불가. 바이너리 형태로 기록해야 함.
    pickle.dump(data, f) # dump() : 파일에 딕셔너리 객체가 가진 데이터를 이진 데이터로 기록하는 함수
    f.close()
# test_binary_fileio end -----------------------------------


def test_binary_fileio2():
    f = open('btest.dat', 'rb') # 바이너리 파일은 반드시 rb로 열어야함
    read_data = pickle.load(f) # 파일에 기록된 이진 데이터를 읽어들임
    f.close()

    print(read_data)
    print(type(read_data)) # wb는 해당 객체타입 그대로 기록함: <class 'dict'>
# test_binary_fileio2 end ---------------------
