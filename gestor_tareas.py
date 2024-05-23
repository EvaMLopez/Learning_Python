import json

class Tarea:
    # Inicializa una tarea con una descripción y un estado de completado
    def __init__(self, descripcion, completada=False):
        self.descripcion = descripcion
        self.completada = completada

    # Marca la tarea como completada
    def completar(self):
        self.completada = True
    
    # Crea una tarea a partir de valores de descripción y completado
    @classmethod
    def from_values(cls, descripcion, completada):
        tarea = cls.__new__(cls)
        tarea.__init__(descripcion, completada)
        return tarea

class ListaTareas:
    #  Inicializa una lista de tareas con un nombre de archivo y una lista vacía de tareas
    def __init__(self, filename="tareas.json"):
        self.filename = filename
        self.tareas = [] 
        self.cargar_tareas()

    # Agrega una tarea a la lista de tareas
    def agregar_tarea(self, descripcion):
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)
        self.guardar_tareas()

    # Marca una tarea como completada en la lista de tareas
    def marcar_completada(self, posicion):
        try:
            tarea = self.tareas[posicion]
            if tarea.completada:
                print("\n La tarea ya se ha completado.")
            else:
                tarea.completar()
                print("\n Se ha marcado la tarea como completada.")
        except IndexError:
            print("\n La posición ingresada no existe en la lista.")
        self.guardar_tareas()

    # Muestra todas las tareas en la lista de tareas
    def mostrar_tareas(self):
        if len(self.tareas) == 0:
            print("\n Actualmente no hay ninguna tarea.")
        else:
            print("\n ✧ Tareas:")
            for i, tarea in enumerate(self.tareas):
                estado = "Completada ✓ " if tarea.completada else "Pendiente ✗"
                print(f"{i+1}. {tarea.descripcion} - {estado}")
    
    #  Elimina una tarea de la lista de tareas
    def eliminar_tarea(self, posicion):
        try:
                del self.tareas[posicion]
                print("\n Se ha eliminado la tarea.")
        except IndexError:
            print("\n La posición ingresada no existe en la lista.")
        self.guardar_tareas()
    
    # Guarda la lista de tareas en un archivo JSON
    def guardar_tareas(self):
        with open(self.filename, 'w') as file:
            json.dump([[tarea.descripcion, tarea.completada] for tarea in self.tareas], file)

    # Carga la lista de tareas desde un archivo JSON
    def cargar_tareas(self):
        try:
            with open(self.filename, 'r') as file:
                self.tareas = [Tarea.from_values(*t) for t in json.load(file)]
        except FileNotFoundError:
            self.tareas = []

# Muestra el menú de opciones
def mostrar_menu():
    print("\n ★  Menú de opciones ★")
    print("1. Agregar tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar tareas")
    print("4. Eliminar tarea")
    print("5. Salir")

# Pide al usuario una opción válida y la devuelve
def pedir_opcion():
    while True:
        try:
            opcion = int(input(" ➥  Ingrese una opción: "))
            if opcion >= 1 and opcion <= 5:
                return opcion
            else:
                print("Opción inválida. Por favor, ingrese un número entre 1 y 5.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese una opción válida.")

def pedir_descripcion():
    return input("\n Ingrese la descripción de la tarea: ")

def pedir_posicion():
    while True:
        try:
            posicion = int(input("\n Ingrese la posición de la tarea: "))
            return posicion
        except ValueError:
            print("\n Entrada inválida. Por favor, ingrese una opción válida.")

# Función principal del programa
def main():
    lista_tareas = ListaTareas()

    while True:
        mostrar_menu()
        opcion = pedir_opcion()

        if opcion == 1:
            descripcion = pedir_descripcion()
            lista_tareas.agregar_tarea(descripcion)
            print(f"\n Se ha agregado la tarea '{descripcion}'.")
        elif opcion == 2:
            posicion = pedir_posicion()
            lista_tareas.marcar_completada(posicion-1)
        elif opcion == 3:
            lista_tareas.mostrar_tareas()
        elif opcion == 4:
            if len(lista_tareas.tareas) == 0:
                print("\n Actualmente no hay ninguna tarea para eliminar.")
            else:
                posicion = pedir_posicion()
                lista_tareas.eliminar_tarea(posicion-1)
        elif opcion == 5:
            print("\n ¡Hasta pronto!")
            break

if __name__ == "__main__":
    main()
