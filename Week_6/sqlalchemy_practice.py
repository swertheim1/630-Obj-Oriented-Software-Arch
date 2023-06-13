from pyexpat.errors import messages
from sqlalchemy import create_engine, text
from sqlalchemy import Column, Integer, Text, MetaData, Table
from sqlalchemy import select

engine = create_engine('sqlite:///test.db')

metadata = MetaData()
message = Table(
    'messages', metadata,
    Column('id', Integer, primary_key=True),
    Column('message', Text),
)

message.create(bind=engine)

insert_message = message.insert().values(message='Hello World!')
engine.execute(insert_message)

stmt = select([messages.c.message])
message = engine.execute(stmt).fetchone()
print(message)
