from sqlalchemy import create_engine,event
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.engine import Engine




#datos para la coneccion a base de datos 

dataBaseName="gestor_de_venta"
userName="root"
userPassword=""
cocentionPort=3306
server="localhost"

#Creando la conexion
dataBaseConnection=f"mysql+mysqlconnector://{userName}:{userPassword}@{server}:{cocentionPort}/{dataBaseName}"

engine=create_engine(dataBaseConnection)
#abrir la session con la bd

SessionLocal=sessionmaker(autocommit=False,autoflush=False, bind=engine)



