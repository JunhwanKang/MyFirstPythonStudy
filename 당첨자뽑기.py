#학교에서 코딩 대회를 주최하는데 댓글 이벤트를 진행하기로 했다.
#댓글 작성자중에 랜덤으로 1명은 치킨, 3명은 커피 쿠폰을 받게 된다.
# 댓글은 20명이 작성하였고 편의상 아이디는 1~20으로 가정한다
# 댓글 내용과 상관 없이 무작위로 추첨되며 중복은 불가한 프로그램을 작성하시오.
# (출력 예)
# -- 당첨자 발표 --
# 치킨 당첨자 : 5
# 커피 당첨자 :[2,3,4]
# -- 축하합니다 --

from random import *

users = range(1,21)
users = list(users)
#print(type(users))
winners = sample(users, 4)
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")