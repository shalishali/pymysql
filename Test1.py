import pymysql
#pymysql使用方法链接
#https://blog.csdn.net/qq_37176126/article/details/72824106

mydb = pymysql.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="123456"  # 数据库密码
)
#使用cursor()方法获取操作游标
#插入
mycursor = mydb.cursor()

sql_insert = """insert into user(id,username,password) values(4,'chent','1234')"""

try:
    mycursor.execute(sql_insert)
    # 提交
    mydb.commit()
except Exception as e:
    # 错误回滚
    mydb.rollback()
finally:
    mydb.close()