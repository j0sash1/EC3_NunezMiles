from typing import Any

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


BASE_URL = "https://books.toscrape.com"


def obtener_valoracion(clase_css: str) -> int:
    """Convierte la clase CSS de estrellas a un entero."""

    mapa = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
    }

    for clave, valor in mapa.items():
        if clave in clase_css:
            return valor

    return 0


def scrape_books(min_items: int = 50) -> list[dict[str, Any]]:
    """
    Navega por BooksToScrape y extrae libros.

    Retorna una lista de diccionarios.
    """

    libros: list[dict[str, Any]] = []

    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        )
    )

    wait = WebDriverWait(driver, 10)

    try:
        # 1. Entrar al home
        driver.get(BASE_URL)

        # 2. Navegar mediante clic a una categoría
        categoria_link = wait.until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, "Sequential Art")
            )
        )

        categoria_nombre = categoria_link.text
        categoria_link.click()

        while len(libros) < min_items:

            elementos = wait.until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, "article.product_pod")
                )
            )

            for elemento in elementos:

                if len(libros) >= min_items:
                    break

                try:
                    enlace = elemento.find_element(
                        By.CSS_SELECTOR,
                        "h3 a"
                    )

                    titulo = enlace.get_attribute("title")

                    precio_texto = elemento.find_element(
                        By.CSS_SELECTOR,
                        ".price_color"
                    ).text

                    precio = float(
                        precio_texto.replace("£", "")
                    )

                    clase_valoracion = elemento.find_element(
                        By.CSS_SELECTOR,
                        "p.star-rating"
                    ).get_attribute("class")

                    valoracion = obtener_valoracion(
                        clase_valoracion
                    )

                    stock_texto = elemento.find_element(
                        By.CSS_SELECTOR,
                        ".instock"
                    ).text

                    disponible = "In stock" in stock_texto

                    url_detalle = enlace.get_attribute("href")

                    libros.append(
                        {
                            "titulo": titulo,
                            "precio": precio,
                            "valoracion": valoracion,
                            "disponible": disponible,
                            "categoria": categoria_nombre,
                            "url_detalle": url_detalle,
                        }
                    )

                except Exception as error:
                    print(
                        f"Error procesando libro: {error}"
                    )
                    continue

            try:
                siguiente = driver.find_element(
                    By.CSS_SELECTOR,
                    "li.next a"
                )

                siguiente.click()

            except NoSuchElementException:
                break

    finally:
        driver.quit()

    return libros