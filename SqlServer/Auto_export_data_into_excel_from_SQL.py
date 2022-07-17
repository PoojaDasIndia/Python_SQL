import pyodbc
import pandas as pd
from datetime import datetime
import os
from plyer import notification
print(os.getcwd())
# create sql

myclient = pyodbc.connect(driver='{SQL Server};',
                          host=r'DODO-7\SQLEXPRESS',
                          UID='DODO-7',
                          PWD="poojadas123",
                          database="OrderDB",
                          trusted_connection="yes")
    



query="SELECT * FROM DBO.Orders WHERE City='Seattle';"

# Getting the data from SQL into pandas DataFrame

df = pd.read_sql(sql=query, con=myclient)

# Export the data on the desktop

filepath=os.environ["userprofile"]+"\\Desktop\\Database\\"+"SQL_OrderData_"+datetime.now().strftime("%d-%b-%Y %H%M%S")+".csv"

df.to_csv(filepath, index=False)


# Display  notification to user

notification.notify(title="Report Status !!!",message=f"Sales data has been successfully save into Excel \nTotal Rows:{df.shape[0]}\nTotal Columns:{df.shape[1]}",timeout=10)






