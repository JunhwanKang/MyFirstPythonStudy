#일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도: {2}]".format(self.name, location, self.speed))

#공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력: {0}, 공격력: {1}".format(self.hp, self.damage))
    
    def Attack(self, location):
        self.location = location
        print("{0} : {1}방향으로 공격!!! [공격력: {2}]".format(self.name, self.location, self.damage))

    def damaged(self, damage):
        self.damage = damage
        print("{0} 유닛이 {1} 피해를 입었습니다.".format(self.name, self.damage))
        self.hp -= damage
        print("현재 남은 체력은 {0}입니다".format(self.hp))
        if self.hp <= 0 : print("{0} 유닛이 파괴되었습니다.".format(self.name))

firebat = AttackUnit("파이어벳", 50, 16, 8)
firebat.Attack("1시")
firebat.damaged(25)
firebat.damaged(25)

#공중 유닛
class FlyableUnit:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도: {2}]".format(name, location, self.flying_speed))

dropship = FlyableUnit(5)
dropship.fly("드랍쉽", "1시")

class FlyAttackUnit(AttackUnit,FlyableUnit):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0)
        FlyableUnit.__init__(self, flying_speed)

        def move(self, location):
            print("[공중 유닛 이동]")
            self.fly(self.name, location)

valkyrie = FlyAttackUnit("발키리", 80, 200, 10)
valkyrie.fly(valkyrie.name, "1시")   
valture = AttackUnit("벌쳐", 80, 10, 20)
battlecruiser = FlyAttackUnit("배틀크루져", 500, 25 ,3)

valture.move("11시")
battlecruiser.move("9시")

#건물 
class bulidingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)

supply_depot = bulidingUnit("서플라이 디폿", 500, "7시")    

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass #아무것도 안하고 넘어간다 (완성된것 처럼)

game_start()
game_over()