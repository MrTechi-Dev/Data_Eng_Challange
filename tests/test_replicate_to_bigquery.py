import pytest
import pandas as pd
from google.cloud import bigquery
from scripts.config_loader import load_config

# Load BigQuery configuration
bq_config = load_config('../config/bigquery_config.json')

@pytest.fixture
def bigquery_client():
    client = bigquery.Client.from_service_account_json(bq_config["credentials_file"])
    yield client

def test_replicate_to_bigquery(bigquery_client):
    test_data = pd.DataFrame({"PasajeroID": [1, 2], "Nombre": ["John", "Jane"], "Apellido": ["Doe", "Smith"], "Edad": [30, 25], "VueloID": [100, 101]})
    table_id = f"{bq_config['project_id']}.{bq_config['dataset_id']}.TestTable"

    job = bigquery_client.load_table_from_dataframe(test_data, table_id)
    job.result()  # Wait for the job to complete

    table = bigquery_client.get_table(table_id)
    assert table.num_rows == 2, "Data not loaded correctly into BigQuery."
