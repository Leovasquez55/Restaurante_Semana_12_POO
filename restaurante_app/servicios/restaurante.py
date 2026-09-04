from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class Restaurante:

    def __init__(self) -> None:
        # Colecciones principales
        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []
        self.ventas: list[Venta] = []

        # Índices auxiliares para búsquedas rápidas
        self.indice_productos: dict[str, Producto] = {}
        self.indice_usuarios: dict[str, Usuario] = {}
        self.indice_ventas_usuario: dict[str, list[Venta]] = {}

    def reconstruir_indices(self) -> None:
        """Reconstruye los índices a partir de las colecciones principales."""

        self.indice_productos.clear()
        self.indice_usuarios.clear()
        self.indice_ventas_usuario.clear()

        for producto in self.productos:
            self.indice_productos[producto.codigo.strip().lower()] = producto

        for usuario in self.usuarios:
            self.indice_usuarios[usuario.identificacion.strip()] = usuario

        for venta in self.ventas:
            identificacion = venta.usuario_id.strip()

            if identificacion not in self.indice_ventas_usuario:
                self.indice_ventas_usuario[identificacion] = []

            self.indice_ventas_usuario[identificacion].append(venta)

    def registrar_producto(self, producto: Producto) -> None:
        clave = producto.codigo.strip().lower()

        if clave in self.indice_productos:
            raise ValueError("Ya existe un producto con ese codigo.")

        self.productos.append(producto)
        self.indice_productos[clave] = producto

    def buscar_producto(self, codigo: str) -> Producto | None:
        clave = codigo.strip().lower()
        return self.indice_productos.get(clave)

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        stock: int
    ) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = precio
        producto.stock = stock

        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        self.productos.remove(producto)

        clave = producto.codigo.strip().lower()
        self.indice_productos.pop(clave, None)

        return True

    def listar_productos(self) -> list[Producto]:
        return self.productos.copy()

    def registrar_usuario(self, usuario: Usuario) -> None:
        identificacion = usuario.identificacion.strip()

        if identificacion in self.indice_usuarios:
            raise ValueError(
                "Ya existe un usuario con esa identificacion."
            )

        self.usuarios.append(usuario)
        self.indice_usuarios[identificacion] = usuario

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        clave = identificacion.strip()
        return self.indice_usuarios.get(clave)

    def listar_usuarios(self) -> list[Usuario]:
        return self.usuarios.copy()

    def mostrar_categorias(self) -> set[str]:
        return {producto.categoria for producto in self.productos}

    def vender_producto(
        self,
        codigo_producto: str,
        identificacion_usuario: str,
        cantidad: int
    ) -> bool:

        usuario = self.buscar_usuario(identificacion_usuario)
        producto = self.buscar_producto(codigo_producto)

        if usuario is None or producto is None:
            return False

        if cantidad <= 0 or producto.stock < cantidad:
            return False

        venta = Venta(
            usuario.identificacion,
            producto.codigo,
            cantidad
        )

        self.ventas.append(venta)
        producto.vender(cantidad)

        identificacion = usuario.identificacion.strip()

        if identificacion not in self.indice_ventas_usuario:
            self.indice_ventas_usuario[identificacion] = []

        self.indice_ventas_usuario[identificacion].append(venta)

        return True

    def listar_ventas(self) -> list[Venta]:
        return self.ventas.copy()

    def ventas_por_usuario(
        self,
        identificacion_usuario: str
    ) -> list[Venta]:

        identificacion = identificacion_usuario.strip()

        return self.indice_ventas_usuario.get(
            identificacion,
            []
        ).copy()