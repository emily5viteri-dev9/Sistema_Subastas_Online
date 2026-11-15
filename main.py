
from usuario import Usuario
from comprador import Comprador
from vendedor import Vendedor
from administrador import Administrador
from producto import Producto
from subasta import Subasta
from plataforma import Plataforma


def main():

    print("================================")
    print("     SISTEMA DE SUBASTAS ONLINE")
    print("================================")

    # Crear usuarios
    usuario1 = Usuario(1, "Carlos", "carlos@gmail.com", "1234")
    comprador1 = Comprador(2, "Ana", "ana@gmail.com", "1234", 500)
    vendedor1 = Vendedor(3, "Pedro", "pedro@gmail.com", "1234")
    administrador1 = Administrador(4, "Laura", "laura@gmail.com", "1234")

    # Crear producto
    producto1 = Producto(
        1,
        "Laptop",
        "Laptop en buen estado",
        300,
        vendedor1
    )

    vendedor1.agregar_producto(producto1)

    # Crear subasta
    subasta1 = Subasta(
        1,
        producto1,
        "15/11/2026",
        "20/11/2026"
    )

    # Crear plataforma
    plataforma1 = Plataforma("Subastas Online")

    # Registrar información
    plataforma1.registrar_usuario(usuario1)
    plataforma1.registrar_usuario(comprador1)
    plataforma1.registrar_usuario(vendedor1)
    plataforma1.registrar_usuario(administrador1)

    plataforma1.publicar_producto(producto1)
    plataforma1.crear_subasta(subasta1)

    # Mostrar información
    plataforma1.mostrar_informacion()
    plataforma1.listar_usuarios()
    plataforma1.listar_productos()
    plataforma1.listar_subastas()

    # Realizar pujas
    print("\n--- PROCESO DE PUJAS ---")

    comprador1.realizar_puja(subasta1, 350)
    comprador1.realizar_puja(subasta1, 400)

    # Cerrar subasta
    print("\n--- RESULTADO DE LA SUBASTA ---")
    subasta1.cerrar_subasta()

    # Mostrar información del administrador
    print("\n--- ADMINISTRADOR ---")
    administrador1.mostrar_permisos()


if __name__ == "__main__":
    main()
