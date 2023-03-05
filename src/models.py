from sqlalchemy import MetaData, Table, Column, String, Integer, ForeignKey

metadate = MetaData()

webinar = Table(
    "webinar",
    metadate,
    Column("id", Integer, primary_key=True),
    Column("course", Integer, ForeignKey("course.id")),
    Column("teacher", Integer, ForeignKey("teacher.id")),
    Column("status", String, nullable=False)
)

course = Table(
    "course",
    metadate,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False)
)

teacher = Table(
    "teacher",
    metadate,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("name", String, nullable=False),
    Column("webinar_id", Integer, ForeignKey("webinar.id"))
)
