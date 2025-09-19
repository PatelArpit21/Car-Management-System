import mysql.connector as conn

def fetch_data(query):
    connection=conn.connect(host='localhost',user='root',password='',database='Car_dekho')
    cur=connection.cursor();
    cur.execute(query)
    return cur.fetchall()
    
def insert_data(query):
    connection=conn.connect(host='localhost',user='root',password='',database='Car_dekho')
    cur=connection.cursor();
    cur.execute(query)
    connection.commit()
    connection.close()

def change_data(query):
    connection=conn.connect(host='localhost',user='root',password='',database='Car_dekho')
    cur=connection.cursor();
    cur.execute(query)
    connection.commit()
    connection.close()