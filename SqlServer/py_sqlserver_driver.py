
# connection with sql-server

import pyodbc as con

"""Setup the connection string & query variables
Find the DRIVERS you have available by using the pyodbc.drivers() method"""

for i in con.drivers():
    print(i)
