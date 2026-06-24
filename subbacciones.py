#subacciones necesarias
def CargarLibro () #procedimiento
    #pedir los datos del libro, armar el registro (TipoLibro) y guardarlo en el archivo "Libros.txt"
    
def BuscarLibro () #procedimiento
    #Recorre el archivo "libros.txt", verifica que el libro exista y que haya stock
    
def MostrarLibros () #procedimiento
    #Recorre el archivo "libros.txt" y muestra todos los libros que hay en stock
    
def EmitirPrestamo () #procedimiento
    #Solicita DNI del usuario y algún dato único del libro, verifica stock y guarda el pretamo en el archivo "prestamos.txt"

def DevolverLibro () #procedimiento
    #Solicita DNI del usuario y algún dato único del libro, verifica que el prestamo exista y lo elimina del archivo "prestamos.txt" o marca como devuelto

def MostrarPrestamos () #procedimiento
    #Recorre el archivo "prestamos.txt" y muestra todos los prestamos activos
    
def CalcularMulta () #procedimiento
    #selecciona un prestamo activo, calcula la multa según la fecha de devolución y la fecha actual y la muestra al usuario
