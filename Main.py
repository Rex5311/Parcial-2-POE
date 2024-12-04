import tkinter as tk
from vista.vista import Vista
from controlador.cotrolador import Controlador

ventana = tk.Tk()

controlador = Controlador(None)  

vista = Vista(ventana, controlador)

controlador.vista = vista

ventana.mainloop()
