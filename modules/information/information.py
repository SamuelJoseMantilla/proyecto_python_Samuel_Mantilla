import modules.utils.coreFiles as cf
import modules.utils.console as u
from datetime import datetime

MEDICAMENTOS = "data/medicamentos.json"
PACIENTES = "data/pacientes.json"
EMPLEADOS = "data/empleados.json"
VENTAS = "data/ventas.json"

def salesReport():
    try:
        u.borrar_pantalla()
        ventas = cf.read_json(VENTAS)
        pacientes = cf.read_json(PACIENTES)
        empleados = cf.read_json(EMPLEADOS)
        medicamentos = cf.read_json(MEDICAMENTOS)

        fechaInicio = datetime.strptime(input("Fecha inicio (AAAA/MM/DD): "),"%Y/%m/%d")
        fechaFin = datetime.strptime(input("Fecha final (AAAA/MM/DD): "),"%Y/%m/%d")
        ingresos = 0

        print("\n===== INFORME DE VENTAS =====\n")

        for idVenta, venta in ventas["ventas"].items():
            fechaVenta = datetime.strptime(venta["fecha"],"%Y/%m/%d")

            if fechaInicio <= fechaVenta <= fechaFin:
                
                paciente = pacientes["pacientes"][venta["idPaciente"]]["nombre"]
                empleado = empleados["empleados"][venta["idEmpleado"]]["nombre"]
                medicamento = medicamentos["medicamentos"][venta["idMedicamento"]]["nombre"]

                print(f"Venta: {idVenta}")
                print(f"Fecha: {venta['fecha']}")
                print(f"Paciente: {paciente}")
                print(f"Empleado: {empleado}")
                print(f"Medicamento: {medicamento}")
                print(f"Cantidad: {venta['cantidad']}")
                print(f"Total: ${venta['total']}")
                print("-" * 30)

                ingresos += venta["total"]

        print(f"\nIngresos Totales: ${ingresos}")
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


def expirationReport():
    try:
        u.borrar_pantalla()
        medicamentos = cf.read_json(MEDICAMENTOS)
        lista = []

        for idMed, med in medicamentos["medicamentos"].items():

            fecha = datetime.strptime(
                med["fechaCadu"],"%Y/%m/%d")

            lista.append(
                (
                    fecha,
                    idMed,
                    med ))

        lista.sort()

        print("\n===== INFORME DE CADUCIDAD =====\n")

        for fecha, idMed, med in lista:

            print(f"ID: {idMed}")
            print(f"Medicamento: {med['nombre']}")
            print(f"Stock: {med['stock']}")
            print(f"Caduca: {med['fechaCadu']}")
            print("-" * 30)
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