# for문은 while문과 상호치환할 수 있다.
# 다만 명시적인 시작과 끝이 있을 때 사용
# while문보다 사용빈도가 높다.

#1) 나무를 10번 찍기
# for i in range(1,11): #1 ~ 10
#     print("나무를{0}번 찍었습니다.".format(i))

#2) 리스트, 튜플과 함께 사용하기
# datas = [2,4,6,8,10]
# for num in datas:
#     print(num,end=", ")
# print()
#
# datas = [10,20,30,40,50]
# for num in datas:
#     print(num,end=", ")
# print()

#3) range 함수와 사용
# for i in range(10,21):
#     print(i,end ="")
# print()
#
# for i in range(10,101,2):
#     print(i,end="")
# print()
#
# for i in range(100, 0, -2):
#     print(i,end=" ")
# print()

#4) 1~100까지 누적합을 구하세요
# tot  = 0;
# for i in range(1,101):
#     tot += i
# print("1~100까지 누적합:{0}".format(tot))
#
# #5) 정수를 입력받아 누적하고,
# #    "end"를 입력하면 누적값을 출력하세요
#
# result = 0
# while(True):
#     num1 = input("정수입력: ")
#     if num1 == "end":
#         break
#     elif num1.isdigit():
#         result += int(num1)
#     else:
#         print("정수가 아닙니다.")
# print(result)
#
#
# #6) 정수를 입력받아 저장하고,
# #    "end"를 입력하면 입력한 순서대로 모든 정수 출력
# nums = []
# while(True):
#     num1 = input("정수입력: ")
#     if num1 == "end":
#         break
#     elif num1.isdigit():
#         nums.append(int(num1))
#     else:
#         print("정수가 아닙니다.")
# print(nums)
#
# #8) 구구단 3단을 출력하세요
# for i in range(1,10):
#     print("{0}*{1} = {2}".format(3,i,3*i))

#9) 구구단 9단을 역순으로 출력하세요
# for i in range(9,0,-1):
#     print("{0}*{1} = {2}".format(9,i,9*i))


#숙제
#10) 구구단 9단을 짝수만 출력
# for i in range(1,10):
#     if i % 2 == 0:
#         print("{0}x{1}={2}".format(9,i,9*i))

#11) 구구단 전체를 출력하세요
# for i in range(1,10):
#     for j in range(1,10):
#         print("{0}x{1}={2}".format(i,j,i*j))

#12)구구단 전체를 출력하는데 각 단을 세로로 출력하세요
# for i in range(2,10):
#     print()
#     for j in range(2,10):
#         print("{0}x{1}={2} \t".format(j, i, i * j), end="")

#-------------------------------------------------
#13) 리스트 내포
# datas = []
# for i in range(0,10):
#     datas.append(i)
#
# print(datas)


# datas = [i for i in range(0,10)]
# print(datas)

# datas = [i*2 for i in range(0,10)]
# print(datas)

# datas = [i*3 for i in range(0,10) if i%2==0]
# print(datas)

# datas = []
# for i in range(0,10):
#     if i % 2 == 0:
#         datas.append((i*3))
# print(datas)


