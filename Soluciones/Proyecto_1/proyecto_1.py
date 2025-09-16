#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Proyecto 1: Simulación de un problema de física con POO y métodos numéricos.

Este script implementa una simulación de un problema de física utilizando
programación orientada a objetos (POO), herencia múltiple, abstracción,
polimorfismo, encapsulación con decoradores @property, decoradores adicionales
(caching y timing), y un método numérico implementado sin librerías externas
(excepto math). También incluye visualización y animación con Matplotlib.
"""

import math
import time
from functools import wraps
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -----------------------------------------------------------------------------
# 1. Implementación de POO (Herencia, Abstracción, Polimorfismo)
# -----------------------------------------------------------------------------

# Decoradores adicionales (caching y timing)
def timing(func):
    """Decorador para medir el tiempo de ejecución de una función."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Tiempo de ejecución de {func.__name__}: {end_time - start_time:.4f} segundos")
        return result
    return wrapper

def cache(func):
    """Decorador para cachear los resultados de una función."""
    _cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in _cache:
            _cache[key] = func(*args, **kwargs)
        return _cache[key]
    return wrapper

# Clase abstracta para un sistema físico
class SistemaFisico:
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not isinstance(value, str):
            raise ValueError("El nombre debe ser una cadena de texto.")
        self._nombre = value

    def simular(self, dt, pasos):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

    def visualizar(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

# Clase base para un objeto con masa
class ObjetoConMasa:
    def __init__(self, masa):
        self._masa = masa

    @property
    def masa(self):
        return self._masa

    @masa.setter
    def masa(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("La masa debe ser un número positivo.")
        self._masa = value

# Clase para un objeto con posición
class ObjetoConPosicion:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = value

# Clase que hereda de SistemaFisico, ObjetoConMasa y ObjetoConPosicion (Herencia Múltiple)
class Particula(SistemaFisico, ObjetoConMasa, ObjetoConPosicion):
    def __init__(self, nombre, masa, x, y, z, vx, vy, vz):
        SistemaFisico.__init__(self, nombre)
        ObjetoConMasa.__init__(self, masa)
        ObjetoConPosicion.__init__(self, x, y, z)
        self._vx = vx
        self._vy = vy
        self._vz = vz
        self.posiciones = [(x, y, z)]

    @property
    def vx(self):
        return self._vx

    @vx.setter
    def vx(self, value):
        self._vx = value

    @property
    def vy(self):
        return self._vy

    @vy.setter
    def vy(self, value):
        self._vy = value

    @property
    def vz(self):
        return self._vz

    @vz.setter
    def vz(self, value):
        self._vz = value

    @timing
    @cache
    def calcular_fuerza(self, otra_particula=None):
        """Calcula la fuerza sobre la partícula (ejemplo simple: gravedad)."""
        if otra_particula:
            # Ejemplo de fuerza gravitacional simplificada
            G = 6.674e-11  # Constante gravitacional
            r_x = otra_particula.x - self.x
            r_y = otra_particula.y - self.y
            r_z = otra_particula.z - self.z
            r_cuadrado = r_x**2 + r_y**2 + r_z**2
            if r_cuadrado == 0: return (0, 0, 0) # Evitar división por cero
            r = math.sqrt(r_cuadrado)
            fuerza_magnitud = (G * self.masa * otra_particula.masa) / r_cuadrado
            # Componentes de la fuerza
            fx = fuerza_magnitud * (r_x / r)
            fy = fuerza_magnitud * (r_y / r)
            fz = fuerza_magnitud * (r_z / r)
            return fx, fy, fz
        else:
            # Sin otra partícula, fuerza nula o solo gravedad en Z
            return (0, 0, -9.81 * self.masa) # Ejemplo: gravedad en -Z

    @timing
    def simular(self, dt, pasos, otras_particulas=None):
        """Simula el movimiento de la partícula usando el método de Euler."""
        for _ in range(pasos):
            total_fx, total_fy, total_fz = 0, 0, 0
            if otras_particulas:
                for otra in otras_particulas:
                    if otra != self:
                        fx, fy, fz = self.calcular_fuerza(otra)
                        total_fx += fx
                        total_fy += fy
                        total_fz += fz
            else:
                # Si no hay otras partículas, solo consideramos la gravedad en Z
                total_fx, total_fy, total_fz = self.calcular_fuerza()

            # Aceleración
            ax = total_fx / self.masa
            ay = total_fy / self.masa
            az = total_fz / self.masa

            # Actualizar velocidad (método de Euler)
            self.vx += ax * dt
            self.vy += ay * dt
            self.vz += az * dt

            # Actualizar posición (método de Euler)
            self.x += self.vx * dt
            self.y += self.vy * dt
            self.z += self.vz * dt

            self.posiciones.append((self.x, self.y, self.z))

    def visualizar(self):
        """Visualiza la trayectoria de la partícula."""
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        x_data = [p[0] for p in self.posiciones]
        y_data = [p[1] for p in self.posiciones]
        z_data = [p[2] for p in self.posiciones]

        line, = ax.plot(x_data, y_data, z_data, 'b-')
        point, = ax.plot([x_data[0]], [y_data[0]], [z_data[0]], 'ro')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(f'Trayectoria de {self.nombre}')

        def update(frame):
            point.set_data([x_data[frame]], [y_data[frame]])
            point.set_3d_properties([z_data[frame]])
            return line, point

        ani = FuncAnimation(fig, update, frames=len(self.posiciones), blit=True)
        plt.show()

# -----------------------------------------------------------------------------
# Ejemplo de uso
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # Crear una partícula
    particula1 = Particula("Proyectil", 1.0, 0, 0, 100, 10, 5, 0)

    # Simular su movimiento bajo gravedad
    print("\nSimulando movimiento de una partícula bajo gravedad:")
    particula1.simular(dt=0.1, pasos=200)
    particula1.visualizar()

    # Crear dos partículas para simular interacción gravitacional
    particula_a = Particula("Tierra", 5.972e24, 0, 0, 0, 0, 0, 0)
    particula_b = Particula("Luna", 7.342e22, 3.844e8, 0, 0, 0, 1022, 0) # Posición y velocidad inicial de la Luna

    print("\nSimulando interacción gravitacional entre dos partículas:")
    # Para una simulación más realista, se necesitaría un integrador más avanzado
    # y considerar que ambas partículas se afectan mutuamente.
    # Aquí, simplificamos simulando el efecto de la Tierra sobre la Luna.
    # La Tierra se considera fija para este ejemplo simple.
    particula_b.simular(dt=3600, pasos=1000, otras_particulas=[particula_a]) # dt en segundos (1 hora)
    particula_b.visualizar()

    # Demostración de los decoradores
    print("\nDemostración de decoradores:")
    p_test = Particula("Test", 1, 0, 0, 0, 0, 0, 0)
    p_test2 = Particula("Test2", 2, 1, 1, 1, 0, 0, 0)

    # Primera llamada (sin cache)
    p_test.calcular_fuerza(p_test2)
    # Segunda llamada (con cache)
    p_test.calcular_fuerza(p_test2)

    # Cambiar un parámetro para ver que el cache se invalida si la clave cambia
    p_test2.x = 2
    p_test.calcular_fuerza(p_test2)

    # Demostración de encapsulación con @property
    try:
        p_test.masa = -5
    except ValueError as e:
        print(f"Error al intentar asignar masa inválida: {e}")

    try:
        p_test.nombre = 123
    except ValueError as e:
        print(f"Error al intentar asignar nombre inválido: {e}")

    print(f"Masa de p_test: {p_test.masa}")
    print(f"Nombre de p_test: {p_test.nombre}")




