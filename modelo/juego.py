import random

class Juego:
    def __init__(self, max_rango):
        self.max_rango = max_rango
        self.numero_adivinar = random.randint(1, max_rango)
        self.intentos_max = max_rango // 20
        self.intentos_hechos = 0

    def hacer_intento(self, intento):
        self.intentos_hechos += 1
        if intento == self.numero_adivinar:
            return "acertó"
        elif intento < self.numero_adivinar:
            return "mayor"
        else:
            return "menor"

    def juego_terminado(self):
        return self.intentos_hechos >= self.intentos_max or self.intentos_hechos == self.intentos_max

    def resultado_final(self):
        if self.intentos_hechos < self.intentos_max:
            return f"¡Felicidades! Adivinaste el número {self.numero_adivinar}."
        else:
            return f"Se acabaron tus intentos. El número correcto era {self.numero_adivinar}."

