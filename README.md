# Data_Eng_Challange
Data Engineer challange for Acero


# Data Replication from SQL Server to BigQuery

## Descripción
Este proyecto implementa un flujo de datos desde bases de datos SQL Server hacia BigQuery utilizando Change Data Capture (CDC).

## Estructura
- **`setup/`**: Scripts de configuración para SQL Server.
- **`scripts/`**: Scripts Python para carga, replicación y monitoreo.
- **`config/`**: Configuraciones para bases de datos y BigQuery.
- **`diagrams/`**: Diagramas de arquitectura.
- **`tests/`**: Scripts de prueba automatizada.
- **`data/`**: Archivos CSV de datos originales.

## Requisitos
- Python 3.8+
- Google Cloud SDK configurado
- SQL Server habilitado para CDC

## Instalación
1. Clona este repositorio.
2. Instala dependencias:
   ```bash
   pip install -r requirements.txt
