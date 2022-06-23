class Empleado:
    empleados_disponibles = []

    @classmethod
    def conseguir_empleado(cls, empleado_id):
        for empleado in cls.empleados_disponibles:
            if empleado.id == empleado_id:
                return empleado
        return None

    # def __init__(self, nombre, cargo, sueldo):
    def __init__(self, **kwargs):
        self.id = len(self.__class__.empleados_disponibles) + 1
        self.nombre = kwargs["nombre"] # nombre
        self.cargo = kwargs["cargo"] # cargo
        self.sueldo = kwargs["sueldo"] # sueldo
        self.__class__.empleados_disponibles.append(self) 
        # Empleado.empleados_disponibles.append(self)

    def __repr__(self):
        return f"<object {self.__class__}: {self.nombre}>"

    def saludar(self, destinatario):
        return f"Hola, {destinatario.nombre}, soy {self.nombre}, mucho gusto."

class Sala:
    def __init__(self, **kwargs):
        self.capacity = kwargs["capacity"]
        self.vip = kwargs["vip"]
        self.empleado_id = None

    def asignar_encargado(self, empleado_id):
        self.empleado_id = empleado_id

    @property
    def encargado(self):
        # devuelve al empleado con self.empleado_id
        # consultariamos la base de datos para pedir
        # el registro del empleado con empleado_id
        # asignaria a la propiedad encargado el objeto
        # empleado que corresponde al registro
        return Empleado.conseguir_empleado(self.empleado_id)

class Cliente:
    pass

class Ticket:
    pass

class Pelicula:
    pass

class Funcion:
    pass
