# 당신은 택시기사이고, 어플로 손님을 매칭할 수 있다.
#50명의 승객과 매칭 기회가 있다. 이때 총 탑승 승객 수를 구하는 프로그램을 작성하시오.
#조건1: 승객별 운행 소요 시간은 5분~50분 사이의 난수로 정해진다.
#조건2: 당신은 소요 시간이 5분~15분 사이의 손님만 태울수 있다

from random import *

customers = range(1,51)
customers = list(customers)
num = 0
count = 0
for info in range(50):
    minute = randrange(5,51)
    num += 1
    if 5 <= minute <= 15:
        print("[O]"+str(num)+"번째 손님 (소요시간: "+str(minute)+")")
        count += 1   
    else: 
       print("[ ]"+str(num)+"번째 손님 (소요시간: "+str(minute)+")")


    print("총 탑승 승객: "+str(count)+"명")
    
