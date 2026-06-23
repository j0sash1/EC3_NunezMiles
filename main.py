from database import create_db_and_tables, get_session
from queries import (
    estadisticas,
    items_por_categoria,
    top_10_por_criterio,
    total_items,
)
from seed import seed_database


def main() -> None:
    """
    Ejecuta el flujo completo:
    creación de tablas, carga de datos y consultas.
    """

    create_db_and_tables()

    seed_database()

    with get_session() as session:

        print("\n=== TOTAL DE LIBROS ===")
        print(total_items(session))

        print("\n=== LIBROS POR CATEGORIA ===")
        print(items_por_categoria(session))

        print("\n=== TOP 10 LIBROS MÁS CAROS ===")

        for libro in top_10_por_criterio(session):
            print(
                f"{libro.titulo} - £{libro.precio}"
            )

        print("\n=== ESTADISTICAS ===")
        print(estadisticas(session))


if __name__ == "__main__":
    main()