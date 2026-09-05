
import json
from pathlib import Path

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class ArchivoServicio:

    def __init__(self) -> None:
        # Ruta de la carpeta datos
        self.ruta_datos = Path(__file__).resolve().parent.parent / "datos"

        self.ruta_productos = self.ruta_datos / "productos.json"
        self.ruta_usuarios = self.ruta_datos / "usuarios.json"
        self.ruta_ventas = self.ruta_datos / "ventas.json"

        # Crear la carpeta datos si no existe
        self.ruta_datos.mkdir(exist_ok=True)

    # =========================
    # PRODUCTOS
    # =========================

    def guardar_productos(self, productos: list[Producto]) -> None:
        datos = [producto.to_dict() for producto in productos]

        try:
            with open(self.ruta_productos, "w", encoding="utf-8") as archivo:
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
            with open(self.ruta_productos, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

            productos = []

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
            return []

        except json.JSONDecodeError:
            print("productos.json está vacío o dañado.")
            return []

        except PermissionError:
            print("No hay permisos para leer productos.json.")
            return []

        except KeyError as error:
            print(f"Falta la clave {error} en productos.json.")
            return []

    # =========================
    # USUARIOS
    # =========================

    def guardar_usuarios(self, usuarios: list[Usuario]) -> None:
        datos = [usuario.to_dict() for usuario in usuarios]

        try:
            with open(self.ruta_usuarios, "w", encoding="utf-8") as archivo:
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
            with open(self.ruta_usuarios, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

            usuarios = []

            for dato in datos:
                usuario = Usuario(
                    dato["identificacion"],
                    dato["nombre"],
                    dato["correo"]
                )
                usuarios.append(usuario)

            return usuarios

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print("usuarios.json está vacío o dañado.")
            return []

        except PermissionError:
            print("No hay permisos para leer usuarios.json.")
            return []

        except KeyError as error:
            print(f"Falta la clave {error} en usuarios.json.")
            return []

    # =========================
    # VENTAS
    # =========================

    def guardar_ventas(self, ventas: list[Venta]) -> None:
        datos = [venta.to_dict() for venta in ventas]

        try:
            with open(self.ruta_ventas, "w", encoding="utf-8") as archivo:
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
            with open(self.ruta_ventas, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

            ventas = []

            for dato in datos:
                venta = Venta(
                    dato["usuario_id"],
                    dato["producto_codigo"],
                    int(dato["cantidad"])
                )
                ventas.append(venta)

            return ventas

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print("ventas.json está vacío o dañado.")
            return []

        except PermissionError:
            print("No hay permisos para leer ventas.json.")
            return []

        except KeyError as error:
            print(f"Falta la clave {error} en ventas.json.")
            return []