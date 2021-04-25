import pymysql

db = pymysql.connect(host='127.1.27.1',port=3306,user='root',password='T0iRStniPd')

#创建一个cursor对象
cursor = db.cursor()
#sql语句打印版本号
sql = 'select version()'
#执行sql语句
cursor.execute(sql)
#获取返回的信息
data = cursor.fetchone()
print(data)
#断开连接
cursor.close()
db.close()