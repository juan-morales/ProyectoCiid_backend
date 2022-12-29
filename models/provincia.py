from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from conf.db import meta, engine
from sqlalchemy.orm import relationship

provincias = Table("provincias", meta,
            Column("id", Integer, primary_key=True),
            Column("name", String(255)),
            )

meta.create_all(engine)