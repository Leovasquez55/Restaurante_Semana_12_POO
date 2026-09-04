from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio


def mostrar_menu() -> None:
    opciones = (
        "Registrar producto",
        "Buscar producto",
        "Actualizar producto",
        "Eliminar producto",
        "Listar productos",
        "Registrar usuario",
        "Listar usuarios",
        "Mostrar categorias",
        "Vender producto",
        "Consultar ventas de un usuario",
        "Salir"
    )

    print("\n" + "=" * 40)
    print("        SISTEMA DE RESTAURANTE")
    print("=" * 40)

    for numero, opcion in enumerate(opciones, start=1):
        print(f"{numero}. {opcion}")


def registrar_producto(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:
    try:
        codigo = input("Ingrese el codigo: ")
        nombre = input("Ingrese el nombre: ")
        categoria = input("Ingrese la categoria: ")
        precio = float(input("Ingrese el precio: "))
        stock = int(input("Ingrese el stock: "))

        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio,
            stock
        )

        restaurante.registrar_producto(producto)
        archivo_servicio.guardar_productos(restaurante.productos)

        print("Producto registrado correctamente.")

    except ValueError as error:
        print(f"Error: {error}")


def buscar_producto(restaurante: Restaurante) -> None:
    codigo = input("Ingrese el codigo del producto: ")

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("Producto no encontrado.")
    else:
        print(producto)


def actualizar_producto(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:
    try:
        codigo = input("Ingrese el codigo del producto: ")
        nombre = input("Ingrese el nuevo nombre: ")
        categoria = input("Ingrese la nueva categoria: ")
        precio = float(input("Ingrese el nuevo precio: "))
        stock = int(input("Ingrese el nuevo stock: "))

        actualizado = restaurante.actualizar_producto(
            codigo,
            nombre,
            categoria,
            precio,
            stock
        )

        if actualizado:
            archivo_servicio.guardar_productos(restaurante.productos)
            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")

    except ValueError as error:
        print(f"Error: {error}")


def eliminar_producto(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:
    codigo = input("Ingrese el codigo del producto: ")

    eliminado = restaurante.eliminar_producto(codigo)

    if eliminado:
        archivo_servicio.guardar_productos(restaurante.productos)
        print("Producto eliminado correctamente.")
    else:
        print("Producto no encontrado.")


def listar_productos(restaurante: Restaurante) -> None:
    productos = restaurante.listar_productos()

    if not productos:
        print("No hay productos registrados.")
        return

    print("\n--- LISTA DE PRODUCTOS ---")

    for producto in productos:
        print(producto)


def registrar_usuario(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:
    try:
        identificacion = input("Ingrese la identificacion: ")
        nombre = input("Ingrese el nombre: ")
        correo = input("Ingrese el correo: ")

        usuario = Usuario(
            identificacion,
            nombre,
            correo
        )

        restaurante.registrar_usuario(usuario)
        archivo_servicio.guardar_usuarios(restaurante.usuarios)

        print("Usuario registrado correctamente.")

    except ValueError as error:
        print(f"Error: {error}")


def listar_usuarios(restaurante: Restaurante) -> None:
    usuarios = restaurante.listar_usuarios()

    if not usuarios:
        print("No hay usuarios registrados.")
        return

    print("\n--- LISTA DE USUARIOS ---")

    for usuario in usuarios:
        print(usuario)


def mostrar_categorias(restaurante: Restaurante) -> None:
    categorias = restaurante.mostrar_categorias()

    if not categorias:
        print("No hay categorias registradas.")
        return

    print("\n--- CATEGORIAS ---")

    for categoria in sorted(categorias):
        print(f"- {categoria}")


def vender_producto(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:
    try:
        identificacion_usuario = input(
            "Ingrese la identificacion del usuario: "
        )
        codigo_producto = input(
            "Ingrese el codigo del producto: "
        )
        cantidad = int(input("Ingrese la cantidad: "))

        vendido = restaurante.vender_producto(
            codigo_producto,
            identificacion_usuario,
            cantidad
        )

        if vendido:
            archivo_servicio.guardar_productos(
                restaurante.productos
            )
            archivo_servicio.guardar_ventas(
                restaurante.ventas
            )

            print("Venta registrada correctamente.")
        else:
            print(
                "No se pudo realizar la venta. "
                "Verifique el usuario, producto, cantidad y stock."
            )

    except ValueError as error:
        print(f"Error: {error}")


def consultar_ventas_usuario(
    restaurante: Restaurante
) -> None:
    identificacion = input(
        "Ingrese la identificacion del usuario: "
    )

    usuario = restaurante.buscar_usuario(identificacion)

    if usuario is None:
        print("Usuario no encontrado.")
        return

    ventas = restaurante.ventas_por_usuario(
        identificacion
    )

    if not ventas:
        print("El usuario no tiene ventas registradas.")
        return

    print("\n--- VENTAS DEL USUARIO ---")

    for venta in ventas:
        producto = restaurante.buscar_producto(
            venta.producto_codigo
        )

        if producto is not None:
            print(
                f"Producto: {producto.nombre} | "
                f"Codigo: {producto.codigo} | "
                f"Cantidad: {venta.cantidad}"
            )


def main() -> None:
    restaurante = Restaurante()

    archivo_servicio = ArchivoServicio(
        "restaurante_app/datos/productos.json"
    )

    productos_guardados = archivo_servicio.cargar_productos()
    usuarios_guardados = archivo_servicio.cargar_usuarios()
    ventas_guardadas = archivo_servicio.cargar_ventas()

    restaurante.productos.extend(productos_guardados)
    restaurante.usuarios.extend(usuarios_guardados)
    restaurante.ventas.extend(ventas_guardadas)

    # Reconstruir los índices a partir de los datos recuperados
    restaurante.reconstruir_indices()

    while True:
        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opcion: "))

            if opcion == 1:
                registrar_producto(
                    restaurante,
                    archivo_servicio
                )

            elif opcion == 2:
                buscar_producto(restaurante)

            elif opcion == 3:
                actualizar_producto(
                    restaurante,
                    archivo_servicio
                )

            elif opcion == 4:
                eliminar_producto(
                    restaurante,
                    archivo_servicio
                )

            elif opcion == 5:
                listar_productos(restaurante)

            elif opcion == 6:
                registrar_usuario(
                    restaurante,
                    archivo_servicio
                )

            elif opcion == 7:
                listar_usuarios(restaurante)

            elif opcion == 8:
                mostrar_categorias(restaurante)

            elif opcion == 9:
                vender_producto(
                    restaurante,
                    archivo_servicio
                )

            elif opcion == 10:
                consultar_ventas_usuario(restaurante)

            elif opcion == 11:
                print("Programa finalizado.")
                break

            else:
                print("Opcion no valida.")

        except ValueError:
            print("Debe ingresar un numero valido.")


if __name__ == "__main__":
    main()