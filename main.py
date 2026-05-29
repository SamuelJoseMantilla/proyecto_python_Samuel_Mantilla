import os
import json
import modules.ui.menus as menu

def main():
    try:
        menu.mainMenu()
    except ValueError:
        print("❌ Error: Ingresa un valor válido.")
    except FileNotFoundError:
        print("❌ Error: No se encontró la base de datos (CampusLands.json).")
    except json.JSONDecodeError:
        print("❌ Error: El archivo de base de datos está dañado o mal formado.")
    except KeyError as e:
        print(f"❌ Error: Falta la clave {e} en los datos del sistema.")
    except KeyboardInterrupt:
        print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú principal.")
    except EOFError:
        print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú principal.")
    except Exception as e:
        print(f"⚠️ Error inesperado: {e}")

if __name__=="__main__":
    main()