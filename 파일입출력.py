score_file = open("score.txt", "w", encoding = "utf8") #스코어텍스트를 열겠다 "w"<<쓰기위한 목적으로 언어는 utf8
print("수학: 0", file = score_file)
print("영어: 50", file = score_file)
score_file.close() #v파일은 항상 닫아줘야한다.

score_file = open("score.txt", "a", encoding = "utf8") # "a"는 덮어쓰기 어팬드의 약자
score_file.write("과학: 80")
score_file.write("\n코딩: 100") # print는 줄바꿈을 해주지만 write 함수는 줄바꿈 안해줘서 직접해줘야 한다.
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8") # "r"은 파일 내용을 읽어오겠다.
print(score_file.read()) # 이것은 파일의 전부를 읽어오겠다는 의미이다.
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.readline()) #줄 별로 읽기, 한줄을 읽고 커서는 다음 줄로 이동되기 때문에 다음 print문은 다음 줄을 읽어온다.
print(score_file.readline())
print(score_file.readline(),end = "") #붙여쓰고 싶다면 end이용!
print(score_file.readline())
score_file.close()

# 내가 쓴 text가 아니라 몇줄인지 모를때
score_file = open("score.txt", "r", encoding = "utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()   

# 내가 쓴 text가 아니라 몇줄인지 모를때 (리스트 사용하기)
score_file = open("score.txt", "r", encoding = "utf8")
lines = score_file.readlines() #list형태로 저장한다.
for line in lines:
    print(line, end = "")
score_file.close()

