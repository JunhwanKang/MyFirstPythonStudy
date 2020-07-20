#방법 1
import theater_module
theater_module.price(3)
theater_module.price_morning(3)
theater_module.price_soldier(3)

#방법 2
import theater_module as tm  #이름이 길 경우에 as를 써서 이름을 줄일 수 있음
tm.price(3)
tm.price_morning(3)
tm.price_soldier(3)

# #방법 3   *은 모듈에 있는 모든 것을 쓰겠다
# from theater_module import *
# price(3)
# price_morning(3)
# price_soldier(3)

#방법 3-1
from theater_module import price,price_morning  #이렇게 원하지 않는 부분은 빼고 사용 가능 여기서도 as써서 함수이름 지정가능 
price(3)
price_morning(3)
# price_soldier(3)