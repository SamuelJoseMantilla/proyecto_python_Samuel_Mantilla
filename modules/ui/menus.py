import modules.utils.console as u
import modules.medications.medicines as m
import modules.patients.patients as p
import modules.employees.employees as em
import modules.suppliers.suppliers as s
import modules.sales.sales as sa
import modules.purchase.purchase as pu
import modules.reports.reports as re
import modules.information.information as inf

def mainMenu():
    
    while True:
        try:
            u.borrar_pantalla()
        
            print( """
--------MENU----------
1. Medicamentos
2. Interaccion Provedores, Empleados y Pacientes
3. Generacion Informes
4. Modulos Reportes
0. Salir     
            """)
            
            opciones = int(input(':)_ '))
            match (opciones):
                case 1:
                    menuMed()
                case 2:
                    menuInterc()
                case 3:
                    menuInformes()
                case 4:
                    menuReportes()
                case 0:
                    break
                case _:
                    print('Te equivocaste')
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
                
def menuMed():
    
    while True:
        try:
            u.borrar_pantalla()
            print("""
1. Agregar Medicina
2. Eliminar Medicina
3. Listar Medicina
4. Buscar Medicina
5. Modificar medicna
6. Ventas de medicina
7. Compras de medicna
0. Salir
                  
                  """)
            menuMed = int(input('Ingrese la opcion : '))
            match (menuMed):
                case 1:
                    m.addMedicines()
                case 2:
                    m.deleteMedicine()
                case 3:
                    m.listMedicines()
                case 4:
                    m.searchMedicine()
                case 5:
                    m.updateMedicine()
                case 6:
                    menuSales()
                case 7:
                    menuPurchase()    
                case 0:
                    break
                case _:
                    print('Te equivocaste')
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
def menuInterc():
    while True:
        try:
            u.borrar_pantalla()
            print("""
1. Provedores
2. Empleados
3. Pacientes
0. Salir
                """)
            menuInterc = int(input('Ingrese la opcion : '))
            match (menuInterc):
                case 1:
                    menuSuppliers()
                case 2:
                    menuEmployees()
                case 3:
                    menuPatients()
                case 0:
                    break
                case _:
                    print('Te equivocaste')
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
def menuInformes():
    while True:
        try:
            u.borrar_pantalla()
            print("""
1. Informes de Ventas
2. Informes de Caducidad
0. Salir
                """)
            menuInterc = int(input('Ingrese la opcion : '))
            match (menuInterc):
                case 1:
                    inf.salesReport()
                case 2:
                    inf.expirationReport()
                case 0:
                    break
                case _:
                    print('Te equivocaste')
        
        except KeyboardInterrupt:
            print('Interrucion detectada')
            u.pausar_pantalla()
        except ValueError:
            print("❌ Error: Ingresa un valor válido.")
            u.pausar_pantalla()
        except KeyError as e:
            print(f"❌ Error: Falta la clave {e} en los datos del sistema.")
            u.pausar_pantalla()

def menuReportes():
    while True:
        try:
            u.borrar_pantalla()
            print("""
1. Obtener todos los medicamentos con menos de 50 unidades en stock.
2. Listar los proveedores con su información de contacto en medicamentos.
3. Medicamentos comprados al ‘Proveedor A’.
4. Obtener recetas médicas emitidas después del 1 de enero de 2023.
5. Total de ventas del medicamento ‘Paracetamol’.
6. Medicamentos que caducan antes del 1 de enero de 2024.
7. Total de medicamentos vendidos por cada proveedor.
8. Siguiente Menu
0. Salir          
        """)
        
            menuReportes = int(input('Ingrese la opcion : '))
            match (menuReportes):
                case 1:
                    re.stockLessThan50()
                case 2:
                    re.providersContact()
                case 3:
                    re.medicinesByProvider()
                case 4:
                    pass
                case 5:
                    re.totalSalesMedicine()        
                case 6:
                    re.medicinesExpireBefore()
                case 7:
                    re.totalSoldByProvider()
                case 8:
                    while True:
                        u.borrar_pantalla()
                        print("""
1. Cantidad total de dinero recaudado por las ventas de medicamentos.                              
2. Medicamentos que no han sido vendidos.
3. Obtener el medicamento más caro.
4. Número de medicamentos por proveedor.
5. Pacientes que han comprado Paracetamol.
6. Proveedores que no han vendido medicamentos en el último año.
7. Obtener el total de medicamentos vendidos en marzo de 2023.
8. Siguiente Menu
0. Volver al Menu anterior                             
""")
                        sigueMenu = int(input('Ingrese la opcion : '))
                        match (sigueMenu):
                            case 1:
                                re.totalIncome()        
                            case 2:
                                re.medicinesNotSold()
                            case 3:
                                re.mostExpensiveMedicine() 
                            case 4:
                                re.medicineCountByProvider()
                            case 5:
                                re.patientsBoughtMedicine()
                            case 6:
                                re.inactiveProviders()
                            case 7:
                                re.salesMarch2023()
                            case 8:
                                while True:
                                    u.borrar_pantalla()
                                    print("""
1. Obtener el medicamento menos vendido en 2023.                                          
2. Ganancia total por proveedor en 2023 (asumiendo un campo precioCompra en Compras).
3. Promedio de medicamentos comprados por venta.
4. Cantidad de ventas realizadas por cada empleado en 2023.
5. Obtener todos los medicamentos que expiren en 2024.
6. Empleados que hayan hecho más de 5 ventas en total.
7. Medicamentos que no han sido vendidos nunca.
8. Siguiente Menu
0. Volver al Menu Anterior
""")
                                    sigueMenu2 = int(input('Ingrese la opcion : '))
                                    match (sigueMenu2):
                                        case 1:
                                            re.leastSoldMedicine()      
                                        case 2:
                                            re.profitPerProvider2023() 
                                        case 3:
                                            re.averageMedicinesPerSale()
                                        case 4:
                                            re.salesPerEmployee2023()
                                        case 5:
                                            re.medicinesExpire2024()
                                        case 6:
                                            re.employeesMoreThan5Sales()
                                        case 7:
                                            re.medicinesNeverSold()
                                        case 8:
                                            while True:
                                                u.borrar_pantalla()
                                                print("""
1. Paciente que ha gastado más dinero en 2023.  
2. Empleados que no han realizado ninguna venta en 2023.
3. Proveedor que ha suministrado más medicamentos en 2023.
4. Pacientes que compraron el medicamento “Paracetamol” en 2023.
0. Volver al Menu anterior
""")    
                                                sigueMenu2 = int(input('Ingrese la opcion : '))
                                                match (sigueMenu2):
                                                    case 1:
                                                        re.patientMostSpent2023()  
                                                    case 2:
                                                        re.employeesWithoutSales2023()
                                                    case 3:
                                                        re.topProvider2023()
                                                    case 4:
                                                        re.patientsBoughtMedicine2023()
                                                    case 0:
                                                        break        
                                                    case _:
                                                        print('Te equivocaste')
                                        case 0:
                                            break
                                        case _:
                                            print('Te equivocaste')
                            case 0:
                                break
                            case _:
                                print('Te equivocaste')
                case 0:
                    break        
                case _:
                    print('Te equivocaste')                
        except KeyboardInterrupt:
            print('Interrucion detectada')
            u.pausar_pantalla()
        except ValueError:
            print("❌ Error: Ingresa un valor válido.")
            u.pausar_pantalla()
        except KeyError as e:
            print(f"❌ Error: Falta la clave {e} en los datos del sistema.")
            u.pausar_pantalla()
            
def menuSales():
    while True:
        try:
            u.borrar_pantalla()
            print('1. agregar ventas\n2. Buscar Ventas\n3. Listar Ventas\n0. Salir ')
            opciventas =int(input(':) '))
            match (opciventas):
                case 1:
                    sa.addSale()               
                case 2:
                    sa.searchSale()        
                case 3:
                    sa.listSales()     
                case 0:
                    break               
                case _:
                    print('Te equivocaste') 
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

def menuPurchase():
    while True:
        try:
            u.borrar_pantalla()
            print('1. agregar compra\n2. Buscar Compra\n3. Listar Compra\n0. Salir ')
            opciventas =int(input(':) '))
            match (opciventas):
                case 1:
                    pu.addPurchase()               
                case 2:
                    pu.searchPurchase()        
                case 3:
                    pu.listPurchases()     
                case 0:
                    break               
                case _:
                    print('Te equivocaste') 
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
        
def menuSuppliers():
    while True:
        try:
            u.borrar_pantalla()
            print('1. Agregar provedores\n2. Eliminar Proveedores\n3. Listar Proveedores\n4. Buscar Proveedores\n5. Modificar Proveedores\n0. Salir')
            opcionProve = int(input('Ingrese la opcion :'))
            match (opcionProve):
                case 1:
                    s.addSuppliers()
                case 2:
                    s.deleteSuppliers()
                case 3:
                    s.listSuppliers()
                case 4:
                    s.searchSuppliers()
                case 5:
                    s.updateSuppliers()
                case 0:
                    break
                case _:
                    print('Te equivocaste')
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
            
def menuEmployees():
    while True:
        try:
            u.borrar_pantalla()
            print('1. Agregar Empleados\n2. Eliminar Empleados\n3. Listar Empleados\n4. Buscar Empleados\n5. Modificar Empleados\n0. Salir')
            opcionWorke = int(input('Ingrese la opcion :'))
            match (opcionWorke):
                case 1:
                    em.addEMployees()
                case 2:
                    em.deleteEmployees()
                case 3:
                    em.listEmployees()
                case 4:
                    em.searchEmployees()
                case 5:
                    em.updateEmployees()
                case 0:
                    break
                case _:
                    print('Te equivocaste')
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
def menuPatients():
    while True:
        try:
            u.borrar_pantalla()
            print('1. Agregar pacientes\n2. Eliminar Pacientes\n3. Listar Pacientes\n4. Buscar Pacientes\n5. Modificar Empleados\n0. Salir')
            opcionPatie = int(input('Ingrese la opcion :'))
            match (opcionPatie):
                case 1:
                    p.addPatients()
                case 2:
                    p.deletePatients()
                case 3:
                    p.listPatients()
                case 4:
                    p.searchPatients()
                case 5:
                    p.updatePatients()
                case 0:
                    break
                case _:
                    print('Te equivocaste')
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