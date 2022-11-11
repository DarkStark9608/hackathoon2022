.headers ON

DROP TABLE IF EXISTS usuarios;
CREATE TABLE usuarios(
    iduser INTEGER PRIMARY KEY AUTOINCREMENT,
    username varchar(50) NOT NULL,
    apellidoP varchar(50) NOT NULL,
    apellidoM varchar(50) NOT NULL,
    sexo varchar(1),
    edad INTEGER,
    domicilio varchar(250) NOT NULL,
    telefono varchar(10),
    email varchar(30) NOT NULL,
    password varchar(32),
    fkTipo INTEGER
    );

INSERT INTO usuarios(username, apellidoP, apellidoM, sexo, edad, domicilio, telefono, email, password, fkTipo ) VALUES('admin', 'admin', 'admin', 'M', 20, 'admin', 'admin', 'admin', 'admin', 1);
INSERT INTO usuarios(username, apellidoP, apellidoM, sexo, edad, domicilio, telefono, email, password, fkTipo) VALUES('user', 'user', 'user', 'M', 20, 'user', 'user', 'user', 'user', 2);

DROP TABLE IF EXISTS catTipo;
CREATE TABLE catTipo(
    idTipo INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo varchar(50) NOT NULL
    );
INSERT INTO catTipo(tipo) VALUES('Administrador');
INSERT INTO catTipo(tipo) VALUES('Usuario');


DROP TABLE IF EXISTS denunciaEmpresa;
CREATE TABLE denunciaEmpresa(
    iddenunciaEmpresa INTEGER PRIMARY KEY AUTOINCREMENT,
    hora default CURRENT_TIMESTAMP,
    fecha default CURRENT_DATE,
    usuario varchar(7) NOT NULL,
    mensaje varchar(350) NOT NULL,
    evidencia BLOB 
    );
INSERT INTO denunciaEmpresa(usuario, mensaje, evidencia) VALUES('ANONIMO', 'ME PEGO BIEN FUERTE', 'FOTO.PNG');
INSERT INTO denunciaEmpresa(usuario, mensaje, evidencia) VALUES('ANONIMO', 'ME PEGO BIEN MAS O MENOS', 'FOTO.PNG');

DROP TABLE IF EXISTS catCategorias;
CREATE TABLE catCategorias(
    idcatCategorias INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion varchar(50) NOT NULL
);
INSERT INTO catCategorias(descripcion) VALUES('Amenazas');
INSERT INTO catCategorias(descripcion) VALUES('Acoso');
INSERT INTO catCategorias(descripcion) VALUES('Violacion');
INSERT INTO catCategorias(descripcion) VALUES('Agresion Fisica');
INSERT INTO catCategorias(descripcion) VALUES('Agresion Verbal');
INSERT INTO catCategorias(descripcion) VALUES('Hostigamiento laboral');
INSERT INTO catCategorias(descripcion) VALUES('Hostigamiento sexual');
INSERT INTO catCategorias(descripcion) VALUES('Discriminacion');
INSERT INTO catCategorias(descripcion) VALUES('Otros');


DROP TABLE IF EXISTS seguimiento;
CREATE TABLE seguimiento(
    idseguimiento INTEGER PRIMARY KEY AUTOINCREMENT,
    fkdenuncia INTEGER,
    fkusuario INTEGER,
    fecha default CURRENT_TIMESTAMP,
    hora default CURRENT_TIMESTAMP,
    fkInstancia integer,
    fkStatus integer
);

INSERT INTO seguimiento(fkdenuncia, fkusuario, fkInstancia, fkStatus) VALUES(1, 1, 1, 1);
INSERT INTO seguimiento(fkdenuncia, fkusuario, fkInstancia, fkStatus) VALUES(2, 1, 1, 1);

DROP TABLE IF EXISTS catInstancia;
CREATE TABLE catInstancia(
    idcatInstancia INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion varchar(100) NOT NULL,
    extension varchar(10),
    correo varchar(50)
);
INSERT INTO catInstancia(descripcion, extension, correo) VALUES('Secretaria de Trabajo', '1234', 'trabajo@mail.com');
INSERT INTO catInstancia(descripcion, extension, correo) VALUES('Secretaria de Gobernacion', '1234', 'gobierno@.mail.com');
INSERT INTO catInstancia(descripcion, extension, correo) VALUES('Psicologia', '1234', 'psicologia@mail.com');

DROP TABLE IF EXISTS catStatus;
CREATE TABLE catStatus(
    idcatStatus INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion varchar(15) NOT NULL
);

INSERT INTO catStatus(descripcion) VALUES('En proceso');
INSERT INTO catStatus(descripcion) VALUES('Resuelto');
INSERT INTO catStatus(descripcion) VALUES('Cancelado');
INSERT INTO catStatus(descripcion) VALUES('Pendiente');


