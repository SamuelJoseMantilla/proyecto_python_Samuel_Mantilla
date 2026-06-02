import modules.utils.coreFiles as cf
import modules.utils.console as u

PROVEEDORES = "data/proveedores.json"
proveedores = {}
def addSuppliers():
    try:
        u.borrar_pantalla()
        data = cf.read_json(PROVEEDORES)
        codigo = input("Ingrese el código del proveedor : ")
        if codigo in data["proveedores"]:
            print("Ese proveedor ya existe")
            u.pausar_pantalla()
            return

        nombre = input("Ingrese el nombre del proveedor : ")
        direccion = input("Ingrese la direccion: ")
        telefono = int(input("Ingrese el telefono : "))

        data["proveedores"][codigo] = {
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono,
        }
        cf.write_json(PROVEEDORES, data)
        print('Proveedor registrado correctamen')
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

def deleteSuppliers():
    try:    
        u.borrar_pantalla()
        data = cf.read_json(PROVEEDORES)
        codigo = input('Ingrese el código del proveedor a eliminar: ')
        if codigo not in data["proveedores"]:
            print('El proveedor no existe.')
            u.pausar_pantalla()
            return

        nombre = data["proveedores"][codigo]["nombre"]
        confirmacion = input(f'¿Desea eliminar el proveedor {nombre}? (S/N): ').upper()
        if confirmacion == "S":
            del data["proveedores"][codigo]
            cf.write_json(PROVEEDORES, data)
            print('Proveedor eliminado correctamente.')
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

def listSuppliers():
    try:
        u.borrar_pantalla()
        data = cf.read_json(PROVEEDORES)
        if not data["proveedores"]:
            print('No hay proveedores registrados.')
            u.pausar_pantalla()
            return

        print("\n===== LISTADO DE PROVEEDORES =====\n")
        for codigo, proveedor in data["proveedores"].items():
            print(f"Código: {codigo}")
            print(f"Nombre: {proveedor['nombre']}")
            print(f"direccion: {proveedor['direccion']}")
            print(f"telofono: {proveedor['telefono']}")
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
        
def searchSuppliers():
    try:
        u.borrar_pantalla
        data = cf.read_json(PROVEEDORES)
        codigo = input('Ingrese el código del proveedor : ')
        paciente = data["pacientes"].get(codigo)
        if paciente is None:
            print('Empleado no encontrado.')
            u.pausar_pantalla()
            return

        print("\n===== PROVEEDOR ENCONTRADO =====\n")
        print(f"Código: {codigo}")
        print(f"Nombre: {paciente['nombre']}")
        print(f"direccion: {paciente['direccion']}")
        print(f"telofono: {paciente['telefono']}")
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
        

def updateSuppliers():
    try:
        u.borrar_pantalla()
        data = cf.read_json(PROVEEDORES)
        codigo = input('Ingrese el código del proveedor a modificar: ')
        proveedor = data["proveedores"].get(codigo)

        if proveedor is None:
            print('Proveedor no encontrado.')
            u.pausar_pantalla()
            return
        print("\nDatos actuales:")
        print(f"Nombre: {proveedor['nombre']}")
        print(f"direccion: {proveedor['direccion']}")
        print(f"telofono: {proveedor['telefono']}")

        if input("¿Modificar nombre? (S/N): ").upper() == "S":
            proveedor["nombre"] = input("Nuevo nombre: ")
        if input("¿Modificar direccion? (S/N): ").upper() == "S":
            proveedor["direccion"] = input("Nueva direccion: ")
        if input("¿Modificar telefono? (S/N): ").upper() == "S":
            proveedor["telefono"] = input("Nueva telefono: ")
        cf.write_json(proveedor, data)

        print('Paciente actualizado correctamente.')
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