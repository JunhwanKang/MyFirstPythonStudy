#스타로 예를 들어보자!
#마린: 공격 유닛, 군인. 총을 쏠 수 있음 체력 40, 공격력 5
#탱크: 공격 유닛, 포를 쏠 수 있고, 일반 모드/시즈 모드, 체력150, 공격력 35

class Unit:  
    def __init__(self, name, hp, damage):
        self.name = name   
        self.hp = hp
        self.damage = damage     # self.name, self.hp, self.damage 를 멤버 변수라 한다. 멤버변수는 .을 찍어 클래스 외부에서 사용가능
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
print("유닛 이름 : {0}, 공격력 : {1}, ".format(tank.name, tank.damage)) #이렇게 멤버변수에 접근할 수 있다.
#__init__ 는 생성자를 의미한다.
# 클래스를 이용해서 만들어진 것들을 객체라고 하고, 마린과 탱크 같은 애들은 유닛클래스의 인스턴스 라고한다!!
#self를 제외한 동일한 갯수를 떤져줘야한다.

tank2 = Unit("탱크2", 150, 35)
tank2.sizmode = True
if tank2.sizmode == True:
    print("{0}은 시즈 모드입니다.".format(tank2.name))