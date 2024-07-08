import pandas as pd
from sqlalchemy import create_engine, Table, Column, Integer, String, Float, BigInteger, Date, MetaData, Index
from datetime import datetime, timedelta

# Load Type {fl/inc}
loadType = "fl"

# Prepare csv file path
if(loadType == "fl"):
    filePath = 'historical_data.csv'
else:
    # Get Yesterday Date
    yesterday = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
    filePath = f'stock_data_{yesterday}.csv'

# MySQL database configuration
DB_user = 'sql12718512'
DB_pswrd = 'RN68QN1ymB'
DB_host = 'sql12.freesqldatabase.com'
DB_name = 'sql12718512'
table_name = 'stocks'

# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine(f'mysql+pymysql://{DB_user}:{DB_pswrd}@{DB_host}/{DB_name}')

# Create metadata object
metadata = MetaData()

# Define the table schema
stock_data = Table(table_name, metadata,
    Column('id', Integer, primary_key=True),
    Column('date', Date),
    Column('company', String(255)),
    Column('open', Float),
    Column('close', Float),
    Column('high', Float),
    Column('low', Float),
    Column('volume', BigInteger)
)

# Define indexes
Index('idx_date_company', stock_data.c.date, stock_data.c.company)

# Create the table with indexes
metadata.create_all(engine)

# Load CSV data into pandas DataFrame
DF = pd.read_csv(filePath)

try:
    # Write to SQL server
    DF.to_sql(table_name, con=engine, if_exists='append', index=False)
except Exception as e:
    # Print error
    print(f"Error: {str(e)}")
finally:
    # Close connection
    engine.dispose()