class Vehiculo:
    def _init_(self, marca, modelo, año, kilometraje, estado):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje
        self.estado = estado

    def getMarca(self):
        return self.marca

    def getModelo(self):
        return self.modelo

    def getAño(self):
        return self.año

    def getKilometraje(self):
        return self.kilometraje

    def getEstado(self):
        return self.estado