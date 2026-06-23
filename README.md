# Web Scraping con Selenium y SQLModel

## Descripción

Este proyecto implementa un proceso de web scraping utilizando Selenium WebDriver para extraer información desde el sitio Books 
to Scrape (https://books.toscrape.com).

La aplicación navega desde la página principal hacia una categoría específica, recorre la paginación disponible y obtiene información 
de al menos 50 libros. Los datos extraídos son almacenados en una base de datos SQLite mediante SQLModel.

---

## Tecnologías Utilizadas

- Python 3
- Selenium WebDriver
- SQLModel
- SQLite
- WebDriver Manager

---

## Estructura del Proyecto

```
scraper_project/
├── models.py
├── database.py
├── scraper.py
├── seed.py
├── queries.py
├── main.py
├── requirements.txt
└── data.db
```
---

## Ejecución

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar el proyecto:

```bash
python main.py
```
---

## Autores

* Gustavo Miles
* Jorge Nuñez