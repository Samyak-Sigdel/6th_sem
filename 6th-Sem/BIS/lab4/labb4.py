import urllib.parse
import sqlalchemy as sq
import pandas as pd

# Server and database details
server_name = r"DESKTOP-VL101A9\SQLEXPRESS"  # Use raw string or double backslashes
database_name = "BIS"
table_name = "your_table_name"  # Replace with the desired table name
csv_file_path = r"E:\samyak\6th-Sem\6th-Sem\BIS\lab4\August,2024.xlsx"  # Replace with the full path to your CSV file

# Connection parameters
params = urllib.parse.quote_plus(
    f"Driver={{ODBC Driver 17 for SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    "Trusted_Connection=yes;"
)

# Connection string
connection_string = f"mssql+pyodbc:///?odbc_connect={params}"

try:
    # Create SQLAlchemy engine
    engine = sq.create_engine(connection_string, echo=False)
    
    # Test the connection
    with engine.connect() as connection:
        print("Connection Successful")
    
    # Read the CSV file with proper encoding
    # Try 'utf-8', and if it fails, switch to 'latin1' or 'ISO-8859-1'
    try:
        df = pd.read_csv(csv_file_path, encoding='utf-8')
    except UnicodeDecodeError:
        print("UTF-8 decoding failed. Retrying with 'latin1' encoding...")
        df = pd.read_csv(csv_file_path, encoding='latin1')
    
    print(f"CSV file read successfully with {len(df)} rows and columns: {list(df.columns)}")
    
    # Create table dynamically based on the DataFrame structure
    df.to_sql(table_name, con=engine, if_exists='fail', index=False)
    print(f"Table '{table_name}' created and data loaded successfully.")

except ValueError as ve:
    print(f"Table creation failed: {ve}")
    print("The table might already exist. Consider using 'if_exists=\"append\"' instead.")
except Exception as e:
    print("An error occurred:", e)
