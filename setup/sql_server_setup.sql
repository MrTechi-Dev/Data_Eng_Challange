CREATE TABLE CatLineasAereas (
    LineaAereaID INT PRIMARY KEY,
    Nombre VARCHAR(255),
    Codigo VARCHAR(10)
);

CREATE TABLE sucursal1_Pasajeros (
    PasajeroID INT PRIMARY KEY,
    Nombre VARCHAR(255),
    Apellido VARCHAR(255),
    Edad INT,
    VueloID INT
);

CREATE TABLE sucursal1_Vuelos (
    VueloID INT PRIMARY KEY,
    Origen VARCHAR(255),
    Destino VARCHAR(255),
    Fecha DATETIME,
    LineaAereaID INT
);

CREATE TABLE sucursal2_Pasajeros (
    PasajeroID INT PRIMARY KEY,
    Nombre VARCHAR(255),
    Apellido VARCHAR(255),
    Edad INT,
    VueloID INT
);

CREATE TABLE sucursal2_Vuelos (
    VueloID INT PRIMARY KEY,
    Origen VARCHAR(255),
    Destino VARCHAR(255),
    Fecha DATETIME,
    LineaAereaID INT
);


BULK INSERT CatLineasAereas
FROM '/home/rick/Documents/Data_Eng_Challange/data/central/CatLineasAereas.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);

BULK INSERT sucursal1_Pasajeros
FROM '/home/rick/Documents/Data_Eng_Challange/data/sucursal1/Pasajeros.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);

BULK INSERT sucursal1_Vuelos
FROM '/home/rick/Documents/Data_Eng_Challange/data/sucursal1/Vuelos.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);

BULK INSERT sucursal2_Pasajeros
FROM '/home/rick/Documents/Data_Eng_Challange/data/sucursal2/Pasajeros.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);

BULK INSERT sucursal2_Vuelos
FROM '/home/rick/Documents/Data_Eng_Challange/data/sucursal2/Vuelos.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
