import contextlib
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DIR, DB_ECHO

SQLALCHEMY_DATABASE_URL = f"sqlite:///{DIR}/backstage.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=DB_ECHO
)

metadata = MetaData(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Dependency
@contextlib.contextmanager
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()