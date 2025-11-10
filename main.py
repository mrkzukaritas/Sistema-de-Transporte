from envios.envio_manager import EnvioManager

def menu():
    manager = EnvioManager()

    while True:
        print("\n=== SISTEMA DE GESTIÓN DE ENVIOS ===")
        print("1. Crear envío")
        print("2. Listar envíos")
        print("3. Actualizar envío")
        print("4. Eliminar envío")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo = input("Tipo (terrestre/maritima/aerea): ").lower()
            destino = input("Destino: ")
            manager.crear_envio(tipo, destino)
        elif opcion == "2":
            manager.listar_envios()
        elif opcion == "3":
            id_envio = int(input("ID del envío a actualizar: "))
            nuevo_estado = input("Nuevo estado (Pendiente/En tránsito/Entregado): ")
            manager.actualizar_envio(id_envio, nuevo_estado)
        elif opcion == "4":
            id_envio = int(input("ID del envío a eliminar: "))
            manager.eliminar_envio(id_envio)
        elif opcion == "5":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
