# ================ 비밀번호 만들기 ================
#     규칙1. http:// 부분제거
#     규칙2. 처음 만나는 점 이후 부분 제거
#     규칙3. 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + ! 로 구성
#
url = "http://github.com" 
myStr = url.replace("http://", "")  #규칙1
# print(myStr)
myStr = myStr[:myStr.index(".")]  #규칙2
print(myStr)
pwd = myStr[:3]+str(len(myStr))+str(myStr.count("e"))+ "!"
print(url+"의 비밀번호는 "+pwd+"입니다.")


