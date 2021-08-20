# 1_ while문
# ~동안
# 값이 True인 동안
# 계속 반복

# while True:
#     str_money = input('현재 금액은? ')  # 문자열 '1000'
#     money = int(str_money)  # 숫자    1000
#
#     if money >= 10000:
#         print("케잌 사먹을 수 있다.")
#     elif money >= 5000:
#         print("담배 사 필 수 있다.")
#     elif money >= 3000:
#         print("콜라 마실 수 있다.")
#     elif money >= 1200:
#         print("빵 사먹을 수 있다.")
#     else:
#         print("못 사먹는다.")

#2) while문의 필요성
#나무를 10번 찍고 싶다.
# print("나무를 1번 찍는다.")
# print("나무를 2번 찍는다.")
# print("나무를 3번 찍는다.")
# print("나무를 4번 찍는다.")
# print("나무를 5번 찍는다.")
# print("나무를 6번 찍는다.")
# print("나무를 7번 찍는다.")
# print("나무를 8번 찍는다.")
# print("나무를 9번 찍는다.")
# print("나무를 10번 찍는다.")

#3) 규칙성 찾기
# num = 1
# print("나무를 {0}번 찍는다.".format(num)); num += 1
# print("나무를 {0}번 찍는다.".format(num)); num += 1
# print("나무를 {0}번 찍는다.".format(num)); num += 1
# print("나무를 {0}번 찍는다.".format(num)); num += 1
# print("나무를 {0}번 찍는다.".format(num)); num += 1
# print("나무를 {0}번 찍는다.".format(num)); num += 1
# print("나무를 {0}번 찍는다.".format(num)); num += 1
# print("나무를 {0}번 찍는다.".format(num)); num += 1
# print("나무를 {0}번 찍는다.".format(num)); num += 1
# print("나무를 {0}번 찍는다.".format(num)); num += 1
# print("나무를 {0}번 찍는다.".format(num)); num += 1

#4) 규칙성을 반복문에 적용하기
# num = 1
# while num <= 10:
#     print("나무를 {0}번 찍는다.".format(num))
#     num += 1

#5) 10000번으로 늘려보자
num = 1
while num <= 10000:
    print("나무를 {0}번 찍는다.".format(num))
    num += 1

#6) 무한루프 탈출하기
while True:
    money = int(input('현재 금액은? '))  # 문자열 '1000'
    if money == -1:
        print("탈출!")
        break

    if money >= 10000:
        print("케잌 사먹을 수 있다.")
    elif money >= 5000:
        print("담배 사 필 수 있다.")
    elif money >= 3000:
        print("콜라 마실 수 있다.")
    elif money >= 1200:
        print("빵 사먹을 수 있다.")
    else:
        print("못 사먹는다.")
        
print('end')