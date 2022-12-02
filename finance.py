import pymysql as ps 
con = ps.connect(host='localhost',user='root',password='mew20188',db='income_statement')
cs = con.cursor() 
cs.execute('''CREATE TABLE ''') 
con.commit()
cs.close() 
con.close()