import pymysql.cursors
connect = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    db='test',
    charset='utf8'
)
# 获取游标
cursor = connect.cursor()

# 插入数据
sql = "INSERT INTO trade (name, account, saving) VALUES ( '%s', '%s', %.2f )"
data = ('22dwws', '13812345678', 30000)
cursor.execute(sql % data)
connect.commit()
print('成功插入', cursor.rowcount, '条数据')