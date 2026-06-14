import psycopg2
def table():
    conn = psycopg2.connect(host ="localhost",
                            dbname="postgres",
                            user ="postgres",
                            password ="QWERTYUIOP",
                            port = 5432)
    cur =conn.cursor()
    cur.execute('''create table employees(Name text,Id int,Age int);''')
    print("Table created Successfully") 
    conn.commit()
    conn.close()

def data():
    conn = psycopg2.connect(host ="localhost",
                            dbname="postgres",
                            user ="postgres",
                            password ="QWERTYUIOP",
                            port = 5432)
    cur =conn.cursor()
    cur.execute("""insert into employees values
    ('Mohit',47,21),
    ('Akash',18,22),
    ('Rahul',13,20),
    ('Sandeep',14,21);""")
    print("Data Inserted Successfully")
    conn.commit()
    conn.close()


def extract():
    conn = psycopg2.connect(host ="localhost",
                            dbname="postgres",
                            user ="postgres",
                            password ="QWERTYUIOP",
                            port = 5432)
    cur =conn.cursor()
    cur.execute("select * from employees;")
    show =cur.fetchone()
    print(show[1])
    print("Data Extracted Successfully")
    conn.commit()
    conn.close()

def user_input_data():
    conn = psycopg2.connect(host ="localhost",
                            dbname="postgres",
                            user ="postgres",
                            password ="QWERTYUIOP",
                            port = 5432)
    cur =conn.cursor()
    name=input("Enter name of the employee: ")
    id=int(input("Enter id of the employee: "))
    age=int(input("Enter age of the employee: "))
    query ='''insert into employees(Name,Id,Age) values(%s,%s,%s);'''
    cur.execute(query,(name,id,age))
    print("Data Inserted Successfully")
    conn.commit()
    conn.close()
# table()
# data()
# extract()
user_input_data()