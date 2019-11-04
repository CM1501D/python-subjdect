import pymysql
# print(pymysql)
def my_db(sql):
    db=pymysql.connect(
        host="localhost",
        user="root",
        passwd="lxfDOTA2",
        port=3306,
        db="lxf",
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)
    cursor=db.cursor()
    cursor.execute(sql)
    data=cursor.fetchone()
    return data
    print(data)
