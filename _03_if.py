# 1) if문
# ; 조건문
# 조건이 참(True)면 실행,
# 아니면 실행하지 않음

# 2) 간단 if 문
str_money = input('현재 금액은? ')   # 문자열 '1000'
money = int(str_money)             # 숫자    1000
if money >= 1200:
    print("빵 사먹을 수 있다 ^^")

# 3) if else문
str_money = input('현재 금액은? ')   # 문자열 '1000'
money = int(str_money)             # 숫자    1000
if money >= 1200:
    print("빵 사먹을 수 있다 ^^")
else:
    print("빵 못 사먹는다")


# 4) if elif else문
# ; 10000이상 케잌 사먹을 수 있다.
#   5000이상 담배 사 필 수 있다.
#   3000이상 콜라 마실 수 있다.
#   1200이상 빵 사먹을 수 있다.
#   1200미만 못 사먹는다.

# str_money = input('현재 금액은? ')   # 문자열 '1000'
# money = int(str_money)             # 숫자    1000
#
# if money >= 10000:
#     print("케잌 사먹을 수 있다.")
# elif money >= 5000:
#     print("담배 사 필 수 있다.")
# elif money >= 3000:
#     print("콜라 마실 수 있다.")
# elif money >= 1200:
#     print("빵 사먹을 수 있다.")
# else:
#     print("못 사먹는다.")

