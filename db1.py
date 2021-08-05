#db1.py
import sqlite3

#연결객체 생성(일단은 메모리에 임시로 저장)
#con = sqlite3.connect(":memory")
#구문을 수행할 커서 객체를 생성
cur = sqlite3.cursor("c:\\work\\test.db")
#데이터를 담을 테이블을 생성
cur.execute("create table PhoneBook (name text, phoneNum text);")
#1건을 입력
cur.execute("insert into PhoneBook values ('derick','010-111');")
#입력 파라미터 처리
name = "gildong"
phoneNumber ="010-222"
cur.execute("insert into PhoneBook values (?,?);",(name,phoneNumber))
#다중의 레코드(데이터를 입력하는 경우)
datalist =(("tom","010-123"),("dsp","010-454"))
cur.excutemany("insert into PhoneBook values(?,?);",datalist)

#결과를 검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)

#정상적으로 작업 완료
con.commit()