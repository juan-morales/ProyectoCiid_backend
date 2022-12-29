from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Date
from conf.db import meta, engine
from models.provincia import provincias


personas = Table("personas", meta,
            Column("id", Integer, primary_key=True),
            Column("apellido", String(255)),
            Column("nombre", String(255)),
            Column("dni", String(255)),
            Column("fechaNac", Date),
            Column("direccion", String(255)),
            Column("provincia_id", Integer, ForeignKey('provincias.id'))
            )

meta.create_all(engine)