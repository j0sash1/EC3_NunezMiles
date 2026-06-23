from sqlmodel import select

from database import get_session
from models import Categoria, Libro
from scraper import scrape_books


def seed_database() -> None:
    """Carga los libros scrapeados en la base de datos."""

    libros_scrapeados = scrape_books()

    with get_session() as session:

        for item in libros_scrapeados:

            categoria = session.exec(
                select(Categoria).where(
                    Categoria.nombre == item["categoria"]
                )
            ).first()

            if categoria is None:
                categoria = Categoria(
                    nombre=item["categoria"]
                )

                session.add(categoria)
                session.commit()
                session.refresh(categoria)

            libro_existente = session.exec(
                select(Libro).where(
                    Libro.titulo == item["titulo"]
                )
            ).first()

            if libro_existente:
                continue

            libro = Libro(
                titulo=item["titulo"],
                precio=item["precio"],
                valoracion=item["valoracion"],
                disponible=item["disponible"],
                categoria_id=categoria.id,
                url_detalle=item["url_detalle"],
            )

            session.add(libro)

        session.commit()
        