#Function2.py

x= 2
def func1(a):
    return x+a


#호출
print(func1(1))

def func2(a):
    x = 5
    return x + a

#호출
print(func2(1))

#불변형식을 내부에서 읽기+쓰기
g = 1
def testScope(a):
    global g
    g = 2
    return g+a
#호출
print(testScope(1))
print("전역변수 g:",g)

#기본값을 셋팅
def times(a=10,b=20):
    return a*b

#호출
print(times())
print(times(a=5))
print(times(3,4))

#키워드 인자(파라미터명을 명시)
def connectURI(sever,port):
    strURL = "http://" + server +":"+port
    return strURL

#호출
print(connectURI("bitCamp","80"))



