CREATE database typ_bd;

use typ_bd;

CREATE TABLE usuarios(
    id int primary key auto_increment,
    mail varchar(40),
    nombre varchar(40),
    clave varchar(30)
);

INSERT INTO usuarios (mail, nombre, clave) VALUES
('pepe@jose.com', 'Jose Pepe', '12344321'),
('tina@antonia.com', 'Maria Antonia', '1a2b3c4d5e');


select * from usuarios;