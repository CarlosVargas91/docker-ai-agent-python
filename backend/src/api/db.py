import os
import sqlmodel
from sqlmodel import Session, SQLModel

DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL == "":
    raise NotImplementedError(f"You need a valid database URL. Current value: {DATABASE_URL}")
else
    print(f"The DATABASE_URL is: {DATABASE_URL}")

engine = sqlmodel.create_engine(DATABASE_URL)

#database models
def init_db():
    print("creating database tables...")
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session