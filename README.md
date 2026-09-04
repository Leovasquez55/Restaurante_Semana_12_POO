# Restaurante App semana 12

# Realizado por:
Leonardo Vasquez

# Descripción

Sistema de gestión de un restaurante desarrollado en Python utilizando Programación Orientada a Objetos (POO).

El proyecto permite administrar productos y usuarios, registrar ventas y consultar las ventas realizadas por cada usuario. En esta versión correspondiente a la Semana 12, se optimizaron las búsquedas mediante el uso de colecciones auxiliares e índices en memoria, manteniendo las listas como colecciones principales.

# Objetivo

Optimizar las operaciones de búsqueda y consulta del sistema mediante el uso de estructuras de datos adecuadas, reduciendo la necesidad de recorrer todas las colecciones cada vez que se realiza una búsqueda.

# Funcionalidades

El sistema permite:

- Registrar productos.
- Buscar productos por código.
- Actualizar productos.
- Eliminar productos.
- Listar productos.
- Registrar usuarios.
- Listar usuarios.
- Mostrar categorías de productos.
- Registrar ventas.
- Controlar el stock disponible.
- Consultar las ventas realizadas por un usuario.
- Guardar y cargar información mediante archivos JSON.

# Colecciones utilizadas

El sistema mantiene como colecciones principales:

- "list[Producto]" para almacenar productos.
- "list[Usuario]" para almacenar usuarios.
- "list[Venta]" para almacenar ventas.

Además, se incorporaron colecciones auxiliares tipo "dict" para optimizar las búsquedas:

- "indice_productos": permite localizar productos rápidamente mediante su código.
- "indice_usuarios": permite localizar usuarios rápidamente mediante su identificación.
- "indice_ventas_usuario": permite consultar directamente las ventas asociadas a un usuario.

También se utiliza un "set" para obtener las categorías únicas de los productos.

# Optimización de búsquedas

Antes de la optimización, las búsquedas se realizaban recorriendo las listas de productos, usuarios o ventas.

En la Semana 12 se implementaron índices auxiliares utilizando diccionarios.

# Por ejemplo:

self.indice_productos: dict[str, Producto] = {}
self.indice_usuarios: dict[str, Usuario] = {}
self.indice_ventas_usuario: dict[str, list[Venta]] = {}

De esta manera, una búsqueda de producto por código o de usuario por identificación puede realizarse directamente mediante su clave.

# Sincronización de índices

Los índices se mantienen sincronizados con las colecciones principales.

Cuando se registra un producto o usuario, también se actualiza su índice correspondiente.

Cuando se elimina un producto, su entrada también se elimina del índice.

Cuando se registra una venta, esta se agrega tanto a la lista principal de ventas como al índice correspondiente al usuario.

Además, al iniciar el programa se ejecuta:

restaurante.reconstruir_indices()

Este método reconstruye los índices a partir de los datos cargados desde los archivos JSON.

# Persistencia de datos

El sistema utiliza archivos JSON para conservar la información:

datos/
├── productos.json
├── usuarios.json
└── ventas.json

Los datos se cargan al iniciar el programa y se guardan después de realizar operaciones que modifican la información.

Esto permite cerrar y volver a ejecutar el programa sin perder los productos, usuarios y ventas registrados.

Control de stock

Al realizar una venta, el sistema verifica:

- Que el usuario exista.
- Que el producto exista.
- Que la cantidad sea mayor que cero.
- Que exista stock suficiente.

Después de registrar una venta, el stock del producto se reduce automáticamente.

# Ejemplo:

Stock inicial: 10
Cantidad vendida: 5
Stock restante: 5

# Estructura del proyecto

restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md

# Tecnologías utilizadas

- Python 3
- Programación Orientada a Objetos
- Listas ("list")
- Diccionarios ("dict")
- Conjuntos ("set")
- Archivos JSON
- Persistencia de datos
- Git y GitHub

# Pruebas realizadas

Durante las pruebas se verificó:

1. Registro de productos.
2. Registro de usuarios.
3. Búsqueda de productos por código.
4. Búsqueda de usuarios por identificación.
5. Registro de ventas.
6. Consulta de ventas por usuario.
7. Actualización automática del stock.
8. Persistencia de productos, usuarios y ventas en archivos JSON.
9. Reconstrucción de los índices al iniciar el programa.

# Conclusión

La implementación de colecciones auxiliares permitió mejorar las búsquedas frecuentes del sistema, evitando recorrer completamente las listas principales en cada consulta.

Se mantuvieron las listas como colecciones principales para conservar la estructura del proyecto y se utilizaron diccionarios como índices para acceder rápidamente a productos, usuarios y ventas. Además, los índices se reconstruyen al iniciar el programa a partir de los datos almacenados en JSON, garantizando la coherencia entre la información persistida y las estructuras utilizadas durante la ejecución.
