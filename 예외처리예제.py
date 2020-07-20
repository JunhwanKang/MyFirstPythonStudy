# 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
# 대시 손님의 치킨 요리시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

# 조건1: 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
#        출력 메세지: "잘못된 값을 입력하였습니다."
# 조건2: 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#        치킨 소진 시 자용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#        출력 메시지: "재고가 소진되어 더 이상 주문을 받지 않습니다."

class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1 # 대기 번호

while(True):
    try:
        print("[현재 주문 가능 치킨은 {}마리입니다.]\n".format(chicken))
        order = int(input("몇 마리의 치킨을 주문하시겠습니까? "))
        if order > chicken:
            print("재고가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else: 
            print("[대기번호 {0}] {1}마리의 치킨이 주문 완료되었습니다.".format(waiting, order))
            chicken -= order
            waiting += 1
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")

    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break
    finally:
        print("\n저희 치킨집을 이용해서 감사합니다.")
    
