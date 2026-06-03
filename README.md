# Sistema de Gestión de Farmacia

## Autor

**Samuel Mantilla Pallares**

---

## Descripción

Este proyecto consiste en el desarrollo de un sistema de gestión para una farmacia utilizando el lenguaje de programación Python y almacenamiento de información mediante archivos JSON.

El sistema permite administrar medicamentos, proveedores, pacientes, empleados, compras y ventas, además de generar reportes e informes que facilitan el control de la información y la toma de decisiones dentro de la farmacia.

---

## Objetivos

* Gestionar la información de medicamentos.
* Gestionar pacientes, empleados y proveedores.
* Registrar compras y ventas de medicamentos.
* Mantener actualizado el inventario de medicamentos.
* Generar reportes estadísticos e informativos.
* Aplicar conceptos de programación modular y persistencia de datos en archivos JSON.

---

## Tecnologías Utilizadas

### Lenguaje de Programación

* Python 3

### Librerías Utilizadas

* `json`

  * Permite leer y escribir información en archivos JSON.

* `os`

  * Utilizada para validar la existencia de archivos y directorios.

* `datetime`

  * Permite trabajar con fechas para informes, reportes y validación de caducidad.

---

## Estructura del Proyecto

```text
Proyecto_Python_SamuelMantilla/

│
├── data/
│   ├── medicamentos.json
│   ├── proveedores.json
│   ├── pacientes.json
│   ├── empleados.json
│   ├── compras.json
│   └── ventas.json
│
├── modules/
│   ├── medicines/
│   ├── providers/
│   ├── employees/
│   ├── patients/
│   ├── shopping/
│   ├── sales/
│   ├── reports/
│   ├── information/
│   └── utils/
│
├── main.py
└── README.md
```

---

## Persistencia de Datos

El sistema utiliza seis archivos JSON independientes para almacenar la información:

### medicamentos.json

Contiene:

* Nombre del medicamento.
* Precio.
* Stock disponible.
* Fecha de caducidad.
* Proveedor asociado.

### proveedores.json

Contiene:

* Nombre.
* Dirección.
* Teléfono.

### pacientes.json

Contiene:

* Nombre.
* Dirección.
* Teléfono.

### empleados.json

Contiene:

* Nombre.
* Cargo.
* Fecha de contratación.

### compras.json

Contiene:

* Fecha de compra.
* Proveedor.
* Medicamento.
* Cantidad comprada.
* Precio de compra.

### ventas.json

Contiene:

* Fecha de venta.
* Paciente.
* Empleado.
* Medicamento.
* Cantidad vendida.
* Precio de venta.
* Total de la venta.

---

## Funcionalidades Implementadas

### Gestión de Medicamentos

* Agregar medicamentos.
* Buscar medicamentos.
* Modificar medicamentos.
* Eliminar medicamentos.
* Listar medicamentos.

### Gestión de Proveedores

* Agregar proveedores.
* Buscar proveedores.
* Modificar proveedores.
* Eliminar proveedores.
* Listar proveedores.

### Gestión de Pacientes

* Agregar pacientes.
* Buscar pacientes.
* Modificar pacientes.
* Eliminar pacientes.
* Listar pacientes.

### Gestión de Empleados

* Agregar empleados.
* Buscar empleados.
* Modificar empleados.
* Eliminar empleados.
* Listar empleados.

### Gestión de Compras

* Registrar compras.
* Buscar compras.
* Modificar compras.
* Eliminar compras.
* Listar compras.

### Gestión de Ventas

* Registrar ventas.
* Buscar ventas.
* Modificar ventas.
* Eliminar ventas.
* Listar ventas.

---

## Módulo de Informes

El sistema permite generar:

### Informe de Ventas

Muestra:

* Ventas realizadas dentro de un rango de fechas.
* Paciente asociado.
* Empleado responsable.
* Medicamento vendido.
* Cantidad vendida.
* Total generado.

### Informe de Caducidad

Muestra:

* Medicamentos registrados.
* Fecha de expiración.
* Stock disponible.

Permitiendo identificar medicamentos próximos a vencer.

---

## Módulo de Reportes

El sistema incluye reportes como:

* Medicamentos con bajo stock.
* Medicamentos próximos a caducar.
* Medicamento más caro.
* Medicamento menos vendido.
* Medicamentos no vendidos.
* Total de ingresos por ventas.
* Ventas por empleado.
* Pacientes que compraron un medicamento específico.
* Proveedor con mayor suministro.
* Ganancias por proveedor.
* Cantidad de medicamentos por proveedor.
* Entre otros reportes solicitados en el proyecto.

---

## Características del Sistema

* Arquitectura modular.
* Persistencia de datos mediante JSON.
* Código reutilizable mediante funciones.
* Separación de responsabilidades por módulos.
* Fácil mantenimiento y escalabilidad.
* Compatible con Windows, Linux y macOS.

---

## Ejecución

Para ejecutar el proyecto:

```bash
python main.py
```

o

```bash
python3 main.py
```

según el sistema operativo utilizado.

---

## Conclusiones

Este proyecto permitió aplicar conceptos fundamentales de programación en Python como estructuras de datos, modularización, manejo de archivos JSON, validación de datos, generación de reportes y administración de información persistente. Además, proporciona una solución funcional para la gestión básica de una farmacia mediante una interfaz de consola.
