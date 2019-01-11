import pymysql.cursors

connect=pymysql.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='root',
    db='test',
    charset='utf8'
)
cursor=connect.cursor()
sql1="update trade set name='%s' where account='%s'"
data1=('墨镜111','18012345678')
cursor.execute(sql1 % data1)
connect.commit()
print("修改成功===》",cursor.rowcount)