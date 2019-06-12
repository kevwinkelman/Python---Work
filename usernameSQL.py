import pymssql

conn = pymssql.connect(server='TXPTCDBPRD16A\\KBWEB', user='kwinkelman', password='Papaya1299845!?', database='SOLD')
cursor = conn.cursor()

cursor.execute("select * from dbo.userinfo where Userid = 'calverio'")
row = cursor.fetchone()

conn.close()

print(row)