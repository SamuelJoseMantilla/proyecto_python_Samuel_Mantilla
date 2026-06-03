import modules.utils.coreFiles as cf
import modules.utils.console as u

EMPLEADOS = "data/empleados.json"
empleados = {}
def addEMployees():
    try:
        u.borrar_pantalla()
        data = cf.read_json(EMPLEADOS)
        codigo = input("Ingrese el código del empleado : ")
        if codigo in data["empleados"]:
            print("Ese empleado ya existe")
            u.pausar_pantalla()
            return

        nombre = input("Ingrese el nombre del empleado : ")
        cargo = input("Ingrese el cargo : ")
        fechaContrata = input("Ingrese la fecha de contratacion (AAAA/MM/DD) : ")

        data["empleados"][codigo] = {
            "nombre": nombre,
            "cargo": cargo,
            "fechaContrata": fechaContrata,
        }
        cf.write_json(EMPLEADOS, data)
        print('Empleado registrado correctamen')
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

def deleteEmployees():
    try:    
        u.borrar_pantalla()
        data = cf.read_json(EMPLEADOS)
        codigo = input('Ingrese el código del empleado a eliminar: ')
        if codigo not in data["empleados"]:
            print('El empleado no existe.')
            u.pausar_pantalla()           
            return

        nombre = data["empleados"][codigo]["nombre"]
        confirmacion = input(f'¿Desea eliminar el empleado {nombre}? (S/N): ').upper()
        if confirmacion == "S":
            del data["empleados"][codigo]
            cf.write_json(EMPLEADOS, data)
            print('Empleado eliminado correctamente.')
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
        
def listEmployees():
    try:
        u.borrar_pantalla()
        data = cf.read_json(EMPLEADOS)
        if not data["empleados"]:
            print('No hay empleados registrados.')
            u.pausar_pantalla()
            return
        
        print("\n===== LISTADO DE EMPLEADOS =====\n")
        for codigo, empleado in data["empleados"].items():
            print(f"Código: {codigo}")
            print(f"Nombre: {empleado['nombre']}")
            print(f"cargo: {empleado['cargo']}")
            print(f"Fecha de Contratacion: {empleado['fechaContrata']}")
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
        
def searchEmployees():
    try:
        u.borrar_pantalla()
        data = cf.read_json(EMPLEADOS)
        codigo = input('Ingrese el código del empleado : ')
        empleado = data["empleados"].get(codigo)
        if empleado is None:
            print('Empleado no encontrado.')
            u.pausar_pantalla()
            return

        print("\n===== EMPLEADO ENCONTRADO =====\n")
        print(f"Código: {codigo}")
        print(f"Nombre: {empleado['nombre']}")
        print(f"cargo: {empleado['cargo']}")
        print(f"Fecha de Contratacion: {empleado['fechaContrata']}")
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
        

def updateEmployees():
    try:
        u.borrar_pantalla()
        data = cf.read_json(EMPLEADOS)
        codigo = input('Ingrese el código del empleado a modificar: ')
        empleado = data["empleados"].get(codigo)

        if empleado is None:
            print('Empleados no encontrado.')
            u.pausar_pantalla()
            return
        print("\nDatos actuales:")
        print(f"Nombre: {empleado['nombre']}")
        print(f"cargo: {empleado['cargo']}")
        print(f"Fecha de Contratacion: {empleado['fechaContrata']}")

        if input("¿Modificar nombre? (S/N): ").upper() == "S":
            empleado["nombre"] = input("Nuevo nombre: ")
        if input("¿Modificar cargo? (S/N): ").upper() == "S":
            empleado["cargo"] = input("Nuevo cargo: ")
        if input("¿Modificar fecha de contratacion? (S/N): ").upper() == "S":
            empleado["fechaContrata"] = input("Nueva fecha (AAAA/MM/DD): ")
        cf.write_json(EMPLEADOS, data)

        print('Empleado actualizado correctamente.')
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
        