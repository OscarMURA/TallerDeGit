# Informe del Proyecto: Sistema de Gestión de Vehículos

## Introducción

Este proyecto consistió en el desarrollo de un **Sistema de Gestión de Vehículos**, que permite registrar vehículos, almacenar su historial de mantenimiento y realizar búsquedas avanzadas de acuerdo a diferentes criterios, como el año de fabricación. El proyecto fue gestionado usando Git y GitHub para el control de versiones, lo que facilitó la colaboración en equipo y la integración de las funcionalidades desarrolladas por cada miembro.


## Miembros del Equipo
LUIS MANUEL ROJAS 
OSCAR MUÑOZ
DIEGO POLANCO
SEBASTIAN ERAZO
ANDRES CHAMORRO

## Funcionalidades Implementadas

- **Clase Vehículo**: Permite registrar vehículos con los atributos: marca, modelo, año de fabricación, kilometraje, estado y tipo de combustible.
- **Clase HistorialMantenimiento**: Almacena información de los mantenimientos realizados a cada vehículo, como la fecha, descripción, kilometraje, costo, y el mecánico encargado.
- **Búsqueda de Vehículos por Año**: Se añadió la funcionalidad de filtrar vehículos por año, permitiendo especificar si se desean buscar vehículos fabricados antes o después de un año dado.
- **Validaciones**: Se añadieron validaciones en la clase `Vehiculo` para que solo acepte tipos de combustible predefinidos (Gasolina, Diesel, Eléctrico).

## Control de Versiones y Resolución de Conflictos

El proyecto fue gestionado usando Git para el control de versiones. Cada funcionalidad fue desarrollada en ramas independientes siguiendo las convenciones de commits acordadas. A continuación, se destacan algunos conflictos que se presentaron y su resolución:

1. **Conflicto en la rama `develop` al realizar merge de funcionalidades de búsqueda por rangos y búsqueda por año**: Durante la integración, se detectó un conflicto en los métodos de búsqueda. La solución fue organizar el código, implementando ambos métodos de manera coherente sin afectar otras funcionalidades.

2. **Conflicto al trabajar en la misma clase (`Main`) en diferentes ramas**: Este conflicto surgió al integrar diferentes funcionalidades en la clase `Main`. Se resolvió revisando cuidadosamente los cambios y fusionando las contribuciones de cada miembro, manteniendo la consistencia de la clase.

## Comunicación en el Equipo

La comunicación entre los miembros del equipo fue fluida y efectiva. Cada miembro reportaba sus avances, problemas y soluciones a tiempo, lo que facilitó la resolución rápida de los conflictos que surgieron durante el desarrollo del proyecto. La colaboración en las revisiones de los pull requests ayudó a mantener la calidad del código y a seguir las buenas prácticas acordadas.
