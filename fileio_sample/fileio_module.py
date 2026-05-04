# file path : fileio_sample\\fileio_module.py
# module : fileio_sample.fileio_module.py

# 파이썬에서의 파일 입출력처리 테스트 스크립트(함수들만 저장된 모듈 파일)
# 파이썬에서의 파일 입출력은 3단계이다.
# open() -> write() 또는 read() 함수를 통한 읽고 쓰기 -> close()
'''
# open() 반드시 두개의 전달인자를 모두 써야한다.
파일변수 = open('디렉토리명\\파일명.확장자', '열기모드')

파일 입출력의 기본은 텍스트 입출력이다.
열기모드 :
w(wt), x(xt) : 새로 쓰기 모드로 열림. 
w는 대상파일이 없으면 파일을 새로 만듦. 대상 파일이 있으면 기존 내용을 모두 지움.
x는 대상파일이 없으면 오류 발생.
a(at) : 추가 쓰기 모드로 열림. 
a는 대상파일이 없으면 파일을 새로 만듦. 대상 파일이 있으면 기존 내용 위에 추가로 씀.
r(rt) : 읽기만 가능.
r은 대상파일이 없으면 오류 발생.
'''

# 1. 파일을 새로 만들고 값 기록 저장하기
import os

def test_fwrite():
    # f = open('testa.txt', 'w') # 기본경로는 현재 폴더 아래에 저장됨
    f = open('testa.txt', 'w', encoding='UTF-8') # 인코딩에 유니코드 문자셋을 넣어주면 한글 정상 출력됨
    f.write('test file writing check.....\n')
    f.write('2026-05-04')
    f.write('파일에 저장 확인용') # 텍스트파일의 기본 인코딩은 os를 따름 : window 기본 문자셋은 'ms949'(ISO 8859-1)
    # ISO 8859-1는 유니코드 문자셋이 아니어서 한글이 깨져서 나옴
    f.write('!@#$%^&*※☆★○●◎◇◆□■') # 한글 변환 특수문자도 유니코드 문자셋 필요
    f.close()
    return

# 원하는 디렉토리에 파일 만들기
# open() 함수 첫번째 전달인자(전달값(argument): 함수의 매개변수(parameter)에 전달되는 값)
# 전체 경로와 파일명을 함께 입력하면 됨 => 주의: 백슬러시(\) 이스케이프 문자 반드시 두개씩 표기
def test_fwrite2():
    # x 모드 : 대상파일 존재 시 에러 (File Exists Error). 주로 덮어쓰기 방지용으로 사용
    f = open('C:\\python_workspace\\python_fileio\\fileio_sample\\testb.txt', 'x', encoding='UTF-8')
    f.write('test file using path saved.....\n')
    f.write('전체 경로 포함 파일 저장 확인\n')
    f.write('2026년 5월 4일 작성')
    f.close()
    return
# test_fwrite2 end ----------------------------

# a모드 : append(추가쓰기모드)
# 기존내용 마지막 위치 뒤에 추가 기록
def test_fwrite3():
    f = open('testc.txt', 'a', encoding='UTF-8')
    f.write('test file append mode\n')
    f.write('파일의 기존 내용 뒤에 추가 쓰기\n')
    f.close()
# test_fwrite3 end -------------------------------


# 파이썬에서 파일이나 디렉토리 다루기
# os 모듈이 제공하는 함수 사용법
def test_osmodule():
    # 사용중인 컴퓨터의 사용자 계정(컴퓨터이름) 조회
    print(f'사용자 계정 : {os.getlogin()}')

    # 현재 작업 디렉토리 확인
    # os 모듈을 활용하면 현재 작업중인 경로를 확인하고 이용할 수 있음
    print(f'현재 파일 경로 : {os.getcwd()}') # get currunt working directory (작업 디렉토리 조회)