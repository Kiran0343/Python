from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('mysql://root:Msatyam13$@localhost/python')
con = engine.connect()
con.execute("DROP TABLE IF EXISTS kiran")

con.execute("CREATE TABLE kiran(id int8 not null primary key,name varchar(20) not null,city varchar(10) not null)")

con.execute("INSERT INTO kiran VALUES(1,'kiran','hyd'),(2,'aditya','hyd'),(3,'abhi','hyd')")

data = con.execute("SELECT * FROM kiran")
data2 = pd.DataFrame(data.fetchall(),columns = data.keys())
print data2

con.execute("DELETE FROM kiran WHERE id = 1")
data = con.execute("SELECT * FROM kiran")
data2 = pd.DataFrame(data.fetchall(),columns = data.keys())
print data2

con.execute("UPDATE kiran set name = 'aditya reddy' WHERE id = 2")
data = con.execute("SELECT * FROM kiran")
data2 = pd.DataFrame(data.fetchall(),columns = data.keys())
print data2