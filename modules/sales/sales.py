import modules.utils.coreFiles as cf

VENTAS = "data/ventas.json"
ventas = {}

def addventas():
    data = cf.read_json(VENTAS)
    