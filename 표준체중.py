#표준체중을 구하는 프로그램을 작성
#성별에 따른 공식
#남자: 키 x 키 x 22   키 = meter단위
#여자: 키 x 키 x 22
#조건 1: 표준 체중은 별도의 함수 내에서 계산
#          함수명 : std_weight
#          전달값 : 키(height), 성별(gender)
#조건 2: 표준 체중은 소수점 둘째자리까지 표시

#출력 예  키 175cm 남자의 표준 체중은 67.38kg입니다.

height = int(input("키를 입력하시오: "))
gender = input("성별을 입력하세요: ")

def std_weight (height, gender):
    if gender == "남자":
        print("키 {0}cm {1}의 표준 체중은 {2}입니다.".format(height, gender, round(height*height*22/10000, 2)))
        return height
    elif gender == "여자":
        print("키 {0}cm {1}의 표준 체중은 {2}입니다.".format(height, gender, round(height*height*21/10000, 2)))
        return height

std_weight(height, gender)
