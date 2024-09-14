class HistorialMantenimiento:
    def __init__(self, fecha, descripcion, kilometraje, costo, mecanico):
        self.fecha = fecha
        self.descripcion = descripcion
        self.kilometraje = kilometraje
        self.costo = costo
        self.mecanico = mecanico

    def getFecha(self):
        return self.fecha

    def getDescripcion(self):
        return self.descripcion

    def getKilometraje(self):
        return self.kilometraje

    def getCosto(self):
        return self.costo

    def getMecanico(self):
        return self.mecanico

    def setFecha(self, fecha):
        self.fecha = fecha

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def setKilometraje(self, kilometraje):
        self.kilometraje = kilometraje

    def setCosto(self, costo):
        self.costo = costo

    def setMecanico(self, mecanico):
        self.mecanico = mecanico

    def __str__(self):
        return f"Fecha: {self.fecha}, Descripción: {self.descripcion}, Kilometraje: {self.kilometraje}, Costo: {self.costo}, Mecánico: {self.mecanico}"
