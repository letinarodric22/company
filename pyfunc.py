import psycopg2


try:
    conn = psycopg2.connect("dbname= company user=postgres password=1234")
    cur =conn.cursor()
except Exception as e:
    print(e)    

def fetch_data(tbname):
    try:
        q = "SELECT * FROM " + tbname + ";"
        cur.execute(q)
        records = cur.fetchall()
        return records 
    except Exception as e:
        return e
    
def insert_customer(v):
    vs = str(v)
    q = "insert into customer(id, firstname, lastname, email, phone) "\
        "values" + vs
    cur.execute(q)
    conn.commit()
    return q