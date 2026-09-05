from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante


def mostrar_menu() -> None:
    print("\n" + "=" * 45)
    print("          RESTAURANTE APP")
    print("=" * 45)
    print("1. Registrar producto")
    print("2. Buscar producto por código")
    print("3. Listar productos")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Registrar usuario")
    print("7. Buscar usuario por identificación")
    print("8. Listar usuarios")
    print("9. Actualizar usuario")
    print("10. Eliminar usuario")
    print("11. Registrar venta")
    print("12. Consultar ventas por usuario")
    print("13. Listar ventas")
    print("14. Mostrar categorías")
    print("0. Salir")
    print("=" * 45)


def main() -> None:

    archivo = ArchivoServicio()
    restaurante = Restaurante()

    # =========================
    # CARGAR DATOS
    # =========================

    restaurante.productos = archivo.cargar_productos()
    restaurante.usuarios = archivo.cargar_usuarios()
    restaurante.ventas = archivo.cargar_ventas()

    # Reconstruir índices después de recuperar los datos
    restaurante.reconstruir_indices()

    print("\nDatos cargados correctamente.")
    print(f"Productos: {len(restaurante.productos)}")
    print(f"Usuarios: {len(restaurante.usuarios)}")
    print(f"Ventas: {len(restaurante.ventas)}")

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción: ").strip()

        # =========================
        # PRODUCTOS
        # =========================

        if opcion == "1":

            try:
                codigo = input("Código: ").strip()
                nombre = input("Nombre: ").strip()
                categoria = input("Categoría: ").strip()
                precio = float(input("Precio: "))
                stock = int(input("Stock: "))

                producto = Producto(
                    codigo,
                    nombre,
                    categoria,
                    precio,
                    stock
                )

                restaurante.registrar_producto(producto)

                archivo.guardar_productos(
                    restaurante.productos
                )

                print("Producto registrado correctamente.")

            except ValueError as error:
                print(f"Error: {error}")

        elif opcion == "2":

            codigo = input(
                "Ingrese el código del producto: "
            ).strip()

            producto = restaurante.buscar_producto(codigo)

            if producto is None:
                print("Producto no encontrado.")
            else:
                print("\nProducto encontrado:")
                print(producto)

        elif opcion == "3":

            productos = restaurante.listar_productos()

            if not productos:
                print("No hay productos registrados.")
            else:
                print("\n--- PRODUCTOS ---")

                for producto in productos:
                    print(producto)

        elif opcion == "4":

            codigo = input(
                "Código del producto que desea actualizar: "
            ).strip()

            producto = restaurante.buscar_producto(codigo)

            if producto is None:
                print("Producto no encontrado.")
            else:
                try:
                    nombre = input("Nuevo nombre: ").strip()
                    categoria = input("Nueva categoría: ").strip()
                    precio = float(input("Nuevo precio: "))
                    stock = int(input("Nuevo stock: "))

                    actualizado = restaurante.actualizar_producto(
                        codigo,
                        nombre,
                        categoria,
                        precio,
                        stock
                    )

                    if actualizado:
                        archivo.guardar_productos(
                            restaurante.productos
                        )

                        print(
                            "Producto actualizado correctamente."
                        )

                except ValueError as error:
                    print(f"Error: {error}")

        elif opcion == "5":

            codigo = input(
                "Código del producto que desea eliminar: "
            ).strip()

            eliminado = restaurante.eliminar_producto(codigo)

            if eliminado:
                archivo.guardar_productos(
                    restaurante.productos
                )

                print(
                    "Producto eliminado correctamente."
                )
            else:
                print("Producto no encontrado.")

        # =========================
        # USUARIOS
        # =========================

        elif opcion == "6":

            try:
                identificacion = input(
                    "Identificación: "
                ).strip()

                nombre = input("Nombre: ").strip()
                correo = input("Correo: ").strip()

                usuario = Usuario(
                    identificacion,
                    nombre,
                    correo
                )

                restaurante.registrar_usuario(usuario)

                archivo.guardar_usuarios(
                    restaurante.usuarios
                )

                print(
                    "Usuario registrado correctamente."
                )

            except ValueError as error:
                print(f"Error: {error}")

        elif opcion == "7":

            identificacion = input(
                "Ingrese la identificación del usuario: "
            ).strip()

            usuario = restaurante.buscar_usuario(
                identificacion
            )

            if usuario is None:
                print("Usuario no encontrado.")
            else:
                print("\nUsuario encontrado:")
                print(usuario)

        elif opcion == "8":

            usuarios = restaurante.listar_usuarios()

            if not usuarios:
                print("No hay usuarios registrados.")
            else:
                print("\n--- USUARIOS ---")

                for usuario in usuarios:
                    print(usuario)

        elif opcion == "9":

            identificacion = input(
                "Identificación del usuario que desea actualizar: "
            ).strip()

            usuario = restaurante.buscar_usuario(
                identificacion
            )

            if usuario is None:
                print("Usuario no encontrado.")
            else:
                try:
                    nombre = input("Nuevo nombre: ").strip()
                    correo = input("Nuevo correo: ").strip()

                    actualizado = restaurante.actualizar_usuario(
                        identificacion,
                        nombre,
                        correo
                    )

                    if actualizado:
                        archivo.guardar_usuarios(
                            restaurante.usuarios
                        )

                        print(
                            "Usuario actualizado correctamente."
                        )

                except ValueError as error:
                    print(f"Error: {error}")

        elif opcion == "10":

            identificacion = input(
                "Identificación del usuario que desea eliminar: "
            ).strip()

            eliminado = restaurante.eliminar_usuario(
                identificacion
            )

            if eliminado:
                archivo.guardar_usuarios(
                    restaurante.usuarios
                )

                print(
                    "Usuario eliminado correctamente."
                )
            else:
                print("Usuario no encontrado.")

        # =========================
        # VENTAS
        # =========================

        elif opcion == "11":

            try:
                codigo = input(
                    "Código del producto: "
                ).strip()

                identificacion = input(
                    "Identificación del usuario: "
                ).strip()

                cantidad = int(
                    input("Cantidad: ")
                )

                venta_realizada = restaurante.vender_producto(
                    codigo,
                    identificacion,
                    cantidad
                )

                if venta_realizada:

                    archivo.guardar_productos(
                        restaurante.productos
                    )

                    archivo.guardar_ventas(
                        restaurante.ventas
                    )

                    print(
                        "Venta registrada correctamente."
                    )

                    print(
                        "El stock fue actualizado."
                    )

                else:
                    print(
                        "No se pudo realizar la venta. "
                        "Verifique usuario, producto y stock."
                    )

            except ValueError as error:
                print(f"Error: {error}")

        elif opcion == "12":

            identificacion = input(
                "Identificación del usuario: "
            ).strip()

            usuario = restaurante.buscar_usuario(
                identificacion
            )

            if usuario is None:
                print("Usuario no encontrado.")
            else:

                ventas = restaurante.ventas_por_usuario(
                    identificacion
                )

                if not ventas:
                    print(
                        "El usuario no tiene ventas registradas."
                    )
                else:
                    print(
                        "\n--- VENTAS DEL USUARIO ---"
                    )

                    for venta in ventas:
                        print(venta)

        elif opcion == "13":

            ventas = restaurante.listar_ventas()

            if not ventas:
                print("No hay ventas registradas.")
            else:
                print("\n--- TODAS LAS VENTAS ---")

                for venta in ventas:
                    print(venta)

        # =========================
        # CATEGORÍAS
        # =========================

        elif opcion == "14":

            categorias = restaurante.mostrar_categorias()

            if not categorias:
                print("No hay categorías registradas.")
            else:
                print("\n--- CATEGORÍAS ---")

                for categoria in sorted(categorias):
                    print(f"- {categoria}")

        # =========================
        # SALIR
        # =========================

        elif opcion == "0":

            archivo.guardar_productos(
                restaurante.productos
            )

            archivo.guardar_usuarios(
                restaurante.usuarios
            )

            archivo.guardar_ventas(
                restaurante.ventas
            )

            print("\nDatos guardados correctamente.")
            print("Programa finalizado.")

            break

        else:
            print(
                "Opción no válida. Intente nuevamente."
            )


if __name__ == "__main__":
    main()