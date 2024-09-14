
# Sistema de Gestión de Vehículos

Este proyecto es un sistema de gestión para vehículos, que permite registrar vehículos, mantener un historial de mantenimiento, y realizar búsquedas avanzadas por año de fabricación.

## Funcionalidades

1. **Registro de Vehículos**: Permite agregar vehículos con atributos como:
   - Marca
   - Modelo
   - Año de fabricación
   - Kilometraje
   - Estado (Nuevo o Usado)
   - Tipo de Combustible (Gasolina, Diesel, Eléctrico)
   - **Color** (nuevo atributo añadido)
   - Potencia (nuevo atributo añadido): Indica los caballos de fuerza del vehículo, permitiendo registrar la potencia en unidades de caballos de fuerza (HP).

2. **Historial de Mantenimiento**: Registra los detalles del mantenimiento del vehículo, incluyendo:
   - Fecha del servicio
   - Descripción del servicio
   - Kilometraje en el momento del servicio
   - Costo
   - Mecánico responsable

3. **Búsqueda de Vehículos por Año**: Ahora puedes filtrar vehículos fabricados **antes** o **después** de un año dado.
   - **antes**: Lista vehículos fabricados antes del año especificado.
   - **despues**: Lista vehículos fabricados después del año especificado.

## Instalación y Configuración

1. **Clonar el repositorio**:
   ```bash
   git clone <URL-del-repositorio>
   ```

2. **Acceder al directorio del proyecto**:
   ```bash
   cd <nombre-del-directorio>
   ```

3. **Python deberá estar instalado**.

## Instrucciones de Uso

### Registro de Vehículos
Usa el método `añadir_vehiculo()` de la clase `Main` para registrar un vehículo en el sistema.

### Búsqueda de Vehículos por Año
Puedes buscar vehículos fabricados antes o después de un año dado utilizando el método `buscar_vehiculos_por_año(año, 'antes'/'despues')`.

### Ejemplo de Uso:

```python
# Instanciar el sistema de gestión
sistema = Main()

# Añadir vehículos a la flota
sistema.añadir_vehiculo(Vehiculo("Toyota", "Corolla", 2018, 45000, "Usado", "Gasolina"))
sistema.añadir_vehiculo(Vehiculo("Tesla", "Model S", 2021, 15000, "Nuevo", "Eléctrico"))

# Buscar vehículos fabricados antes del 2020
sistema.buscar_vehiculos_por_año(2020, 'antes')

# Buscar vehículos fabricados después del 2019
sistema.buscar_vehiculos_por_año(2019, 'despues')
```

### Búsqueda por Rango de Años

El sistema permite buscar vehículos dentro de un rango de años. Esta funcionalidad es útil para obtener una lista de vehículos fabricados dentro de un intervalo de tiempo.

Para buscar vehículos dentro de un rango de años, puedes utilizar el método `buscar_vehiculos_por_rango_de_años`.

#### Ejemplo:

```python
sistema.buscar_vehiculos_por_rango_de_años(2018, 2020)
```

Este código buscara los carros del año 2018, 2019 y 2020.
