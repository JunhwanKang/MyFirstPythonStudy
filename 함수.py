def open_account():  #def로 함수를 생성할수있다. def 변수(): 함수 내용
    print("새로운 계좌가 생성되었습니다.") # 여기까지는 함수를 생성 한 것이고, 이것을 호출해야 원하는 결과를 도출할수 있다.

open_account()   #함수 호출

#함수의 전달값과 반환값
def deposit(balance, money):  #전달값이 있는 새로운 함수를 만든다.
    print ("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance+money))  #그리고 그 전달받은 값들을 더해서 출력
    return balance+money #반환값

balance = 0 #처음 통장의 잔액
balance = deposit(balance, 1500)

def withdraw(balance, money):
     if money > balance:
        print("잔액이 부족합니다. 현재 잔액은 {0}원 입니다.".format(balance))
        return balance
     else:
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다".format(balance-money))
        return balance-money

withdraw(balance, 500)    
withdraw(balance,2000)

#================함수의 기본값====================
def info(name, age, main_lang):
    print("이름: {0} \t나이: {1} \t주 사용 언어: {2}"\
        .format(name, age, main_lang))

info("강준환", 25, "자바")
info("홍길동", 25, "파이썬")

#같은 나이에 같은 언어를 사용 (즉 반복되는 값이 있는경우)
#기본값을 지정해 줄 수 있고, 그리고 만약 사용자가 값을 주면 기본값이 아닌 주어진 값을 얻음
def info2(name, age=25, main_lang="파이썬"):
    print("이름: {0} \t나이: {1} \t주 사용 언어: {2}"\
        .format(name, age, main_lang))
info2("강준환")
info2("홍길동")

#키워드값을 이용한 함수 활용!!
def info(name, age, main_lang):
    print(name, age, main_lang)
#이렇게 키워드로 지정할 수 있고 순서대로 정의하지 않아도 맞춰진다.
info(name = "유재석", main_lang = "파이썬", age = 20)
info(main_lang = "자바", age = 20, name = "김태호")  

#가변인자
#만약에 언어를 여러개 할줄아는 사람이 있다면!!!
#아래와 같이 쓸 것이다.
def info(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름: {0}\t나이: {1}\t".format(name, age), end = " ") #end = " "은 줄바꾸지않고 다음문장을 옆에 붙일수있다
    print(lang1, lang2, lang3, lang4, lang5)

info("유재석", 20, "파이썬", "자바", "C언어", "C++", "C#")
info("유병재", 15, "코틀린", "루비", "", "", "") #이 사람은 두개의 언어밖에 하지 못 해서 나머지를 ""로 표현해야하는 
#번거로움이 있다. 사람의 수가 많아진다면 더욱 번거롭다. 그리고 유재석이란 사람이 언어를 한개 더 배운다면 추가할 수 없다.
 
def info(name, age, *language):
    print("이름: {0}\t나이: {1}\t".format(name, age), end = " ") 
    for lang in language:
        print(lang, end=" ")
    print()

info("강준환", 20, "파이썬", "자바", "C언어", "C++", "C#", "자바스크립트")
info("홍길동", 15, "코틀린", "루비")