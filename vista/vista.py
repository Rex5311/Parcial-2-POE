import tkinter as tk
from tkinter import messagebox

class Vista:
    def __init__(self, ventana, controlador):
        self.ventana = ventana
        self.controlador = controlador  
        self.ventana.title("Juego Adivina el Número")
        self.ventana.geometry("300x250")
        
        self.instrucciones = tk.Label(ventana, text="Introduce el rango máximo:")
        self.instrucciones.pack(pady=10)
        
        self.entrada_rango = tk.Entry(ventana)
        self.entrada_rango.pack(pady=10)
        
        self.boton_iniciar = tk.Button(ventana, text="Iniciar Juego", command=self.controlador.iniciar_juego)  # Llamamos al método del controlador
        self.boton_iniciar.pack(pady=10)
        
        self.entrada_numero = tk.Entry(ventana)
        self.entrada_numero.pack(pady=10)
        
        self.boton_intentar = tk.Button(ventana, text="Intentar", state=tk.DISABLED, command=self.controlador.intentar_adivinar)  # Llamamos al controlador también
        self.boton_intentar.pack(pady=10)

        self.resultado = tk.Label(ventana, text="", font=("Arial", 12))
        self.resultado.pack(pady=10)
    
    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo("Resultado", mensaje)
    
    def actualizar_intento(self, mensaje):
        self.resultado.config(text=mensaje)
    
    def habilitar_intentos(self):
        self.boton_intentar.config(state=tk.NORMAL)
    
    def obtener_rango(self):
        return int(self.entrada_rango.get())

    def obtener_intento(self):
        return int(self.entrada_numero.get())
    
    def limpiar_campos(self):
        self.entrada_numero.delete(0, tk.END)
