import modules.utils.coreFiles as cf
import modules.utils.console as u

MEDICAMENTOS = "data/medicamentos.json"
PROVEEDORES = "data/proveedores.json"
PACIENTES = "data/pacientes.json"
EMPLEADOS = "data/empleados.json"
VENTAS = "data/ventas.json"
COMPRAS = "data/compras.json"

def addSale():
    try:
        u.borrar_pantalla()
        ventas = cf.read_json(VENTAS)
        pacientes = cf.read_json(PACIENTES)
        empleados = cf.read_json(EMPLEADOS)
        medicamentos = cf.read_json(MEDICAMENTOS)

        idVenta = input("Ingrese ID de la venta: ")
        idPaciente = input("Ingrese ID del paciente: ")
        idEmpleado = input("Ingrese ID del empleado: ")
        idMedicamento = input("Ingrese ID del medicamento: ")

        if idPaciente not in pacientes["pacientes"]:
            print("Paciente no existe")
            u.pausar_pantalla()
            return

        if idEmpleado not in empleados["empleados"]:
            print("Empleado no existe")
            u.pausar_pantalla()
            return

        if idMedicamento not in medicamentos["medicamentos"]:
            print("Medicamento no existe")
            u.pausar_pantalla()
            return

        cantidad = int(input("Cantidad vendida: "))
        stock = medicamentos["medicamentos"][idMedicamento]["stock"]
        if cantidad > stock:
            print("Stock insuficiente")
            u.pausar_pantalla()
            return

        precio = medicamentos["medicamentos"][idMedicamento]["precio"]
        total = precio * cantidad
        fecha = input("Fecha (AAAA/MM/DD): ")
        ventas["ventas"][idVenta] = {
            "fecha": fecha,
            "idPaciente": idPaciente,
            "idEmpleado": idEmpleado,
            "idMedicamento": idMedicamento,
            "cantidad": cantidad,
            "precioVenta": precio,
            "total": total
        }

        medicamentos["medicamentos"][idMedicamento]["stock"] -= cantidad

        cf.write_json(VENTAS, ventas)
        cf.write_json(MEDICAMENTOS, medicamentos)

        print("Venta registrada correctamente")
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

def searchSale():
    try:
        u.borrar_pantalla()
        ventas = cf.read_json(VENTAS)
        idVenta = input("Ingrese ID de la venta: ")
        venta = ventas["ventas"].get(idVenta)

        if venta is None:
            print("Venta no encontrada")
            u.pausar_pantalla()
            return

        print("\n===== VENTA =====")

        print(f"Fecha: {venta['fecha']}")
        print(f"Paciente: {venta['idPaciente']}")
        print(f"Empleado: {venta['idEmpleado']}")
        print(f"Medicamento: {venta['idMedicamento']}")
        print(f"Cantidad: {venta['cantidad']}")
        print(f"Precio Venta: {venta['precioVenta']}")
        print(f"Total: {venta['total']}")
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
    
def listSales():
    try:
        u.borrar_pantalla
        ventas = cf.read_json(VENTAS)

        if not ventas["ventas"]:
            print("No hay ventas registradas")
            u.pausar_pantalla()
            return

        print("\n===== LISTADO DE VENTAS =====\n")

        for idVenta, venta in ventas["ventas"].items():

            print(f"ID: {idVenta}")
            print(f"Fecha: {venta['fecha']}")
            print(f"Paciente: {venta['idPaciente']}")
            print(f"Empleado: {venta['idEmpleado']}")
            print(f"Medicamento: {venta['idMedicamento']}")
            print(f"Cantidad: {venta['cantidad']}")
            print(f"Precio Venta: {venta['precioVenta']}")
            print(f"Total: {venta['total']}")
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