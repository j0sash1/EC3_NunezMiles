from sqlmodel import SQLModel, Field, Relationship


class Categoria(SQLModel, table=True):
    """Representa una categoría de libros."""

    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(unique=True)

    libros: list["Libro"] = Relationship(
        back_populates="categoria"
    )


class Libro(SQLModel, table=True):
    """Representa un libro extraído del sitio."""

    id: int | None = Field(default=None, primary_key=True)

    titulo: str
    precio: float
    valoracion: int
    disponible: bool

    categoria_id: int = Field(
        foreign_key="categoria.id"
    )

    url_detalle: str | None = None

    categoria: Categoria | None = Relationship(
        back_populates="libros"
    )