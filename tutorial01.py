#sep
#- 데이터들을 출력할때 중간중간 삽입되는 문자를 지정하는 옵션
#- 디폴트값으로 Space로 지정이 되어 있다.
print(1,2,3,4,5,6)
print(1,2,3,4,5,6,sep="   ")
# 출력할 내용뒤에 sep = " "공백을 넣어주면 그 공백수 만큼 숫자 사이사이에 출력이된다.


#내장함수
print(max(3,7,-1,5,4))
print(min(3,7,-1,5,4))

#서식문자
print("10 + 15 = 25")
print("%d + %d = %d"%(10,15,25))
print("{} + {} + {}".format(10,15,25))

print("문자열 : {}".format("문자열"))
print("문자열: %s"%("문장열"))

#실수 자리수 지정
print(1.234)
print("{:f},{:.2f}".format(1.234,1.234))
print("%.2f"%(1.234))

