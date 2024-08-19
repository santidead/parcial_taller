-- Active: 1724040572737@@127.0.0.1@3309@Base_Ejemplo
create table jugadores(
    id_jugador int not null auto_increment,
    nombre varchar(50) not null,
    dorsal int not null,
    constraint Pk_Jugadores primary key(id_jugador) 
);

drop table jugadores;

insert into jugadores(nombre,dorsal)
values
    ('Jose',10)
;

delete from jugadores
where nombre = 'jose'
;

update jugadores
set dorsal = 9
where dorsal = 10
;