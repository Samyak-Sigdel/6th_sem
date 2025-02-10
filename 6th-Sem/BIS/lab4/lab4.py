import urllib.parse
import sqlalchemy as sq


server_name = "DESKTOP-VL101A9\\SQLEXPRESS"  
database_name = "BIS"

params = urllib.parse.quote_plus(
    f"Driver={{ODBC Driver 17 for SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    "Trusted_Connection=yes;"
)


connection_string = f"mssql+pyodbc:///?odbc_connect={params}"

try:
    # Create SQLAlchemy engine
    engine = sq.create_engine(connection_string, echo=False)
    # Test the connection
    with engine.connect() as connection:
        print("Connection Successful")
except Exception as e:
    print("Database connection failed:", e)
    exit()
