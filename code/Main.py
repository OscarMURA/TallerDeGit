from Vehicle import Vehiculo

class Main:
    def __init__(self):
        self.vehiculos = []

    # Método para imprimir todos los vehículos registrados
    def mostrar_todos_los_vehiculos(self):
        if not self.vehiculos:
            print("No hay vehículos registrados.")
        else:
            print("Lista de vehículos registrados:")
            for vehiculo in self.vehiculos:
                print(f"Marca: {vehiculo.getMarca()}\n"
                      f"Modelo: {vehiculo.getModelo()}\n"
                      f"Año: {vehiculo.getAño()}\n"
                      f"Kilometraje: {vehiculo.getKilometraje()}\n"
                      f"Estado: {vehiculo.getEstado()}\n"
                      f"Tipo de Combustible: {vehiculo.getTipoCombustible()}\n"
                      f"{'-'*30}")

    # Método para añadir un vehículo a la lista
    def añadir_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print(f"Vehículo {vehiculo.getMarca()} {vehiculo.getModelo()} añadido correctamente.")

    # Método para buscar vehículos por año, permite buscar antes o después del año dado
    def buscar_vehiculos_por_año(self, año, antes_o_despues):
        if antes_o_despues == 'antes':
            encontrados = [vehiculo for vehiculo in self.vehiculos if vehiculo.getAño() < año]
        elif antes_o_despues == 'despues':
            encontrados = [vehiculo for vehiculo in self.vehiculos if vehiculo.getAño() > año]
        else:
            print("Debe especificar 'antes' o 'despues' para el filtro.")
            return

        if encontrados:
            print(f"Vehículos fabricados {antes_o_despues} del año {año}:")
            for vehiculo in encontrados:
                print(f"- {vehiculo.getMarca()} {vehiculo.getModelo()} ({vehiculo.getAño()})")
        else:
            print(f"No se encontraron vehículos fabricados {antes_o_despues} del año {año}.")

    # Método para buscar vehículos por año o rango de años
    def buscar_vehiculos_por_rango_de_años(self, año_inicio, año_fin=None):
        if año_fin is None:
            año_fin = año_inicio
        encontrados = [vehiculo for vehiculo in self.vehiculos if año_inicio <= vehiculo.getAño() <= año_fin]
        if encontrados:
            print(f"Vehículos entre los años {año_inicio} y {año_fin}:")
            for vehiculo in encontrados:
                print(f"- {vehiculo.getMarca()} {vehiculo.getModelo()} ({vehiculo.getAño()})")
        else:
            print(f"No se encontraron vehículos entre los años {año_inicio} y {año_fin}.")

def main():
    sistema = Main()

    # Crear tres vehículos
    vehiculo1 = Vehiculo("Toyota", "Corolla", 2018, 45000, "Usado", "Gasolina")
    vehiculo2 = Vehiculo("Tesla", "Model S", 2021, 15000, "Nuevo", "Eléctrico")
    vehiculo3 = Vehiculo("Ford", "F-150", 2019, 60000, "Usado", "Diesel")

    # Añadir vehículos al sistema
    sistema.añadir_vehiculo(vehiculo1)
    sistema.añadir_vehiculo(vehiculo2)
    sistema.añadir_vehiculo(vehiculo3)

    # Mostrar todos los vehículos registrados
    sistema.mostrar_todos_los_vehiculos()

    # Buscar vehículos fabricados antes del 2020
    sistema.buscar_vehiculos_por_año(2020, 'antes')

    # Buscar vehículos fabricados después del 2019
    sistema.buscar_vehiculos_por_año(2019, 'despues')

    # Buscar vehículos en el rango de años entre 2018 y 2020
    sistema.buscar_vehiculos_por_rango_de_años(2018, 2020)

if __name__ == "__main__":
    main()
