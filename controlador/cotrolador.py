from modelo.juego import Juego
from vista.vista import Vista
import tkinter as tk

class Controlador:
    def __init__(self, vista):
        self.vista = vista
        self.juego = None
    
    def iniciar_juego(self):
        try:
            max_rango = self.vista.obtener_rango()
            if max_rango <= 0:
                raise ValueError("El rango debe ser mayor que 0.")
            
            self.juego = Juego(max_rango)
            self.vista.habilitar_intentos()
            self.vista.actualizar_intento(f"Tienes {self.juego.intentos_max} intentos para adivinar el número.")
        except ValueError:
            self.vista.mostrar_mensaje("Por favor, ingresa un número válido para el rango.")
    
    def intentar_adivinar(self):
        try:
            intento = self.vista.obtener_intento()
            resultado = self.juego.hacer_intento(intento)
            
            if resultado == "acertó":
                self.vista.mostrar_mensaje(f"¡Felicidades! Adivinaste el número {self.juego.numero_adivinar}.")
            else:
                if resultado == "mayor":
                    self.vista.actualizar_intento("El número es mayor.")
                else:
                    self.vista.actualizar_intento("El número es menor.")
            
            if self.juego.juego_terminado():
                self.vista.mostrar_mensaje(self.juego.resultado_final())
                self.vista.limpiar_campos()
                self.vista.boton_intentar.config(state=tk.DISABLED)
        except ValueError:
            self.vista.mostrar_mensaje("Por favor, ingresa un número válido para el intento.")


