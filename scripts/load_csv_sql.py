import pandas as pd
import pyodbc
from config_loader import load_config

# Load database configuration
db_config = load_config('../config/db_config.json')

# Create connection
conn_str = (
    f"DRIVER={db_config['driver']};"
    f"SERVER={db_config['server']};"
    f"DATABASE={db_config['database']};"
    f"UID={db_config['username']};"
    f"PWD={db_config['password']}"
)

#connection
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Load CSVs into SQL Server
def load_csv_to_sql(file_path, table_name):
    df = pd.read_csv(file_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    print(f"Data loaded into {table_name}")

# Load central and sucursal CSVs
load_csv_to_sql('../data/central/CatLineasAereas.csv', 'CatLineasAereas')
load_csv_to_sql('../data/sucursal1/Pasajeros.csv', 'sucursal1_Pasajeros')
load_csv_to_sql('../data/sucursal1/Vuelos.csv', 'sucursal1_Vuelos')
load_csv_to_sql('../data/sucursal2/Pasajeros.csv', 'sucursal2_Pasajeros')
load_csv_to_sql('../data/sucursal2/Vuelos.csv', 'sucursal2_Vuelos')
