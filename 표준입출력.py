print("Python" + "Java") #  +를 쓰면 붙어서 출력이 된다.
print("Python", "Java") # ,를 쓰면 한칸 뛰고 출력이 된다. 여기서 sep를 쓰면 공백이 아닌 원하는 것을 넣어줄 수 있다.
print("Python", "Java", sep = ",") 
print("Python", "Java", "Ruby", sep = " vs ")
print(" ")
print("Python", "Java", end = "? ")
print("뒤에 end를 쓰면 붙어서 출력이 됩니다!!!(원래는 줄 바꿈)")
# print("Python", "Java", file = sys.stdout) #표준 출력
# print("Python", "Java", file = sys.stderr)   #표준 에러

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(4), str(score).rjust(4), sep= ":")
    #ljust()는 ( )안에 숫자만큼 자리를 만들고 왼쪽정렬 rjust() 반대로 오른쪽정렬

#은행 순서대기표
for num in range(1,21):
    print("대기번호: "+ str(num).zfill(3))

#값 입력 받을때 주의할점
answer = input("아무 값이나 입력하세요: ") #여기서 숫자를 입력해도 출력은 잘된다 그 이유는 answer의 타입을 출력해보면 
print("입력하신 값은 " +answer+ "입니다.") #str이기 때문에 우리가 입력한 숫자는 문자열이 되기때문이다!!!   
#항상 문자열 형태로 출력된다.

