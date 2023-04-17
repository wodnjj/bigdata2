print('hello world')

import myfunc
from myfunc import hello, hello2, add, add2

# 함수를 불러서 사용
hello()
hello2('눈이 아프다')
hello2(2)
add(5, 3)
result = add2(5, 3)
hello2(result)