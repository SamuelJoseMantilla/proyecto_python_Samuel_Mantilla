def mainMenu():
    
    while True:
        try:
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
            
        except KeyboardInterrupt:
            print('Interrucion detectada')
            
        except ValueError:
            print("❌ Error: Ingresa un valor válido.")
            
        except KeyError as e:
            print(f"❌ Error: Falta la clave {e} en los datos del sistema.")
            
    
def menuMed():
    
    while True:
        try:
            print("""
1. Agregar Medicina
2. Eliminar Medicina
3. Ventas de medicina
4. Compras de medicna
0. Salir
                  
                  """)
            menuMed = int(input('Ingrese la opcion : '))
            match (menuMed):
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 0:
                    break
                case _:
                    print('Te equivocaste')
        
        except KeyboardInterrupt:
            print('Interrucion detectada')
            
        except ValueError:
            print("❌ Error: Ingresa un valor válido.")
            
        except KeyError as e:
            print(f"❌ Error: Falta la clave {e} en los datos del sistema.")

def menuInterc():
    while True:
        try:
            print("""
1. Registro Provedores
2. Registro Empleados
3. Registro Pacientes
0. Salir
                """)
            menuInterc = int(input('Ingrese la opcion : '))
            match (menuInterc):
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 0:
                    break
                case _:
                    print('Te equivocaste')
        
        except KeyboardInterrupt:
            print('Interrucion detectada')
            
        except ValueError:
            print("❌ Error: Ingresa un valor válido.")
            
        except KeyError as e:
            print(f"❌ Error: Falta la clave {e} en los datos del sistema.")

def menuInformes():
    while True:
        try:
            print("""
1. Informes de Ventas
2. Informes de Caducidad
0. Salir
                """)
            menuInterc = int(input('Ingrese la opcion : '))
            match (menuInterc):
                case 1:
                    pass
                case 2:
                    pass
                case 0:
                    break
                case _:
                    print('Te equivocaste')
        
        except KeyboardInterrupt:
            print('Interrucion detectada')
            
        except ValueError:
            print("❌ Error: Ingresa un valor válido.")
            
        except KeyError as e:
            print(f"❌ Error: Falta la clave {e} en los datos del sistema.")


def menuReportes():
    while True:
        try:
            print("""
1. Obtener todos los medicamentos con menos de 50 unidades en stock.
2. Listar los proveedores con su información de contacto en medicamentos.
3. Medicamentos comprados al ‘Proveedor A’.
4. Obtener recetas médicas emitidas después del 1 de enero de 2023.
5. Total de ventas del medicamento ‘Paracetamol’.
6. Medicamentos que caducan antes del 1 de enero de 2024.
7. Total de medicamentos vendidos por cada proveedor.
8. Siguiente pagina
0. Salir          
        """)
        
            menuReportes = int(input('Ingrese la opcion : '))
            match (menuReportes):
                case 1:
                    pass        
                case 2:
                    pass        
                case 3:
                    pass        
                case 4:
                    pass        
                case 5:
                    pass        
                case 6:
                    pass        
                case 7:
                    pass                
                case 8:
                    while True:
                        print("""
1. Cantidad total de dinero recaudado por las ventas de medicamentos.                              
2. Medicamentos que no han sido vendidos.
3. Obtener el medicamento más caro.
4. Número de medicamentos por proveedor.
5. Pacientes que han comprado Paracetamol.
6. Proveedores que no han vendido medicamentos en el último año.
7. Obtener el total de medicamentos vendidos en marzo de 2023.
8. Siguiente Menu
0. Volver al menu anterior                             
""")
                        sigueMenu = int(input('Ingrese la opcion : '))
                        match (sigueMenu):
                            case 1:
                                pass        
                            case 2:
                                pass        
                            case 3:
                                pass        
                            case 4:
                                pass        
                            case 5:
                                pass        
                            case 6:
                                pass        
                            case 7:
                                pass               
                            case 8:
                                while True:
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
                                            pass        
                                        case 2:
                                            pass        
                                        case 3:
                                            pass        
                                        case 4:
                                            pass        
                                        case 5:
                                            pass        
                                        case 6:
                                            pass        
                                        case 7:
                                            pass             
                                        case 8:
                                            while True:
                                                print("""
1. Paciente que ha gastado más dinero en 2023.  
2. Empleados que no han realizado ninguna venta en 2023.
3. Proveedor que ha suministrado más medicamentos en 2023.
4. Pacientes que compraron el medicamento “Paracetamol” en 2023.
0. Volver al menu anterior
""")    
                                                sigueMenu2 = int(input('Ingrese la opcion : '))
                                                match (sigueMenu2):
                                                    case 1:
                                                        pass        
                                                    case 2:
                                                        pass        
                                                    case 3:
                                                        pass        
                                                    case 4:
                                                        pass        
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
            
        except ValueError:
            print("❌ Error: Ingresa un valor válido.")
            
        except KeyError as e:
            print(f"❌ Error: Falta la clave {e} en los datos del sistema.")