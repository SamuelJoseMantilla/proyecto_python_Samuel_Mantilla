import os
import sys

def borrar_pantalla():
    """
    Limpia la consola en Windows, Linux y macOS.
    """
    os.system("cls" if sys.platform.startswith("win") else "clear")


def pausar_pantalla():
    """
    Espera a que el usuario presione Enter.
    """
    input("\nPresione Enter para continuar...")