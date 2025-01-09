import time
from replicate_to_bigquery import replicate_table_to_bigquery
from config_loader import load_config


db_config = load_config('../config/db_config.json')
bq_config = load_config('../config/bigquery_config.json')

# Monitor 
def monitor_changes():
    while True:
        tables = [
            'CatLineasAereas',
            'sucursal1_Pasajeros',
            'sucursal1_Vuelos',
            'sucursal2_Pasajeros',
            'sucursal2_Vuelos',
        ]
        for table in tables:
            print(f"Checking changes for table {table}...")
            replicate_table_to_bigquery(table)
        print("Sleeping for 5 minutes...")
        time.sleep(300)  

monitor_changes()
