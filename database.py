from sqlmodel import Session, SQLModel, create_engine

DATABASE_URL = "sqlite:///data.db"

engine = create_engine(DATABASE_URL)


def create_db_and_tables() -> None:
    """Crea las tablas de la base de datos."""
    SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    """Retorna una sesión de base de datos."""
    return Session(engine)