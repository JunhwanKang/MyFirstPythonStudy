from random import *

#일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도: {2}]".format(self.name, location, self.speed))

    def damaged(self, damage):
        self.damage = damage
        print("{0} 유닛이 {1} 피해를 입었습니다.".format(self.name, self.damage))
        self.hp -= damage
        print("현재 남은 체력은 {0}입니다".format(self.hp))
        if self.hp <= 0 : print("{0} 유닛이 파괴되었습니다.".format(self.name))

#공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
       
    def Attack(self, location):
        self.location = location
        print("{0} : {1}방향으로 적군을 공격합니다. [공격력: {2}]".format(self.name, self.location, self.damage))

#마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 3, 5)

    #스팀팩 : 자신의 체력을 10사용해서 일정시간동안 이동 및 공격속도 증가
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else: 
            print("{0} : 체력이 부족하여 스팀팩을 사용할 수 없습니다.".format(self.name))

#탱크
class Tank(AttackUnit):
    #시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격, 이동불가
    seize_developed = False #시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        #현재 시즈모드가 아닐때 >>> 시즈모드
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        #현재 시즈모드일 때 >>> 시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False

#공중 유닛
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도: {2}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

#레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False #클로킹 모드 (해제 상태)

    def clocking(self):
        if self.clocked == True: #클로킹 모드 >>> 모드 해제
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
        else:
            print("{0} : 클로킹 모드를 활성화 합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
     print("Player : gg")
     print("[Player님이 게임에서 퇴장하셨습니다.")

#실제 게임 시뮬레이션 

#게임 시작
game_start()
#마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()
#탱크 2기 생성
t1 = Tank()
t2 = Tank()
#레이스 1기 생성
w1 = Wraith()

#유닛 일괄 관리 (생성된 유닛을 모두 append)
Attack_Units = []
Attack_Units.append(m1)
Attack_Units.append(m2)
Attack_Units.append(m3)
Attack_Units.append(t1)
Attack_Units.append(t2)
Attack_Units.append(w1)

#전군 이동

for unit in Attack_Units:
    unit.move("1시")

#탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")

#공격 모드 준비 (마린: 스팀팩, 탱크: 시즈모드, 레이스: 클로킹)
for unit in Attack_Units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

#전군 공격
for unit in Attack_Units:
    unit.Attack("1시")

#전군 피해
for unit in Attack_Units:
    unit.damaged(randint(5,21)) #공격을 랜덤으로 받음 (5~20)사이의 피해

# 게임 종료
game_over()