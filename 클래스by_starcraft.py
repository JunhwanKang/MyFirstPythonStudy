#스타로 예를 들어보자!
#마린: 공격 유닛, 군인. 총을 쏠 수 있음

name = "마린"
hp = 40
damage = 5

print("{} 유닛이 생성되었습니다.".format(name))
print("체력은 {0}이고, 공격력은 {1}입니다.\n".format(hp,damage))

#탱크: 공격 유닛, 포를 쏠 수 있고, 일반 모드/시즈 모드.
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{} 유닛이 생성되었습니다.".format(tank_name))
print("체력은 {0}이고, 공격력은 {1}입니다.\n".format(tank_hp,tank_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력{2}]".format(name, location, damage))

attack(name, "1시 방향", damage)
attack(tank_name, "1시 방향", tank_damage)