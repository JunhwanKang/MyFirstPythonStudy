# gun = 10  #전역변수

# def checkpoint(soldiers):
#     gun = gun-soldiers  #여기서는 지역 변수를 설정해줘야함 여기gun은 전역변수임 
#     print("[함수 내] 남은 총: {0}".format(gun))

# print("전체 총: {0}".format(gun))
# checkpoint(2)  # 2명이 경계근무를 나감
# print("남은 총: {0}".format(gun))

gun = 10  #전역변수

def checkpoint(soldiers):
    gun = 20  #지역변수
    gun = gun-soldiers  #여기서는 지역 변수를 설정해줘야함 
    print("[함수 내] 남은 총: {0}".format(gun))

print("전체 총: {0}".format(gun))
checkpoint(2)  # 2명이 경계근무를 나감
print("남은 총: {0}".format(gun))

#위에 처럼하면 우리 생각대로 출력이 되지않는다 이때 전역변수를 밑에 지역변수에서도 쓰겠다라고 선언해줘야함 그것이 glabal
gun = 10  #전역변수

def checkpoint(soldiers):
    global gun
    gun = gun-soldiers  #여기서는 지역 변수를 설정해줘야함 
    print("[함수 내] 남은 총: {0}".format(gun))

print("전체 총: {0}".format(gun))
checkpoint(2)  # 2명이 경계근무를 나감
print("남은 총: {0}".format(gun))

#==============================다른 방법==================================
gun = 10  #전역변수

def checkpoint_ret(gun, soldiers):
    gun = gun-soldiers  
    print("[함수 내] 남은 총: {0}".format(gun))
    return gun #값을 리턴해서 함수 외부로 떤져줄수있다.

print("전체 총: {0}".format(gun))
gun = checkpoint_ret(gun, 2)  # 2명이 경계근무를 나감
print("남은 총: {0}".format(gun))
