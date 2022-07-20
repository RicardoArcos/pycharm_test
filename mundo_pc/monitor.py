class Monitor:
    contador_monitores = 0

    def __init__(self, marca, tamano):
        Monitor.contador_monitores += 1
        self._id_monitor = Monitor.contador_monitores
        self._marca = marca
        self._tamano = tamano

    def __str__(self):
        return f'ID: {self._id_monitor}, Marca: {self._marca}, Tamaño: {self._tamano}'
    