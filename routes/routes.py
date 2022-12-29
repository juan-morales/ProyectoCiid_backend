from fastapi import APIRouter, HTTPException, Response ,status, Header
from conf.db import con
from schemas.provincia import Provincia
from schemas.persona import Persona
from models.persona import personas
from models.provincia import provincias

route = APIRouter() 

@route.get('/')
def get_home():
    return{
        "status": True,
        "message": "Bienvenido a la api"
    }
    
    ''' ---------- PROVINCIAS ---------- '''
    
    
''' LISTAR PROVINCIAS '''
@route.get("/provincias", tags=["Provincias"])
def get_all_provincia():
    return con.execute(provincias.select()).fetchall() 


''' AGREGAR PROVINCIA '''
@route.post("/provincias", tags=["Provincias"])
def create_user(pcia: Provincia):
    print(pcia)
    new_pcia = {"name": pcia.name}
    print(new_pcia)
    result = con.execute(provincias.insert().values(new_pcia))
    print(result.lastrowid)
    ''' DEVUELVE EL OBJETO CREADO return con.execute(users.select().where(users.c.id == result.lastrowid)).first() '''
    return {
        "success": True,
        "message": "Se agrego la provincia"
    } 
    

''' SELECCIONA UNA PROVINCIA '''
@route.get("/provincias/{id}", tags=["Provincias"])
def get_single_provincia(id:int):
    result = con.execute(provincias.select().where(provincias.c.id == id)).first()
    if(result):
        return result
    else:
        raise HTTPException(status_code=404, detail="Provincia no fue encontrada") 


''' BORRA UNA PROVINCIA JUNTO A SUS PERSONAS '''
@route.delete("/provincias/{id}", tags=["Provincias"])
def delete_provincia(id:str):
    con.execute(personas.delete().where(personas.c.provincia_id == id))
    result = con.execute(provincias.delete().where(provincias.c.id == id))
    return {
        "success": True,
        "message": "Provincia eliminada"
    } 

''' MODIFICAR UNA PROVINCIA '''
@route.put("/provincias/{id}", tags=["Provincias"])
def update_user(id:int, pcia: Provincia):


    con.execute(provincias.update().values(name = pcia.name).where(provincias.c.id == id))
    return {
        "success": True,
        "message": "Se modifico los datos de la provincia"
    } 
    
    






''' ---------- PERSONAS --------'''


@route.get("/personas", tags=["Personas"])
def get_all_personas():
    return con.execute(personas.select()).fetchall()
    


''' AGREGAR PERSONA '''
@route.post("/personas", tags=["Personas"])
def create_persona(persona: Persona):
    new_persona = {"apellido": persona.apellido,"nombre": persona.nombre,"dni": persona.dni,
                "fechaNac": persona.fechaNac,"direccion": persona.direccion,"provincia_id": persona.provincia_id}
    result = con.execute(personas.insert().values(new_persona))
    print(result.lastrowid)
    ''' DEVUELVE EL OBJETO CREADO return con.execute(users.select().where(users.c.id == result.lastrowid)).first() '''
    return {
        "success": True,
        "message": "Se agrego la persona"
    } 
    

''' SELECCIONA UNA PERSONA '''
@route.get("/personas/{id}", tags=["Personas"])
def get_single_personsa(id:int):
    result = con.execute(personas.select().where(personas.c.id == id)).first()
    if(result):
        return result
    else:
        raise HTTPException(status_code=404, detail="Persona no fue encontrada") 


''' BORRA UNA PERSONA '''
@route.delete("/personas/{id}", tags=["Personas"])
def delete_persona(id:str):
    con.execute(personas.delete().where(personas.c.id == id))
    return {
        "success": True,
        "message": "Persona eliminada"
    } 


''' MODIFICAR UNA PERSONA '''
@route.put("/personas/{id}", tags=["Personas"])
def update_persona(id:int, persona: Persona):

    con.execute(personas.update().values(apellido = persona.apellido,
    nombre = persona.nombre, dni = persona.dni, fechaNac = persona.fechaNac,
    direccion = persona.direccion, provincia_id = persona.provincia_id).where(personas.c.id == id))
    return {
        "success": True,
        "message": "Se modifico los datos de la persona"
    } 
    