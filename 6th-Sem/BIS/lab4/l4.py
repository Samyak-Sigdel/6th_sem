import os
import pandas as pd
import sqlalchemy as sq
import urllib

server_name = r"DESKTOP-VL101A9\SQLEXPRESS" 
database_name = "BIS"
directory_path = r"E:\samyak\6th-Sem\6th-Sem\BIS\lab4"  


params = urllib.parse.quote_plus(
    "Driver={ODBC Driver 17 for SQL Server};"
    f"Server={server_name};"
    f"Database={database_name};"
    "Trusted_Connection=yes;"
)
connection_string = f"mssql+pyodbc:///?odbc_connect={params}"


try:
    engine = sq.create_engine(connection_string, echo=False)
    engine.connect()
 
    print("Connection Sucessful")
except Exception as e:
    print("Database connection failed:", e)
    exit()

try:
    for file_name in os.listdir(directory_path):
        if file_name.endswith('.csv') or file_name.endswith('.xlsx'):
            file_path = os.path.join(directory_path, file_name)
            print(f"Importing file: {file_path}")

        
            if file_name.endswith('.csv'):
                df = pd.read_csv(file_path, dtype=str)
            else:  
                df = pd.read_excel(file_path, dtype=str)

    
            df = df.replace(",", "", regex=True)

    
            print(f"Number of records: {len(df)}")
            print("First few rows:")
            print(df.head())
            

    
            table_name = os.path.splitext(file_name)[0]


            df.to_sql(table_name, engine, index=False, if_exists='append')
            print(f"File {file_name} imported successfully into table '{table_name}'.")
except Exception as e:
    print("Error during file import:", e)

print("Files imported sucessfully")
