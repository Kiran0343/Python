from sqlalchemy import create_engine
import pandas as pd

# connecting to MYSQl database
engine = create_engine('mysql+pymysql://root:Msatyam13$@localhost/python')
con = engine.connect()
#dropping table before creation if exists
con.execute("DROP TABLE IF EXISTS kiran")

# creatng table kiran
con.execute("CREATE TABLE kiran(id int8 not null primary key,name varchar(20) not null,city varchar(10) not null)")


# insering values into the table kiran
con.execute("INSERT INTO kiran VALUES(1,'kiran','hyd'),(2,'aditya','hyd'),(3,'abhi','hyd')")

# selecting data
data = con.execute("SELECT * FROM kiran")
data2 = pd.DataFrame(data.fetchall(),columns = data.keys())
print data2

# Deleting a row from the table
con.execute("DELETE FROM kiran WHERE id = 1")
data = con.execute("SELECT * FROM kiran")
data2 = pd.DataFrame(data.fetchall(),columns = data.keys())
print data2

#Updating a row in the table
con.execute("UPDATE kiran set name = 'aditya reddy' WHERE id = 2")
data = con.execute("SELECT * FROM kiran")
data2 = pd.DataFrame(data.fetchall(),columns = data.keys())
print data2

