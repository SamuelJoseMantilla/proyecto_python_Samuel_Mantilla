import modules.utils.coreFiles as cf
import modules.utils.console as u
from datetime import datetime

MEDICAMENTOS = "data/medicamentos.json"
PROVEEDORES = "data/proveedores.json"
PACIENTES = "data/pacientes.json"
EMPLEADOS = "data/empleados.json"
VENTAS = "data/ventas.json"
COMPRAS = "data/compras.json"


def stockLessThan50():
    try:
        u.borrar_pantalla()    
        medicamentos = cf.read_json(MEDICAMENTOS)
        print("\nMEDICAMENTOS CON MENOS DE 50 UNIDADES\n")
        for idMed, med in medicamentos["medicamentos"].items():
            if med["stock"] < 50:
                print(
                    f"ID: {idMed} | "
                    f"Nombre: {med['nombre']} | "
                    f"Stock: {med['stock']}")
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


def medicinesExpireBefore():
    try:
        u.borrar_pantalla()
        fechaLimite = input("Ingrese fecha (AAAA/MM/DD): ")
        fechaLimite = datetime.strptime(fechaLimite,"%Y/%m/%d")
        medicamentos = cf.read_json(MEDICAMENTOS)
        
        for med in medicamentos["medicamentos"].values():
            fecha = datetime.strptime(med["fechaCadu"],"%Y/%m/%d")

            if fecha < fechaLimite:
                print(med["nombre"])
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

def medicinesExpire2024():
    try:
        u.borrar_pantalla()
        medicamentos = cf.read_json(MEDICAMENTOS)
        for med in medicamentos["medicamentos"].values():
            fecha = datetime.strptime(med["fechaCadu"],"%Y/%m/%d")
            if fecha.year == 2024:

                print(med["nombre"])
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

def medicinesNotSold():
    try:
        u.borrar_pantalla()
        medicamentos = cf.read_json(MEDICAMENTOS)
        ventas = cf.read_json(VENTAS)
        vendidos = set()
        for venta in ventas["ventas"].values():
            vendidos.add(venta["idMedicamento"])
            
        for idMed, med in medicamentos["medicamentos"].items():
            if idMed not in vendidos:
                print(med["nombre"])
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

def medicinesNeverSold():
    medicinesNotSold()


def mostExpensiveMedicine():
    try:
        u.pausar_pantalla()
        medicamentos = cf.read_json(MEDICAMENTOS)
        mayor = None
        for med in medicamentos["medicamentos"].values():
            if mayor is None:
                mayor = med
            elif med["precio"] > mayor["precio"]:
                mayor = med
        print(mayor)
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

def leastSoldMedicine():
    try:
        u.borrar_pantalla()
        medicamentos = cf.read_json(MEDICAMENTOS)
        ventas = cf.read_json(VENTAS)
        contador = {}
        for idMed in medicamentos["medicamentos"]:
            contador[idMed] = 0

        for venta in ventas["ventas"].values():
            contador[venta["idMedicamento"]] += venta["cantidad"]
        menor = min(contador,key=contador.get)
        print(medicamentos["medicamentos"][menor]["nombre"])
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
        
def totalSalesMedicine():
    try:
        u.borrar_pantalla()
        nombreBuscado = input("Nombre del medicamento: ").lower()
        medicamentos = cf.read_json(MEDICAMENTOS)
        ventas = cf.read_json(VENTAS)
        total = 0
        for venta in ventas["ventas"].values():

            idMed = venta["idMedicamento"]
            nombre = medicamentos["medicamentos"][idMed]["nombre"].lower()
            if nombre == nombreBuscado:
                total += venta["cantidad"]
        print(total)
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

def totalIncome():
    try:
        u.borrar_pantalla()
        ventas = cf.read_json(VENTAS)
        total = 0
        for venta in ventas["ventas"].values():
            total += venta["total"]
        print(total)
        u.pausar_pantalla

    except KeyboardInterrupt:
        print('Interrucion detectada')
        u.pausar_pantalla()
    except ValueError:
        print("❌ Error: Ingresa un valor válido.")
        u.pausar_pantalla()
    except KeyError as e:
        print(f"❌ Error: Falta la clave {e} en los datos del sistema.")
        u.pausar_pantalla()

def salesMarch2023():
    try:
        u.borrar_pantalla()
        ventas = cf.read_json(VENTAS)
        total = 0
        for venta in ventas["ventas"].values():
            fecha = datetime.strptime(venta["fecha"],"%Y/%m/%d")
            if fecha.year == 2023 and fecha.month == 3:
                total += venta["cantidad"]
        print(total)
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

def averageMedicinesPerSale():
    
    try:
        u.borrar_pantalla()
        ventas = cf.read_json(VENTAS)
        cantidadVentas = len(ventas["ventas"])
        if cantidadVentas == 0:
            print(0)
            u.pausar_pantalla()
            return
        totalMedicamentos = 0
        for venta in ventas["ventas"].values():
            totalMedicamentos += venta["cantidad"]
        print(totalMedicamentos /cantidadVentas)
 
    except KeyboardInterrupt:
        print('Interrucion detectada')
        u.pausar_pantalla()
    except ValueError:
        print("❌ Error: Ingresa un valor válido.")
        u.pausar_pantalla()
    except KeyError as e:
        print(f"❌ Error: Falta la clave {e} en los datos del sistema.")
        u.pausar_pantalla()   
    
def patientsBoughtMedicine():
    try:
        u.borrar_pantalla()
        nombreBuscado = input("Ingrese el medicamento: ").lower()
        pacientes = cf.read_json(PACIENTES)
        medicamentos = cf.read_json(MEDICAMENTOS)
        ventas = cf.read_json(VENTAS)
        encontrados = set()
        for venta in ventas["ventas"].values():
            idMed = venta["idMedicamento"]
            if medicamentos["medicamentos"][idMed]["nombre"].lower() == nombreBuscado:
                idPaciente = venta["idPaciente"]
                encontrados.add(pacientes["pacientes"][idPaciente]["nombre"])
                
        for paciente in encontrados:
            print(paciente)
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

def inactiveProviders():
    try:
        u.borrar_pantalla()
        proveedores = cf.read_json(PROVEEDORES)
        compras = cf.read_json(COMPRAS)
        activos = set()
        for compra in compras["compras"].values():
            fecha = datetime.strptime(compra["fecha"],"%Y/%m/%d")
            if fecha.year >= datetime.now().year - 1:
                activos.add(compra["idProveedor"])
                
        for idProv, prov in proveedores["proveedores"].items():
            if idProv not in activos:
                print(prov["nombre"])
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

def profitPerProvider2023():
    try:
        u.borrar_pantalla()
        medicamentos = cf.read_json(MEDICAMENTOS)
        compras = cf.read_json(COMPRAS)
        ventas = cf.read_json(VENTAS)
        ganancias = {}

        for venta in ventas["ventas"].values():

            idMed = venta["idMedicamento"]
            precioVenta = venta["precioVenta"]
            costo = 0
            for compra in compras["compras"].values():
                if compra["idMedicamento"] == idMed:
                    costo = compra["precioCompra"]

            ganancia = (precioVenta - costo) * venta["cantidad"]
            proveedor = medicamentos["medicamentos"][idMed]["idProveedor"]
            ganancias[proveedor] = (ganancias.get(proveedor, 0)+ ganancia)
        print(ganancias)        
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

def salesPerEmployee2023():
    try:
        u.borrar_pantalla()
        empleados = cf.read_json(EMPLEADOS)
        ventas = cf.read_json(VENTAS)
        contador = {}
        for idEmp in empleados["empleados"]:
            contador[idEmp] = 0
        for venta in ventas["ventas"].values():
            fecha = datetime.strptime(venta["fecha"],"%Y/%m/%d")
            if fecha.year == 2023:
                contador[venta["idEmpleado"]] += 1
        print(contador)
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

def employeesMoreThan5Sales():
    try:
        u.borrar_pantalla()
        empleados = cf.read_json(EMPLEADOS)
        ventas = cf.read_json(VENTAS)
        contador = {}
        for venta in ventas["ventas"].values():
            idEmp = venta["idEmpleado"]
            contador[idEmp] = (contador.get(idEmp, 0)+ 1)

        for idEmp, cantidad in contador.items():
            if cantidad > 5:
                print(empleados["empleados"][idEmp]["nombre"])
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


def patientMostSpent2023():
    try:
        u.borrar_pantalla()
        pacientes = cf.read_json(PACIENTES)
        ventas = cf.read_json(VENTAS)
        gastos = {}

        for venta in ventas["ventas"].values():
            fecha = datetime.strptime(
                venta["fecha"],"%Y/%m/%d")

            if fecha.year == 2023:
                idPac = venta["idPaciente"]
                gastos[idPac] = (gastos.get(idPac, 0)+ venta["total"])

        if gastos:
            mayor = max(gastos,key=gastos.get)
            print(pacientes["pacientes"][mayor]["nombre"])
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

def employeesWithoutSales2023():
    try:
        u.borrar_pantalla()
        empleados = cf.read_json(EMPLEADOS)
        ventas = cf.read_json(VENTAS)
        activos = set()

        for venta in ventas["ventas"].values():
            fecha = datetime.strptime(
                venta["fecha"],"%Y/%m/%d")
            if fecha.year == 2023:
                activos.add(venta["idEmpleado"])

        for idEmp, emp in empleados["empleados"].items():

            if idEmp not in activos:
                print(emp["nombre"])
                
    except KeyboardInterrupt:
        print('Interrucion detectada')
        u.pausar_pantalla()
    except ValueError:
        print("❌ Error: Ingresa un valor válido.")
        u.pausar_pantalla()
    except KeyError as e:
        print(f"❌ Error: Falta la clave {e} en los datos del sistema.")
        u.pausar_pantalla()
        
def topProvider2023():
    try:
        u.borrar_pantalla()
        proveedores = cf.read_json(PROVEEDORES)
        compras = cf.read_json(COMPRAS)
        cantidades = {}
        for compra in compras["compras"].values():

            fecha = datetime.strptime(
                compra["fecha"],"%Y/%m/%d")

            if fecha.year == 2023:
                idProv = compra["idProveedor"]
                cantidades[idProv] = (cantidades.get(idProv, 0)+ compra["cantidad"])

        if cantidades:
            mayor = max(cantidades,key=cantidades.get)
            print(proveedores["proveedores"][mayor]["nombre"])
    
    except KeyboardInterrupt:
        print('Interrucion detectada')
        u.pausar_pantalla()
    except ValueError:
        print("❌ Error: Ingresa un valor válido.")
        u.pausar_pantalla()
    except KeyError as e:
        print(f"❌ Error: Falta la clave {e} en los datos del sistema.")
        u.pausar_pantalla()

def patientsBoughtMedicine2023():
    try:
        u.borrar_pantalla()
        nombreBuscado = input("Medicamento: ").lower()
        pacientes = cf.read_json(PACIENTES)
        medicamentos = cf.read_json(MEDICAMENTOS)
        ventas = cf.read_json(VENTAS)
        encontrados = set()

        for venta in ventas["ventas"].values():

            fecha = datetime.strptime(
                venta["fecha"],"%Y/%m/%d")

            if fecha.year != 2023:
                continue
            idMed = venta["idMedicamento"]
            nombre = medicamentos["medicamentos"][idMed]["nombre"].lower()
            if nombre == nombreBuscado:
                idPaciente = venta["idPaciente"]
                encontrados.add(pacientes["pacientes"][idPaciente]["nombre"])
        for paciente in encontrados:
            print(paciente)
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
        
def providersContact():
    try:
        u.borrar_pantalla()
        proveedores = cf.read_json(PROVEEDORES)
        print("\n===== PROVEEDORES =====\n")

        for idProv, prov in proveedores["proveedores"].items():

            print(f"ID: {idProv}")
            print(f"Nombre: {prov['nombre']}")
            print(f"Dirección: {prov['direccion']}")
            print(f"Teléfono: {prov['telefono']}")
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
        

def medicinesByProvider():
    try:
        u.borrar_pantalla()
        idProveedor = input("Ingrese el ID del proveedor: ")
        medicamentos = cf.read_json(MEDICAMENTOS)
        encontrados = False

        print("\n===== MEDICAMENTOS =====\n")

        for idMed, med in medicamentos["medicamentos"].items():

            if med["idProveedor"] == idProveedor:
                encontrados = True
                print(f"{idMed} - {med['nombre']}")
                u.pausar_pantalla()

        if not encontrados:
            print("No hay medicamentos asociados a ese proveedor.")
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

def totalSoldByProvider():
    try:
        u.borrar_pantalla()
        medicamentos = cf.read_json(MEDICAMENTOS)
        proveedores = cf.read_json(PROVEEDORES)
        ventas = cf.read_json(VENTAS)
        totales = {}

        for venta in ventas["ventas"].values():

            idMed = venta["idMedicamento"]
            idProveedor = medicamentos["medicamentos"][idMed]["idProveedor"]
            totales[idProveedor] = (totales.get(idProveedor, 0)+ venta["cantidad"])

        print('\n===== TOTAL VENDIDO POR PROVEEDOR =====\n')

        for idProv, cantidad in totales.items():
            nombre = proveedores["proveedores"][idProv]["nombre"]
            print(f"{nombre}: {cantidad}")
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

def medicineCountByProvider():

    try:
        u.borrar_pantalla()
        medicamentos = cf.read_json(MEDICAMENTOS)
        proveedores = cf.read_json(PROVEEDORES)
        contador = {}

        for med in medicamentos["medicamentos"].values():
            idProveedor = med["idProveedor"]
            contador[idProveedor] = (contador.get(idProveedor, 0)+ 1)

        print("\n===== MEDICAMENTOS POR PROVEEDOR =====\n")

        for idProv, cantidad in contador.items():
            nombre = proveedores["proveedores"][idProv]["nombre"]
            print(f"{nombre}: {cantidad}")
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