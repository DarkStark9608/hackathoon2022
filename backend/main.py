from fastapi import Depends, FastAPI , HTTPException, status, Security
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware
from typing import List

import sqlite3 
import os 
from typing import List 
from fastapi import Depends, FastAPI, HTTPException, status 
from fastapi.security import HTTPBasic, HTTPBasicCredentials 
from pydantic import BaseModel 
from typing import Union  


app = FastAPI()

DATABASE_URL = os.path.join("sql/bd.sqlite") # Path to the database file

origins = [
    "http://0.0.0.0:8000/",
    "http://0.0.0.0:8080/",
    "*",   
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

security = HTTPBasic()
security_bearer = HTTPBearer()

class Usuario1(BaseModel):
    nombre: str
    apellidoP: str
    apellidoM: str
    sexo: str
    edad: int
    domicilio: str
    telefono: str
    correo: str
    contrasena: str
    tipo: int

class Usuario (BaseModel):  
    iduser: int  
    username: str  
    apellidoP: str
    apellidoM: str
    sexo: str
    edad: int
    domicilio :str
    telefono: str
    email: str
    password : str
    fkTipo: int


class CatTipo(BaseModel):
    tipo: str

class Denuncia_empresa (BaseModel):
    usuario: str
    mensaje: str
    evidencia : str

class catStatus (BaseModel):
    descripcion: str

class Seguimiento(BaseModel):
    id_denuncia: int
    id_usuario: int 
    id_instancia: int
    id_estatus: int

class Seguimiento():
    id_denuncia: int
    id_usuario: int 
    id_instancia: int
    id_estatus: int

class Instancia(BaseModel):
    descripcion: str
    extension: str
    correo: str

class Respuesta (BaseModel) :  
    message: str  




@app.get("/")
def root():
    return {"message": "Esta es una API de Seguridad empresarial"}

#inserta a un usuario

@app.post(
    "/usuario", 
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Inserta un usuario",
    description ="Inserta un usuario",
    tags=["User"]
)
def inserta_usuario(usuario: Usuario1):
    try:
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (username, apellidoP, apellidoM, sexo, edad, domicilio, telefono, email, password, fkTipo) VALUES (?,?,?,?,?,?,?,?,?,?)", (usuario.nombre, usuario.apellidoP, usuario.apellidoM, usuario.sexo, usuario.edad, usuario.domicilio, usuario.telefono, usuario.correo, usuario.contrasena, usuario.tipo))
        conn.commit()
        conn.close()
        return {"message": "Usuario insertado"}
    except Exception as e:
        print(e)
        return {"message": "Error al insertar el usuario"}


#obtiene todos los usuarios

@app.get(
    "/usuario",    response_model=List[Usuario],
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Obtiene todos los usuarios",
    description ="Obtiene todos los usuarios",
    tags=["User"]

)
def get_usuarios():
    try:
        conn = sqlite3.connect(DATABASE_URL) 
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        conn.close()
        return usuarios
    except:
        return {"message": "Error al obtener los usuarios"}

#obtiene un usuario por id

@app.get(
    "/usuario/{id}",   response_model=List[Usuario],
    status_code=status.HTTP_200_OK,
    summary     ="Obtiene un usuario por id",
    description ="Obtiene un usuario por id",
    tags=["User"]
)
def get_usuario(email: str):
    try:
        conn = sqlite3.connect(DATABASE_URL)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        usuario = cursor.fetchall()
        conn.close()
        return usuario
    except Exception as e:
        print(e)
        return {"message": "Error al obtener el usuario"}

#actualiza un usuario

@app.put(
    "/usuario/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Actualiza un usuario",
    description ="Actualiza un usuario",
    tags=["User"]
)
def update_usuario(usuario: Usuario):
    try:
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("UPDATE usuarios SET username = ?, apellidoP = ?, apellidoM = ?, sexo = ?, edad = ?, domicilio = ?, telefono = ?, email = ?, password = ?, fkTipo = ? WHERE email = ?", (usuario.username, usuario.apellidoP, usuario.apellidoM, usuario.sexo, usuario.edad, usuario.domicilio, usuario.telefono, usuario.email, usuario.password, usuario.fkTipo, usuario.email))
        conn.commit()
        conn.close()
        return {"message": "Usuario actualizado"}
    except Exception as e:
        print(e)
        return {"message": "Error al actualizar el usuario"}

#elimina un usuario
@app.delete("usuario/{id}",response_model=Respuesta,status_code=status.HTTP_202_ACCEPTED,
summary="Elimina un usuario",description="Elimina un usuario", tags=["TypeUser"])

#Inserta una denuncia

@app.post(              
    "/denuncia",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Inserta una denuncia",
    description ="Inserta una denuncia",
)
def inserta_denuncia(denuncia: Denuncia_empresa):
    try:
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO denunciaEmpresa (usuario, mensaje, evidencia) VALUES (?,?,?)", (denuncia.usuario, denuncia.mensaje, denuncia.evidencia))
        conn.commit()
        conn.close()
        return {"message": "Denuncia insertada"}
    except Exception as e:
        print(e)
        return {"message": "Error al insertar la denuncia"}

#obtiene todas las denuncias            

@app.get(
    "/denuncia",
    status_code=status.HTTP_200_OK,
    summary     ="Obtiene todas las denuncias",
    description ="Obtiene todas las denuncias",
)
def get_denuncias():
    try:
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM denunciaEmpresa")
        denuncias = cursor.fetchall()
        conn.close()
        return denuncias
    except Exception as e:
        print(e)
        return {"message": "Error al obtener las denuncias"}

#obtiene una denuncia por id

@app.get(
    "/denuncia/{id}",
    status_code=status.HTTP_200_OK,
    summary     ="Obtiene una denuncia por id",
    description ="Obtiene una denuncia por id",
)
def get_denuncia(id: int):
    try:
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM denunciaEmpresa WHERE iddenunciaEmpresa = ?", (id,))
        denuncia = cursor.fetchone()
        conn.close()
        return denuncia
    except Exception as e:
        print(e)
        return {"message": "Error al obtener la denuncia"}

#Inserta la categoria estatus 

@app.post(
    "/categoriaEstatus",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Inserta la categoria estatus",
    description ="Inserta la categoria estatus",
)
def inserta_categoriaEstatus(categoriaEstatus: catStatus):
    try:
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO catStatus (descripcion) VALUES (?)", (categoriaEstatus.descripcion,))
        conn.commit()
        conn.close()
        return {"message": "Categoria insertada"}
    except Exception as e:
        print(e)
        return {"message": "Error al insertar la categoria"}

#obtiene todas las categorias

@app.get(
    "/categoriaEstatus",
    status_code=status.HTTP_200_OK,
    summary     ="Obtiene todas las categorias",
    description ="Obtiene todas las categorias",
)
def get_categorias():
    try:
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM catStatus")
        categorias = cursor.fetchall()
        conn.close()
        return categorias
    except Exception as e:
        print(e)
        return {"message": "Error al obtener las categorias"}

#obtiene una categoria por id

@app.get(
    "/categoriaEstatus/{id}",
    status_code=status.HTTP_200_OK,
    summary     ="Obtiene una categoria por id",
    description ="Obtiene una categoria por id",
)
def get_categoria(id: int):
    try:
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM catStatus WHERE idcatStatus = ?", (id,))
        categoria = cursor.fetchone()
        conn.close()
        return categoria
    except Exception as e:
        print(e)
        return {"message": "Error al obtener la categoria"}

#Ingresa la instancia a donde se podra la denuncia

@app.post(
    "/instancia",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Ingresa la instancia a donde se podra la denuncia",
    description ="Ingresa la instancia a donde se podra la denuncia",
)
def inserta_instancia(instancia: Instancia):
    try:
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO catInstancia (descripcion, extension, correo) VALUES (?,?,?)", (instancia.descripcion, instancia.extension, instancia.correo))
        conn.commit()
        conn.close()
        return {"message": "Instancia insertada"}
    except Exception as e:
        print(e)
        return {"message": "Error al insertar la instancia"}

#obtiene todas las instancias

@app.get(
    "/instancia",
    status_code=status.HTTP_200_OK,
    summary     ="Obtiene todas las instancias",
    description ="Obtiene todas las instancias",
)
def get_instancias():
    try:
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM catInstancia")
        instancias = cursor.fetchall()
        conn.close()
        return instancias
    except Exception as e:
        print(e)
        return {"message": "Error al obtener las instancias"}

#obtiene una instancia por id

@app.get(
    "/instancia/{id}",
    status_code=status.HTTP_200_OK,
    summary     ="Obtiene una instancia por id",
    description ="Obtiene una instancia por id",
)
def get_instancia(id: int):
    try:
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM catInstancia WHERE idcatInstancia = ?", (id,))
        instancia = cursor.fetchone()
        conn.close()
        return instancia
    except Exception as e:
        print(e)
        return {"message": "Error al obtener la instancia"}