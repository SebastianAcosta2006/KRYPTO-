class Entorno:
    def __init__(self, padre=None):
        self._tabla = {}
        self._padre = padre

    def definir(self, nombre, valor):
        if nombre in self._tabla:
            raise RuntimeError(f"'{nombre}' ya esta definido en este ambito")
        self._tabla[nombre] = valor

    def asignar(self, nombre, valor):
        self._tabla[nombre] = valor

    def obtener(self, nombre):
        if nombre in self._tabla:
            return self._tabla[nombre]
        if self._padre:
            return self._padre.obtener(nombre)
        raise RuntimeError(f"Nombre no definido: '{nombre}'")

    def existe_local(self, nombre):
        return nombre in self._tabla

    def nuevo_ambito(self):
        return Entorno(padre=self)
