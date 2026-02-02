DROP mercedes;
CREATE DATABASE mercedes;
CREATE USER 'sergio'@'localhost' IDENTIFIED BY 'P@ssw0rd!';
CREATE TABLE usuarios (
    usuarios VARCHAR2(100),
    mail VARCHAR2(150)
);
 
INSERT INTO usuarios (usaurios, mail)
VALUES ('sergio', 'sergio@example.com');

INSERT INTO usuarios (usaurios, mail)
VALUES ('maria', 'maria@example.com');

INSERT INTO usuarios (usaurios, mail)
VALUES ('juan', 'juan@example.com');
