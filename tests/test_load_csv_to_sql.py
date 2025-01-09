import pytest
import pandas as pd
import pyodbc
from scripts.config_loader import load_config

# Load configuration
db_config = load_config('../config/db_config.json')

@pytest.fixture
def sql_connection():
    conn_str = (
        f"DRIVER={db_config['driver']};"
        f"SERVER={db_config['server']};"
        f"DATABASE={db_config['database']};"
        f"UID={db_config['username']};"
        f"PWD={db_config['password']}"
    )
    conn = pyodbc.connect(conn_str)
    yield conn
    conn.close()

def test_load_csv(sql_connection):
    cursor = sql_connection.cursor()
    test_data = pd.DataFrame({"PasajeroID": [1, 2], "Nombre": ["John", "Jane"], "Apellido": ["Doe", "Smith"], "Edad": [30, 25], "VueloID": [100, 101]})
    test_data.to_sql("TestTable", sql_connection, if_exists="replace", index=False)

    cursor.execute("SELECT COUNT(*) FROM TestTable")
    row_count = cursor.fetchone()[0]
    assert row_count == 2, "Data not loaded correctly into SQL Server."
