# 프로젝트(애플리케이션)를 실행하는 스크립트
# 하나의 프로젝트에는 하나의 main만 존재한다.
# CLI(Commend Line Interface) : 실행 시 터미널 창에 글자 형태로 출력되고, 키보드 입력으로 실행
# GUI(Graphic User Interface) : 실행 시 윈도우 창이 열림. 메뉴바/툴바 등을 마우스 클릭으로 실행

# CLI방식의 메뉴 출력용 함수
def menu():
    print('파일 입출력 및 예외처리 테스트용 프로그램 시작')

    # 여러줄의 문자열 값을 표현할 때 ''' '''사용
    prompt = '''
    1. 파일 새로 쓰고 저장하기 테스트
    2. 경로 지정하고 파일 저장하기 테스트
    3. 기존 내용 뒤에 추가 쓰기 테스트
    4. 사용중인 컴퓨터의 사용자 계정과 현재 디렉토리
    5. while 반복문 사용 테스트 1
    6. while 반복문 사용 테스트 2
    9. 메뉴 종료
    '''

    while True:
        # print('1. 파일에 저장하기 테스트 1')
        # print('2. 파일로부터 읽어오기 테스트 1')
        # print('9. 메뉴 종료')2
        print(prompt)
        
        no = int(input('원하는 메뉴 번호 입력 : '))
        if no == 1:
            fs.test_fwrite()
        if no == 2:
            fs.test_fwrite2()
        if no == 3:
            fs.test_fwrite3()
        if no == 4:
            fs.test_osmodule()
        if no == 5:
            lw.test_while()
        if no == 6:
            lw.print_unicode()
        if no == 9:
            break
    # while문 끝나는 지점

    print('테스트 종료 -------------------------')
    return

import fileio_sample.fileio_module as fs
import loop.while_sampe as lw

if __name__ == '__main__':
    # fs.test_fwrite()
    # lw.test_while()
    menu()
    print('프로그램 종료--------------------')


