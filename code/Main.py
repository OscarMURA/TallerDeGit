from Vehicle import Vehiculo

class Main:
    def __init__(self):
        self.vehiculos = []
       
    def mostrar_todos_los_vehiculos(self):
        """
        Muestra todos los vehículos registrados en el sistema.

        Si no hay vehículos registrados, imprime un mensaje indicando que no hay vehículos.
        Si hay vehículos registrados, imprime una lista con los detalles de cada vehículo, incluyendo:
        - Marca
        - Modelo
        - Año
        - Kilometraje
        - Estado actual
        - Tipo de combustible
        - Color
        - Potencia en HP

        Returns:
            None
        """
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
                      f"Color: {vehiculo.getColor()}\n"
                      f"Potencia: {vehiculo.getPotencia()} HP\n"
                      f"{'-'*30}")

    
    def añadir_vehiculo(self, vehiculo):
        """
        Añade un vehículo a la lista de vehículos.

        Args:
            vehiculo (Vehiculo): El objeto vehículo que se va a añadir a la lista.

        Returns:
            None
        """
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

    # Crear tres vehículos con nuevos atributos
    vehiculo1 = Vehiculo("Toyota", "Corolla", 2018, 45000, "Usado", "Gasolina", "Rojo", 132)
    vehiculo2 = Vehiculo("Tesla", "Model S", 2021, 15000, "Nuevo", "Eléctrico", "Negro", 670)
    vehiculo3 = Vehiculo("Ford", "F-150", 2019, 60000, "Usado", "Diesel", "Blanco", 395)

    # Añadir vehículos al sistema
    sistema.añadir_vehiculo(vehiculo1)
    sistema.añadir_vehiculo(vehiculo2)
    sistema.añadir_vehiculo(vehiculo3)

    # Mostrar todos los vehículos registrados
    sistema.mostrar_todos_los_vehiculos()

    # Buscar vehículos por año
    sistema.buscar_vehiculos_por_año(2018)

if __name__ == "__main__":
    main()
