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
                      f"Estado: {vehiculo.getEstadoActual()}\n"
                      f"Tipo de Combustible: {vehiculo.getTipoCombustible()}\n"
                      f"{'-'*30}")

    # Método para añadir un vehículo a la lista
    def añadir_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print(f"Vehículo {vehiculo.getMarca()} {vehiculo.getModelo()} añadido correctamente.")

    # Método para buscar vehículos por año
    def buscar_vehiculos_por_año(self, año):
        encontrados = [vehiculo for vehiculo in self.vehiculos if vehiculo.getAño() == año]
        if encontrados:
            print(f"Vehículos del año {año}:")
            for vehiculo in encontrados:
                print(f"- {vehiculo.getMarca()} {vehiculo.getModelo()}")
        else:
            print(f"No se encontraron vehículos del año {año}.")

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

    # Buscar vehículos por año
    sistema.buscar_vehiculos_por_año(2018)

if __name__ == "__main__":
    main()
