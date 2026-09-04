
import json

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class ArchivoServicio:

    def __init__(self, ruta_productos: str) -> None:
        self.ruta_productos = ruta_productos
        self.ruta_usuarios = "restaurante_app/datos/usuarios.json"
        self.ruta_ventas = "restaurante_app/datos/ventas.json"

    def guardar_productos(self, productos: list[Producto]) -> None:
        datos = []

        for producto in productos:
            datos.append(producto.to_dict())

        try:
            with open(
                self.ruta_productos,
                "w",
                encoding="utf-8"
            ) as archivo:
                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )

        except PermissionError:
            print("No hay permisos para escribir productos.json.")

    def cargar_productos(self) -> list[Producto]:
        try:
            with open(
                self.ruta_productos,
                "r",
                encoding="utf-8"
            ) as archivo:
                datos = json.load(archivo)

            productos: list[Producto] = []

            for dato in datos:
                producto = Producto(
                    dato["codigo"],
                    dato["nombre"],
                    dato["categoria"],
                    float(dato["precio"]),
                    int(dato["stock"])
                )
                productos.append(producto)

            return productos

        except FileNotFoundError:
            print(
                "Archivo de productos no encontrado, "
                "se iniciará sin productos."
            )
            return []

        except json.JSONDecodeError:
            print(
                "El archivo de productos está vacío o dañado, "
                "se iniciará vacío."
            )
            return []

        except PermissionError:
            print("No hay permisos para leer productos.json.")
            return []

        except KeyError as error:
            print(f"Falta la clave {error} en productos.json.")
            return []

    def guardar_usuarios(self, usuarios: list[Usuario]) -> None:
        datos = []

        for usuario in usuarios:
            datos.append(usuario.to_dict())

        try:
            with open(
                self.ruta_usuarios,
                "w",
                encoding="utf-8"
            ) as archivo:
                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )

        except PermissionError:
            print("No hay permisos para escribir usuarios.json.")

    def cargar_usuarios(self) -> list[Usuario]:
        try:
            with open(
                self.ruta_usuarios,
                "r",
                encoding="utf-8"
            ) as archivo:
                datos = json.load(archivo)

            usuarios: list[Usuario] = []

            for dato in datos:
                usuario = Usuario(
                    dato["identificacion"],
                    dato["nombre"],
                    dato["correo"]
                )
                usuarios.append(usuario)

            return usuarios

        except FileNotFoundError:
            print(
                "Archivo de usuarios no encontrado, "
                "se iniciará sin usuarios."
            )
            return []

        except json.JSONDecodeError:
            print(
                "El archivo de usuarios está vacío o dañado, "
                "se iniciará vacío."
            )
            return []

        except PermissionError:
            print("No hay permisos para leer usuarios.json.")
            return []

        except KeyError as error:
            print(f"Falta la clave {error} en usuarios.json.")
            return []

    def guardar_ventas(self, ventas: list[Venta]) -> None:
        datos = []

        for venta in ventas:
            datos.append(venta.to_dict())

        try:
            with open(
                self.ruta_ventas,
                "w",
                encoding="utf-8"
            ) as archivo:
                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )

        except PermissionError:
            print("No hay permisos para escribir ventas.json.")

    def cargar_ventas(self) -> list[Venta]:
        try:
            with open(
                self.ruta_ventas,
                "r",
                encoding="utf-8"
            ) as archivo:
                datos = json.load(archivo)

            ventas: list[Venta] = []

            for dato in datos:
                venta = Venta(
                    dato["usuario_id"],
                    dato["producto_codigo"],
                    int(dato["cantidad"])
                )
                ventas.append(venta)

            return ventas

        except FileNotFoundError:
            print(
                "Archivo de ventas no encontrado, "
                "se iniciará sin ventas."
            )
            return []

        except json.JSONDecodeError:
            print(
                "El archivo de ventas está vacío o dañado, "
                "se iniciará vacío."
            )
            return []

        except PermissionError:
            print("No hay permisos para leer ventas.json.")
            return []

        except KeyError as error:
            print(f"Falta la clave {error} en ventas.json.")
            return []