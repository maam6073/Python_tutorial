#Q2
#while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.

# num = 0
# tot =0
# while(num <= 1000):
#     if(num %3 ==0):
#         tot += num
#     num += 1
# print(tot)


#Q3
#while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
# star ='*'
# starnumber = int(input("숫자입력 : "))
# num = 1
# while(num <= starnumber):
#     print(star * num , end ="")
#     print()
#     num +=1


#Q4
#for문을 사용해 1부터 100까지의 숫자를 출력해 보자.
# for i in range(1,101):
#     print(i)

#Q5
#A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
a = [70,60,55,75,95,90,80,80,85,100]
tot = 0
avg = 0
for i in range(a.__len__()):
    tot += a[i]
    avg = tot / a.__len__()
print(avg)


