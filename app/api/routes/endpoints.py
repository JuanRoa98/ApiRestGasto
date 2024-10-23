from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends

from app.api.DTO.dtos import UsuarioDTOPeticion, UsuarioDTORespuesta
from app.api.DTO.dtos import GastoDTOPeticion,GastoDTORespuesta
from app.api.DTO.dtos import CategoriaDTOPeticion,CategoriaDTORespuesta
from app.api.DTO.dtos import IngresoDTOPeticion,IngresoDTORespuesta

from app.api.models.TablasSQL import Gasto
from app.api.models.TablasSQL import Categoria
from app.api.models.TablasSQL import Ingreso
from app.api.models.TablasSQL import Usuario
from app.database.configuration import SessionLocal, engine

rutas=APIRouter()

def conectarConBd():
    try:
        baseDatos=SessionLocal()
        yield baseDatos

    except Exception as error:
        baseDatos.rollback()
        raise

    finally:
        baseDatos.close()


#CONSTRUYENDO NUESTROS SERVICIOS
#CADA SERVICIO (OPERACION O TRANSACCION EN BD) DEBE PROGRAMARSE COMO UNA FUNCION 

#usuarios

@rutas.post("/usuario",response_model=UsuarioDTORespuesta, summary="Registrar un usuario en la base de datos")
def guardarUsuario(datosUsuario:UsuarioDTOPeticion, database:Session=Depends(conectarConBd)):
    try:
        usuario=Usuario(
            nombres=datosUsuario.nombres,
            fechaNacimiento=datosUsuario.fechaNacimiento,
            ubicacion=datosUsuario.ubicacion,
            metaAhorro=datosUsuario.metaAhorro
        )
        #ordenandole a la base de datos 
        database.add(usuario)
        database.commit()
        database.refresh(usuario)
        return usuario


    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"tenemos un problema{error}")
    

@rutas.get("/usuario", response_model=List[UsuarioDTORespuesta],summary="buscar todos los usuarios en bd")
def buscarUsuarios(database:Session=Depends(conectarConBd)):
    try:
        usuarios=database.query(Usuario).all()
        return usuarios

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"No se puede buscar los usuarios{error}")


#gastos

@rutas.post("/gatos",response_model=GastoDTORespuesta,summary="registrar un gatos")
def guardargastos(datosGastos:GastoDTOPeticion, database:Session=Depends(conectarConBd)):
    try:
        gasto=Gasto(
            descripcion=datosGastos.descripcion,
            categoria=datosGastos.categoria,
            valor=datosGastos.valor,
            fecha=datosGastos.fecha
            
        )
        #ordenandole a la base de datos 
        database.add(gasto)
        database.commit()
        database.refresh(gasto)
        return gasto
    
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"tenemos un problema{error}")

@rutas.get("/usuario", response_model=List[GastoDTORespuesta],summary="buscar todos los gatos en bd")
def buscargastos(database:Session=Depends(conectarConBd)):
    try:
        gastos=database.query(Gasto).all()
        return gastos

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"No se puede buscar los gatos{error}")
    

#categorias
@rutas.post("/categorias",response_model=CategoriaDTORespuesta,summary="registrar una categoria")
def guardarcategorias(datosCategoria:CategoriaDTOPeticion, database:Session=Depends(conectarConBd)):
     try:
        categoria=Categoria(
            nombre=datosCategoria.nombre,
            descripcion=datosCategoria.descripcion,
            fotoCategoria=datosCategoria.fotoCategoria 
        )
        #ordenandole a la base de datos 
        database.add(categoria)
        database.commit()
        database.refresh(categoria)
        return categoria
     
     except Exception as error:
         database.rollback()
         raise HTTPException(status_code=400, detail=f"tenemos un problema{error}")
     
@rutas.get("/categorias", response_model=List[CategoriaDTORespuesta],summary="buscar todos los usuarios en bd")
def buscarcategorias(database:Session=Depends(conectarConBd)):
    try:
        categorias=database.query(Categoria).all()
        return categorias
    
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"No se puede buscar las categorias{error}")
    


#ingreso
@rutas.post("/ingreso", response_model=IngresoDTORespuesta,summary="registrar el ingreso")
def guardaringreso(datosIngreso:IngresoDTOPeticion, database:Session=Depends(conectarConBd)):
    try:
        ingreso=Ingreso(
            valor=datosIngreso.valor,
            descripcion=datosIngreso.descripcion,
            fecha=datosIngreso.fecha
        )
        #ordenandole a la base de datos 
        database.add(ingreso)
        database.commit()
        database.refresh(ingreso)
        return ingreso
    
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"tenemos un problema{error}")

@rutas.get("/ingreso", response_model=List[IngresoDTORespuesta],summary="buscar todos los usuarios en bd")
def buscaringreso(database:Session=Depends(conectarConBd)):
    try:
        Ingreso=database.query(Categoria).all()
        return Ingreso
    
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"No se puede buscar las categorias{error}")
                   





    
