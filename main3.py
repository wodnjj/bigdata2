import mylib

print('1.영화 순위 2. 멜론차트 100')
num = input('입력:')
if num == '1':

    mlist = mylib.get_dmv()
    print(mlist)

    # 리스트에 있는 내용중에 제목만 출력
    for m in mlist:
        print(m[1])

elif num == '2':
    # 멜론차트도 하고 싶다
    mylib.melon()
else:
    print('잘못 입력하셨습니다.')