import streamlit as st
import pymysql
import pandas as pd
# 连接database
conn = pymysql.connect(
host="hadoop",
user="root",
password="123456",
database="sparktest",
charset="utf8")
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor() # 执行完毕返回的结果集默认以元组显示
# 定义要执行的SQL语句
sql = "select * from signup"
execute = cursor.execute(sql)
fetchmany = cursor.fetchmany(2)
print(fetchmany)
data = {'count':[fetchmany[0][1],fetchmany[1][1]]}
df = pd.DataFrame(data,index=[fetchmany[0][0],fetchmany[1][0]],columns=
['count'])
print(df)
st.bar_chart(df)
# 关闭光标对象
cursor.close()
# 关闭数据库连接
conn.close()