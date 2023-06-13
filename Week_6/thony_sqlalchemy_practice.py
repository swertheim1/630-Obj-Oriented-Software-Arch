from sqlalchemy import create_engine, text
from sqlalchemy import Column, Integer, Text, MetaData, Table

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