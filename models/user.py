from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Date
from conf.db import meta, engine
from models.provincia import provincias


users = Table("users", meta,
            Column("id", Integer, primary_key=True),
            Column("username", String(255)),
            Column("password", String(255)),
            )

meta.create_all(engine)