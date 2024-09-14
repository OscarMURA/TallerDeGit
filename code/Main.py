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

def main():
    
    