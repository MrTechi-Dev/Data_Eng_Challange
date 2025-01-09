from unittest.mock import MagicMock
from scripts.monitor_changes import monitor_changes

def test_monitor_changes():
    mock_sql_server = MagicMock()
    mock_bigquery = MagicMock()

    # Simulate changes in SQL Server
    mock_sql_server.query.return_value = [
        {"PasajeroID": 1, "Nombre": "John", "Apellido": "Doe", "Edad": 30, "VueloID": 100},
        {"PasajeroID": 2, "Nombre": "Jane", "Apellido": "Smith", "Edad": 25, "VueloID": 101}
    ]

    # Simulate BigQuery replication
    mock_bigquery.load_table_from_dataframe.return_value = None

    monitor_changes(mock_sql_server, mock_bigquery)
    mock_sql_server.query.assert_called()
    mock_bigquery.load_table_from_dataframe.assert_called()
