import modules.utils.coreFiles as cf
import modules.utils.console as u

PACIENTES = "data/pacientes.json"
pacientes = {}
def addPatients():
    try:
        u.borrar_pantalla()
        data = cf.read_json(PACIENTES)
        codigo = input("Ingrese el código del paciente : ")
        if codigo in data["pacientes"]:
            print("Ese paciente ya existe")
            u.pausar_pantalla()
            return

        nombre = input("Ingrese el nombre del paciente : ")
        direccion = input("Ingrese la direccion: ")
        telefono = int(input("Ingrese el telefono: "))

        data["pacientes"][codigo] = {
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono,
        }
        cf.write_json(PACIENTES, data)
        print('Pacientes registrado correctamen')
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

def deletePatients():
    try:    
        u.borrar_pantalla()
        data = cf.read_json(PACIENTES)
        codigo = input('Ingrese el código del paciente a eliminar: ')
        if codigo not in data["pacientes"]:
            print('El paciente no existe.')
            u.pausar_pantalla()
            return

        nombre = data["pacientes"][codigo]["nombre"]
        confirmacion = input(f'¿Desea eliminar el paciente {nombre}? (S/N): ').upper()
        if confirmacion == "S":
            del data["pacientes"][codigo]
            cf.write_json(PACIENTES, data)
            print('Paciente eliminado correctamente.')
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

def listPatients():
    try:
        u.borrar_pantalla()
        data = cf.read_json(PACIENTES)
        if not data["pacientes"]:
            print('No hay pacientes registrados.')
            u.pausar_pantalla()
            return

        print("\n===== LISTADO DE PACIENTES =====\n")
        for codigo, paciente in data["pacientes"].items():
            print(f"Código: {codigo}")
            print(f"Nombre: {paciente['nombre']}")
            print(f"direccion: {paciente['direccion']}")
            print(f"telofono: {paciente['telefono']}")
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
        
def searchPatients():
    try:
        u.borrar_pantalla()
        data = cf.read_json(PACIENTES)
        codigo = input('Ingrese el código del paciente : ')
        paciente = data["pacientes"].get(codigo)
        if paciente is None:
            print('Empleado no encontrado.')
            u.pausar_pantalla()
            return

        print("\n===== PACIENTE ENCONTRADO =====\n")
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
        

def updatePatients():
    try:
        u.borrar_pantalla()
        data = cf.read_json(PACIENTES)
        codigo = input('Ingrese el código del empleado a modificar: ')
        paciente = data["pacientes"].get(codigo)

        if paciente is None:
            print('Paciente no encontrado.')
            u.pausar_pantalla()
            return
        print("\nDatos actuales:")
        print(f"Nombre: {paciente['nombre']}")
        print(f"direccion: {paciente['direccion']}")
        print(f"telofono: {paciente['telefono']}")

        if input("¿Modificar nombre? (S/N): ").upper() == "S":
            paciente["nombre"] = input("Nuevo nombre: ")
        if input("¿Modificar direccion? (S/N): ").upper() == "S":
            paciente["direccion"] = input("Nueva direccion: ")
        if input("¿Modificar telefono? (S/N): ").upper() == "S":
            paciente["telefono"] = input("Nueva telefono: ")
        cf.write_json(PACIENTES, data)

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