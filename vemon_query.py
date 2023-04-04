DDL_QUERY = '''
    CREATE TABLE IF NOT EXISTS paisprocedencia (
    ID_procedencia int NOT NULL,
    pais varchar (200) null,
    siglas_pais varchar (200) null,
    pais_region varchar (200) null,
    PRIMARY KEY  (ID_procedencia)
);

CREATE TABLE IF NOT EXISTS atencion (
    ID_atencion int NOT NULL,
    diagnostico varchar (200) null,
    viruela_vacuna varchar (200) null,
    contacto_animales varchar (200) null,
    hospitalizado varchar (200) null,
    historia_viaje varchar (200) null,
    PRIMARY KEY  (ID_atencion)
);

CREATE TABLE IF NOT EXISTS paciente (
    ID_paciente int NOT NULL,
    correlativo numeric (9) null,
    edad_anios numeric (9) null,
    edad_meses numeric (9) null,
    genero varchar (200) null,
    orientacion_sexual varchar (200) null,
    PRIMARY KEY  (ID_paciente)
);

CREATE TABLE IF NOT EXISTS calendario (
    fecha date NOT NULL,
    year int NULL,
    month int NULL,
    day int NULL,
    week int NULL,
    PRIMARY KEY  (fecha)
);

CREATE TABLE IF NOT EXISTS factablemono (
    correlativo int NOT NULL,
    ID_atencion numeric (9),
    fecha varchar (15),
    ID_paciente numeric (9),
    ID_procedencia numeric (9),
    cantidad_casos numeric (9),
    porcentaje_positivos numeric (9),
    dias_infeccion numeric (9),
    promedio_dias_infeccion numeric (9),
    casos_semana numeric (9),
    PRIMARY KEY  (correlativo)
);
'''
