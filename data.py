
import psycopg2
def table_create():

    conn=psycopg2.connect(dbname="ak47db",
                        user="postgres",
                        password="shiva2006",
                        port="5432",
                        host="localhost")
    cur=conn.cursor()
    cur.execute("drop table if exists aks;")
    cur.execute("""create table  aks(
                id serial primary key,
                name text,address text,
                age int,
                number text);
                """)
    print("aks table is created")
    conn.commit()
    conn.close()
def insert_data():
        
        conn=psycopg2.connect(dbname="ak47db",
                        user="postgres",
                        password="shiva2006",
                        port="5432",
                        host="localhost")
        cur=conn.cursor()
        name=input("enter the name :-")
        address=input("enter the address :-")
        age=input("enter the age :-")
        number=input("enter the number :-")
        cur.execute("insert into aks(name,address,age,number) values(%s,%s,%s,%s)",(name,address,age,number))
        print("data inserted successfully")
        conn.commit()
        conn.close()
def update_data():
      id=input("enter the id number you want to update:- ")
      conn=psycopg2.connect(dbname="ak47db",
                        user="postgres",
                        password="shiva2006",
                        port="5432",
                        host="localhost")
      cur=conn.cursor()
      
    
      fields={
            "1":("name","enter new name:- "),
            "2":("address","enter new address:-"),
            "3":("age","enter new age :- "),
            "4":("number","enter new number:- ")

    }
      print("which field would you like to update")
      for key in fields:
            print(f"{key} , {fields[key][0]}")
      field_choice=input("enter the no of field which you want to update:- ")
      if field_choice in fields:
            field_name ,prompt=fields[field_choice]
            print(field_name,prompt)
            new_value=input(prompt)
            sql=f"update aks set {field_name} =%s where id=%s"
            cur.execute(sql,(new_value,id))
            print(f"{field_name} is updated successful ")
      else:
            print("invalid key ") 
      conn.commit()
      conn.close()
update_data()