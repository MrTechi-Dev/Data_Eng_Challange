from google.cloud import bigquery
import pandas as pd
from sqlalchemy import create_engine
from config_loader import load_config

# Load configurations
db_config = load_config('../config/db_config.json')
bq_config = load_config('../config/bigquery_config.json')

# Create  connection
db_conn_str = (
    f"mssql+pyodbc://{db_config['username']}:{db_config['password']}@"
    f"{db_config['server']}/{db_config['database']}?driver=ODBC+Driver+17+for+SQL+Server"
)
engine = create_engine(db_conn_str)

# Set up BigQuery
client = bigquery.Client.from_service_account_json(bq_config['credentials_file'])

# Replicate
def replicate_table_to_bigquery(table_name):
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, engine)
    table_id = f"{bq_config['project_id']}.{bq_config['dataset_id']}.{bq_config['table_prefix']}{table_name}"
    job = client.load_table_from_dataframe(df, table_id)
    job.result()  # Wait for the job to complete
    print(f"Table {table_name} replicated to BigQuery.")


tables = [
    'CatLineasAereas',
    'sucursal1_Pasajeros',
    'sucursal1_Vuelos',
    'sucursal2_Pasajeros',
    'sucursal2_Vuelos',
]
for table in tables:
    replicate_table_to_bigquery(table)
