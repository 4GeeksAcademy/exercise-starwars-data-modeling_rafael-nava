# Importación de los módulos necesarios
import os  # Permite interactuar con el sistema operativo
import sys  # Proporciona funciones y variables que se utilizan para manipular diferentes partes del entorno de Python
from sqlalchemy import Column, ForeignKey, Integer, String, Table  # Importa clases y funciones necesarias de SQLAlchemy
from sqlalchemy.orm import relationship, declarative_base  # Importa clases y funciones necesarias de SQLAlchemy
from sqlalchemy import create_engine  # Importa la función create_engine de SQLAlchemy para crear el motor de la base de datos
from eralchemy2 import render_er  # Importa la función render_er de eralchemy2 para generar el diagrama ER

# Declaración de la clase base para las clases de las entidades
Base = declarative_base()

# Definición de la tabla de asociación muchos a muchos entre Usuario y Favoritos
usuario_favoritos = Table('usuario_favoritos', Base.metadata, #Base.metadata en SQLAlchemy es un objeto que almacena metadatos sobre las tablas y sus columnas en una base de datos. Aquí te explico cómo funciona
    # Columna 'usuario_id' para almacenar el ID del usuario que tiene el favorito
    Column('usuario_id', Integer, ForeignKey('usuario.id')),
    # Columna 'favorito_id' para almacenar el ID del favorito asociado al usuario
    Column('favorito_id', Integer, ForeignKey('favoritos.id'))
)


# Definición de la entidad Usuario
class Usuario(Base):
    __tablename__ = 'usuario'  # Nombre de la tabla en la base de datos
    id = Column(Integer, primary_key=True)  # Define una columna para el ID del usuario
    nombre = Column(String(250), nullable=False)  # Define una columna para el nombre del usuario
    email = Column(String(250), nullable=False, unique=True)  # Define una columna para el correo electrónico del usuario, único
    password = Column(String(250), nullable=False)  # Define una columna para la contraseña del usuario
    # Relación uno a muchos con la tabla Favoritos
    favoritos = relationship("Favoritos", secondary=usuario_favoritos, back_populates="usuarios")  # Define la relación entre Usuario y Favoritos

# Definición de la entidad Favoritos
class Favoritos(Base):
    __tablename__ = 'favoritos'  # Nombre de la tabla en la base de datos
    id = Column(Integer, primary_key=True)  # Define una columna para el ID del favorito
    tipo = Column(String(50), nullable=False)  # Define una columna para el tipo de favorito (planeta, personaje, etc.)
    elemento_id = Column(Integer, nullable=False)  # Define una columna para el ID del elemento favorito
    # Relación muchos a muchos con la tabla Usuario
    usuarios = relationship("Usuario", secondary=usuario_favoritos, back_populates="favoritos")  # Define la relación entre Favoritos y Usuario

# Definición de la entidad Film
class Film(Base):
    __tablename__ = 'film'  # Nombre de la tabla en la base de datos
    id = Column(Integer, primary_key=True)  # Define una columna para el ID de la película
    title = Column(String(250), nullable=False)  # Define una columna para el título de la película
    #director = Column(String(250))  # Define una columna para el director de la película

# Definición de la entidad Specie
class Specie(Base):
    __tablename__ = 'specie'  # Nombre de la tabla en la base de datos
    id = Column(Integer, primary_key=True)  # Define una columna para el ID de la especie
    name = Column(String(250), nullable=False)  # Define una columna para el nombre de la especie

# Definición de la entidad Starship
class Starship(Base):
    __tablename__ = 'starship'  # Nombre de la tabla en la base de datos
    id = Column(Integer, primary_key=True)  # Define una columna para el ID de la nave espacial
    name = Column(String(250), nullable=False)  # Define una columna para el nombre de la nave espacial

# Definición de la entidad Vehicle
class Vehicle(Base):
    __tablename__ = 'vehicle'  # Nombre de la tabla en la base de datos
    id = Column(Integer, primary_key=True)  # Define una columna para el ID del vehículo
    name = Column(String(250), nullable=False)  # Define una columna para el nombre del vehículo

# Renderizar el diagrama ER
render_er(Base, 'diagram.png')  # Genera el diagrama ER y lo guarda como 'diagram.png'
