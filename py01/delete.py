import pymysql.cursors
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    db='test',
    charset='utf8'
)
print(connect)
cursor=connect.cursor()
sql="delete from trade where account='%s'"
data= '18012345678'
cursor.execute(sql % data)
connect.commit()
print('删除成功======》',cursor.rowcount)