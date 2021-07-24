#리스트는 어떻게 만들고 사용할까?

odd = [1,3,5,7,9]
print(odd[0])

strodd = ["life","is","too","short"]
print(strodd[1])
a = list()


a = [1,2,3,['a','b','c']]
print(a[3][0])

a = [1,2,['a','b','c',['life','is']]]
print(a[2][3][0])

a = [1,2,3,['a','b','c'],4,5]
print(a[2:5])
print(a[3][:2])


a = [1,2,3]
b = [4,5,6]
#리스트 사이에서 + 기호는 2개의 리스틀르 합치는 기능을 한다.
print(a+b)


a = [1,2,3]
#리스트에서 *는 반복하기에 사용된다.
print(a*3)
print(len(a))


#append 리스트에 요소 추가 함수
a.append(4)
print(a)

a.append([5,6])
print(a)

a = [1,5,2,3,7,4]

#리스트를 정렬시켜주는 함수
a.sort()
print(a)


#리스트 뒤집기(reverse)
a = ['a','c','d']
a.reverse();
print(a)

#위치 반환(인덱스번호를 알려줌)
a = [1,2,3]
print(a.index(3))

#요소 삽입(insert)
a.insert(0,4)
print(a)

#리스트 요소 제거(remove)
a = [1,2,3]
a.remove(2)
print(a)

#리스트 요소 끄집어내기(pop)
a = [1,2,3]
print(a.pop())#그냥 쓰면 맨뒤에 인덱스빼버리고 삭제
# 안에 번호 넣으면 그 해당인덱스를 뽑아내고 삭제제print(a)

#리스트에 포함된 요소 x의 개수 세기(count)
a = [1,2,3,2,2,2]
print(a.count(2))

#리스트 확장(extend)
a = [1,2,3]
a.extend([4,5])
print(a)
b=[6,7]
a.extend(b)
print(a)