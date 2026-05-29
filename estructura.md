medicamentos = {
    nombre : 
    precio : 
    stock : 
    fechaExpiracion : 
 }

 provedores = {
    nombre :
    direc :
    telefono :
    email :
 }
 
 pacientes = {
    nombre :
    direc :
    telefono :
    email :
 }

 empleados = {
    nombre :
    direc :
    telefono :
    email :
 }

 ventas = {
    fechaVenta :
    paciente {
            nombre :
            direc :
            telefono :
            email :
            }
    
    empleados {
        nombre :
        direc :
        telefono :
        email :
    
    medicamentovendidos {
            nombreMedic :
            cantidadVendi :
            precio :
        }
    }
 }

 compras = {
    fechaCompra :
    proveedor {
        nombre :
        direc :
        telefono :
        email :
    }

    medComprados = {
        nombreMed :
        cantidadCompr :
        precioCompr : 
    }
 }