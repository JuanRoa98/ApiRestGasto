from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey


from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
#llamado a la base para crear tabla

Base=declarative_base()

#definir las tablas de mi  modelo 

#usuario

class Usuario(Base):
    __tablename__='Usuario'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombres=Column(String(50))
    fechaNacimiento=Column(Date)
    ubicacion=Column(String(100))
    metaAhorro=Column(Float)


class Gasto(Base):
    __tablename__='Gasto'
    id=Column(Integer, primary_key=True,autoincrement=True)
    descripcion=Column(String(150))
    categoria=Column(String(50))
    valor=Column(Float)
    fecha=Column(Date)

class Categoria(Base):
    __tablename__='Categoria'
    id=Column(Integer, primary_key=True,autoincrement=True)
    nombre=Column(String(50))
    descripcion=Column(String(150))
    fotoCategoria=Column(String(500))
    
class Ingreso(Base):
    __tablename__='Ingreso'
    id=Column(Integer, primary_key=True,autoincrement=True)
    valor=Column(Float)
    descripcion=Column(String(150))
    fecha=Column(Date)

