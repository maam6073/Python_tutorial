#딕셔너리


#키값과 벨류값 추가하기
a = {1 : 'ㅋㅋ'}

a = {1:'a'}
a[2]= 'b'
a['hello'] = 'world'

print(a)


#딕셔너리 요소 삭제하기
del a[1]
print(a)

#딕셔너리에서 Key사용해 Value 얻기
grade ={'pey' : 10 , 'julliet' : 99}
print(grade['pey'])
print(grade['julliet'])

#딕셔너리는 Key를 사용해서 Value를 구할 수 밖에 없다.
#딕셔너리의 Key는 고유한 값이므로 중복되는 Key값을 설정해
#놓으면 하나를 제외한 나머지 것들이 모두 무시된다는 점을 주의
#key값에 리스트를 쓸 수 없는데 이유는 키값은 변하면 안되기 때문
a = {1:'a', 1:'b'}
print(a)

#딕셔너리 관련 함수들
#Key 리스트 만들기(keys)
a= {'name':'pey','phone':'0119993323','birth':'1118'}
print(a.keys())

for k in a.keys():
    print(k)


#dict_keys 객체를 리스트로 변환하려면 다음과 같이 하면된다.
print(list(a.keys()))

#Value리스트 만들기(value)
print(a.values())

#Key,Value 쌍 얻기(items)
print(a.items())

#Key:Value 쌍 모두 지우기(clear)
print(a.clear())
print(a)


#Key로 Value얻기(get)
a= {'name':'pey','phone':'0119993323','birth':'1118'}
print(a.get('name'))

#딕셔너리 안에 찾으려는 key값이 없을 경우 미리 정해 둔 디폴트 값을 대신 가져오게
#하고 싶을 때에는 get(x,'디폴트 값')을 사용하면 편리하다.
print(a.get('foo','없다임마'))

#해당 Key가 딕셔너리 안에 있느지 조사하기(in)
print('name' in a)
print('joker' in a)



