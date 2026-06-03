import modules.utils.coreFiles as cf
import modules.utils.console as u

MEDICAMENTOS = "data/medicamentos.json"
PROVEEDORES = "data/proveedores.json"
PACIENTES = "data/pacientes.json"
EMPLEADOS = "data/empleados.json"
VENTAS = "data/ventas.json"
COMPRAS = "data/compras.json"

def addPurchase():
    try:
        u.borrar_pantalla()
        compras = cf.read_json(COMPRAS)
        medicamentos = cf.read_json(MEDICAMENTOS)
        proveedores = cf.read_json(PROVEEDORES)
        idCompra = input("Ingrese ID de la compra: ")
        idProveedor = input("Ingrese ID del proveedor: ")
        idMedicamento = input("Ingrese ID del medicamento: ")
        if idProveedor not in proveedores["proveedores"]:
            print("Proveedor no existe")
            u.pausar_pantalla()
            return
        if idMedicamento not in medicamentos["medicamentos"]:
            print("Medicamento no existe")
            u.pausar_pantalla()
            return

        cantidad = int(input("Cantidad comprada: "))
        precioCompra = float(input("Precio de compra: "))
        fecha = input("Fecha (AAAA-MM-DD): ")
        compras["compras"][idCompra] = {
            "fecha": fecha,
            "idProveedor": idProveedor,
            "idMedicamento": idMedicamento,
            "cantidad": cantidad,
            "precioCompra": precioCompra
        }

        medicamentos["medicamentos"][idMedicamento]["stock"] += cantidad

        cf.write_json(COMPRAS, compras)
        cf.write_json(MEDICAMENTOS, medicamentos)

        print("Compra registrada correctamente")
        u.pausar_pantalla()
        
    except KeyboardInterrupt:
        print('Interrucion detectada')
        u.pausar_pantalla()
    except ValueError:
        print("❌ Error: Ingresa un valor válido.")
        u.pausar_pantalla()
    except KeyError as e:
        print(f"❌ Error: Falta la clave {e} en los datos del sistema.")
        u.pausar_pantalla()
    
def searchPurchase():
    try:
        u.borrar_pantalla()
        compras = cf.read_json(COMPRAS)
        idCompra = input("Ingrese ID de la compra: ")
        compra = compras["compras"].get(idCompra)
        if compra is None:
            print("Compra no encontrada")
            u.pausar_pantalla()
            return

        print("\n===== COMPRA =====")
        print(f"Fecha: {compra['fecha']}")
        print(f"Proveedor: {compra['idProveedor']}")
        print(f"Medicamento: {compra['idMedicamento']}")
        print(f"Cantidad: {compra['cantidad']}")
        print(f"Precio Compra: {compra['precioCompra']}")
        u.pausar_pantalla()

    except KeyboardInterrupt:
        print('Interrucion detectada')
        u.pausar_pantalla()
    except ValueError:
        print("❌ Error: Ingresa un valor válido.")
        u.pausar_pantalla()
    except KeyError as e:
        print(f"❌ Error: Falta la clave {e} en los datos del sistema.")
        u.pausar_pantalla()
    
def listPurchases():
    try:
        u.borrar_pantalla()
        
        compras = cf.read_json(COMPRAS)
        if not compras["compras"]:
            print("No hay compras registradas")
            return

        print("\n===== LISTADO DE COMPRAS =====\n")

        for idCompra, compra in compras["compras"].items():

            print(f"ID: {idCompra}")
            print(f"Fecha: {compra['fecha']}")
            print(f"Proveedor: {compra['idProveedor']}")
            print(f"Medicamento: {compra['idMedicamento']}")
            print(f"Cantidad: {compra['cantidad']}")
            print(f"Precio Compra: {compra['precioCompra']}")
            print("-" * 40)
            u.pausar_pantalla()
        
    except KeyboardInterrupt:
        print('Interrucion detectada')
        u.pausar_pantalla()
    except ValueError:
        print("❌ Error: Ingresa un valor válido.")
        u.pausar_pantalla()
    except KeyError as e:
        print(f"❌ Error: Falta la clave {e} en los datos del sistema.")
        u.pausar_pantalla()