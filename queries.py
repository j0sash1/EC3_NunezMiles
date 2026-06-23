from sqlmodel import Session, func, select

from models import Categoria, Libro


def total_items(session: Session) -> int:
    """
    Retorna la cantidad total de libros almacenados.
    """

    resultado = session.exec(
        select(func.count()).select_from(Libro)
    ).one()

    return int(resultado)


def items_por_categoria(
    session: Session,
) -> list[tuple[str, int]]:
    """
    Retorna cada categoría junto con la cantidad
    de libros que contiene, ordenado de mayor a menor.
    """

    resultados = session.exec(
        select(
            Categoria.nombre,
            func.count(Libro.id)
        )
        .join(Libro)
        .group_by(Categoria.nombre)
        .order_by(func.count(Libro.id).desc())
    ).all()

    return list(resultados)


def top_10_por_criterio(
    session: Session,
) -> list[Libro]:
    """
    Retorna los 10 libros más caros.

    Se utiliza el precio como criterio numérico,
    ya que es una métrica fácil de comparar.
    """

    resultados = session.exec(
        select(Libro)
        .order_by(Libro.precio.desc())
        .limit(10)
    ).all()

    return list(resultados)


def estadisticas(session: Session) -> dict:
    """
    Retorna estadísticas descriptivas sobre los precios:
    promedio, mínimo y máximo.
    """

    promedio = session.exec(
        select(func.avg(Libro.precio))
    ).one()

    minimo = session.exec(
        select(func.min(Libro.precio))
    ).one()

    maximo = session.exec(
        select(func.max(Libro.precio))
    ).one()

    return {
        "precio_promedio": round(float(promedio), 2),
        "precio_minimo": float(minimo),
        "precio_maximo": float(maximo),
    }