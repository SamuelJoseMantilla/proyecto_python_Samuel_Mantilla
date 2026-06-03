import modules.utils.coreFiles as cf
import modules.utils.console as u

MEDICINAS = "data/medicamentos.json"
PROVEEDORES = "data/proveedores.json"
medicinas = {}

def addMedicines():
    try:
        u.borrar_pantalla()
        medicamentos = cf.read_json(MEDICINAS)
        proveedores = cf.read_json(PROVEEDORES)
        
        idMedicamento = input("Ingrese el código del medicamento: ")
        
        if idMedicamento in medicamentos["medicamentos"]:
            print("Ese medicamento ya existe")
            u.pausar_pantalla()
            return

        idProveedor = input('Ingrese el ID del proovedor : ')
        if idProveedor not in proveedores["proveedores"]:
            print('el proveedor no existe.')
        nombre = input('Ingrese el nombre del medicamento : ')
        precio = float(input('Ingrese el precio: '))
        stock = int(input('Ingrese el stock : '))
        fecha = input('Ingrese la fecha de caducidad (AAAA/MM/DD): ')
        
        medicamentos["medicamentos"][idMedicamento] = {
            "nombre": nombre,
            "precio": precio,
            "stock": stock,
            "fechaCadu": fecha,
            "idProveedor": idProveedor
        }
        
        cf.write_json(MEDICINAS, medicamentos)
        print('Medicamento registrado correctamente')
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


def deleteMedicine():
    try:
        u.borrar_pantalla()    
        data = cf.read_json(MEDICINAS)
        codigo = input('Ingrese el código del medicamento a eliminar: ')
        if codigo not in data["medicamentos"]:
            print('El medicamento no existe.')
            u.pausar_pantalla()
            return

        nombre = data["medicamentos"][codigo]["nombre"]
        confirmacion = input(f'¿Desea eliminar el medicamento {nombre}? (S/N): ').upper()
        if confirmacion == "S":
            del data["medicamentos"][codigo]
            cf.write_json(MEDICINAS, data)
            print('Medicamento eliminado correctamente.')
            u.pausar_pantalla()
            
        else:
            print('Operación cancelada.')
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
        
def listMedicines():
    try:
        u.borrar_pantalla()
        data = cf.read_json(MEDICINAS)
        if not data["medicamentos"]:
            print('No hay medicamentos registrados.')
            u.pausar_pantalla()
            return

        print("\n===== LISTADO DE MEDICAMENTOS =====\n")
        for codigo, medicamento in data["medicamentos"].items():
            print(f"Código: {codigo}")
            print(f"Nombre: {medicamento['nombre']}")
            print(f"Precio: {medicamento['precio']}")
            print(f"Stock: {medicamento['stock']}")
            print(f"Fecha de Caducidad: {medicamento['fechaCadu']}")
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
        
def searchMedicine():
    try:
        u.borrar_pantalla()
        data = cf.read_json(MEDICINAS)
        codigo = input('Ingrese el código del medicamento : ')
        medicamento = data["medicamentos"].get(codigo)
        if medicamento is None:
            print('Medicamento no encontrado.')
            u.pausar_pantalla()
            return

        print("\n===== MEDICAMENTO ENCONTRADO =====\n")
        print(f"Código: {codigo}")
        print(f"Nombre: {medicamento['nombre']}")
        print(f"Precio: {medicamento['precio']}")
        print(f"Stock: {medicamento['stock']}")
        print(f"Fecha de Caducidad: {medicamento['fechaCadu']}")
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
        

def updateMedicine():
    try:
        u.borrar_pantalla
        data = cf.read_json(MEDICINAS)
        codigo = input('Ingrese el código del medicamento a modificar: ')
        medicamento = data["medicamentos"].get(codigo)

        if medicamento is None:
            print('Medicamento no encontrado.')
            u.pausar_pantalla()
            return
        print("\nDatos actuales:")
        print(f"Nombre: {medicamento['nombre']}")
        print(f"Precio: {medicamento['precio']}")
        print(f"Stock: {medicamento['stock']}")
        print(f"Fecha Caducidad: {medicamento['fechaCadu']}")

        if input("¿Modificar nombre? (S/N): ").upper() == "S":
            medicamento["nombre"] = input("Nuevo nombre: ")

        if input("¿Modificar precio? (S/N): ").upper() == "S":
            medicamento["precio"] = float(input("Nuevo precio: "))

        if input("¿Modificar stock? (S/N): ").upper() == "S":
            medicamento["stock"] = int(input("Nuevo stock: "))

        if input("¿Modificar fecha de caducidad? (S/N): ").upper() == "S":
            medicamento["fechaCadu"] = input("Nueva fecha (AAAA/MM/DD): ")

        cf.write_json(MEDICINAS, data)

        print('Medicamento actualizado correctamente.')
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
        