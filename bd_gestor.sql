
create database bd_gestor
CREATE TABLE IF NOT EXISTS roles (
    id_rol INT PRIMARY KEY AUTO_INCREMENT,
    nombre_rol VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nombre_usuario VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    contrasena_hash VARCHAR(256) NOT NULL,
    fecha_creacion DATETIME NOT NULL,
    id_rol INT NOT NULL,
    FOREIGN KEY (id_rol) REFERENCES roles (id_rol) ON DELETE CASCADE
);

INSERT IGNORE INTO roles (nombre_rol) VALUES ('administrador');
INSERT IGNORE INTO roles (nombre_rol) VALUES ('estandar');
