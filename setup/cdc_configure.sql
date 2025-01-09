-- Habilita CDC en la base de datos
EXEC sys.sp_cdc_enable_db;

-- Habilita CDC para cada tabla
EXEC sys.sp_cdc_enable_table
    @source_schema = 'dbo',
    @source_name = 'CatLineasAereas',
    @role_name = NULL;

EXEC sys.sp_cdc_enable_table
    @source_schema = 'dbo',
    @source_name = 'sucursal1_Pasajeros',
    @role_name = NULL;

EXEC sys.sp_cdc_enable_table
    @source_schema = 'dbo',
    @source_name = 'sucursal1_Vuelos',
    @role_name = NULL;

EXEC sys.sp_cdc_enable_table
    @source_schema = 'dbo',
    @source_name = 'sucursal2_Pasajeros',
    @role_name = NULL;

EXEC sys.sp_cdc_enable_table
    @source_schema = 'dbo',
    @source_name = 'sucursal2_Vuelos',
    @role_name = NULL;
