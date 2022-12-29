PASOS PARA EJECUTAR APIREST - FASTAPI

1) LEER EL ARCHIVO requirements.txt DONDE LISTA TODAS LAS DEPENDENCIAS QUE SE NECESITAN PARA EJECUTAR

2) EJECUTARLO EN UN ENTORNO VIRTUAL SI ES POSIBLE - YO USO virtualenv 
Con comando /Script/activate

3) CAMBIAR EL NOMBRE DEL USUARIO, CONTRASEÑA Y PUERTO DE LA BASE DE DATOS LOCAL - ARCHIVO BD.PY 
EN LA LINEA  engine = create_engine("mysql+pymysql://root:@localhost:3307/persona_provincia") - USO XAMP 

4) UNA VEZ INSTALADO TODAS LAS DEPENDENCIAS Y EJECUTADA LA API. EJECUTAR CON COMANDO uvicorn main:app --reload

SE PROCEDE A INSERTAR UN USUARIO "ADMIN" PARA EL LOGIN
INSERT INTO user(username,password) value('admin','admin')

INSERTAR PROVINCIA
INSERT INTO provincia(name) value('Santiago del estero')

INSERTAR UNA PERSONA
INSERT INTO provincia(apellido, nombre, dni, fechaNac, direccion, provincia_id) value('Diaz','Matias',39853171,'20-04-1996','Irigoyen', "id Provincia")

5) COMPROBAR QUE FUNCIONA ANTES DE EJECUNTAR ARCHIVO DE FRONT END

