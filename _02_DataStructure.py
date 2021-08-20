#1) 컬렉션 = 자료구조 : 기본 자료형으로 제공
# datas = [0,1,2,3,4]          # List 순서가 있다.
# print(datas,type(datas))
# print(datas[2])
# datas = (0,1,2,3,4,10,9)     # Tuple
# print(datas,type(datas))
# print(datas[5])
# datas = {0,1,2,3,4}          # Set
# print(datas,type(datas))

# 리스트 : 순스서가 있는 자료구조
# #         삽입/삭제/추가에 편리한 구조
# #         인덱 개념이 존재한다


# 튜플 : 읽기전용 리스트
#       순서가 있다.
#       그러나 삽입/삭제/추가가안된다.

# 셋 : 집합
#     중복이 안된다.

# 2) List 구조
# 순서가 있는 구조
# 삽입/삭제가 편리한 구조
datas = [0,1,2,3,4]
print(datas[1])
datas.insert(2,10)
print(datas)

# 3) Tuple 구조
# 읽기 전용 리스트
# 순서가 있다.
# 다만 읽기만 가능
# 읽을 때는 List보다 속도가 빠르다고 알려져 있음
# 매개변수/여러 개 값을 묶어서 반환할 때
# datas = (1,2,3,4,5)
# print(datas[1])
# a = 10
# b = 20
# a,b = b,a  #=> (a,b) = (b,a)
# print(a,b)

# 4) set 구조
# 집합
# 합집합, 교집합, 차집합
# 순서가 없고, 중복도 안됨
# datas0 = {1,2,3,4,5}
# datas1 = {3,4,5,6,7}
# result = datas0.union(datas1)
# print(result)
# result = datas0.intersection(datas1)
# print(result)
# result = datas0 - datas1
# print(result)
#
# #5) 리스트 <-> 튜플 <-> 셋의 자유로운 상호변환
# datas = [1,2,3,4,5,9,10]
# print(datas,type(datas))
# tDatas = tuple(datas)
# print(tDatas,type(tDatas))
# sDatas = set(datas)
# print(sDatas, type(sDatas))
# lDatas = list(sDatas)
# print(lDatas,type(lDatas))
#
# datas = [1,2,3,4,5,9,10,2,1,3]
# print(datas)
# result = set(datas)
# print(result)
# datas = list(result)
# print(datas)

# 6) 딕셔너리 구조
# ; Map, Hash 구조
# key:value의 이중구조
# key로 검색해서 value를 찾는 구조
# 검색속도가 매우 빠른 구조

# datas = {1:'홍길동',2:'임꺽정',3:'장길산'}
# print(datas,type(datas))
# print(datas[1])
# print(datas['나이'])

# human = {'name':'albert',
#          'age' : 24,
#          'phone':'010-1111-2222'}
# print(human['name'])
# print(human['age'])
# print(human['phone'])


#7)비어있는 자료구조 선언
# datas = []
# print(type(datas))
# datas = list()
# print(type(datas))
# datas= ()
# print(type(datas))
# datas = tuple()
# print(type(datas))
# datas = {}
# print(type(datas))
# datas = dict()
# print(type(datas))
# datas = set()
# print(type(datas))

#

