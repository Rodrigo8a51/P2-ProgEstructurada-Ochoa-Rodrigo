"""
Nombre del Alumno: Rodrigo Ochoa Ayala
Matrícula: UX25II052
Fecha: 25 / 05 / 2026
Examen Segundo Parcial - Programación Estructurada
"""
# ==========================================
# 1. IMPORTACIÓN DE BIBLIOTECAS ESTÁNDAR
# ==========================================
import datetime
import math
import random
import statistics
import sys

# ==========================================
# 2. DEFINICIÓN DE CONSTANTES
# ==========================================
MAX_EPOCHS = 10
UMBRAL_ERROR_CRITICO = 0.95

# ==========================================
# 3. FUNCIONES DEFINIDAS POR EL USUARIO
# ==========================================
def obtener_info_sistema():
    """
    Usa la biblioteca 'sys' para validar el entorno de ejecución.
    Requisitos: Realizar 3 llamadas distintas a la biblioteca 'sys'.
    """

    print("\n--- INFORMACIÓN DEL SISTEMA ---")

    print("Sistema operativo:", sys.platform)

    print("Versión de Python:", sys.version)

    print("Tamaño máximo entero:", sys.maxsize)

    print("--- FIN DE INFORMACIÓN DEL SISTEMA ---\n")

def simular_metricas_entrenamiento(cantidad_epochs):
    """
    Usa las bibliotecas 'random' y 'datetime' para simular los datos de entrenamiento.
    Requisitos: 3 llamadas a 'random' y 3 llamadas a 'datetime'.
    """
    # Llamada datetime 1: obtener la fecha y hora exacta de inicio
    inicio_simulacion = datetime.datetime.now()

    # Llamada datetime 2: formatear la fecha de inicio en español (Día/Mes/Año Hora:Minuto:Segundo)
    fecha_formateada = inicio_simulacion.strftime("%d/%m/%Y %H:%M:%S")
    print(f"Inicio de simulación: {fecha_formateada}")

    # Lista de eventos posibles para el log
    eventos_log = ["Epoch exitoso", "Gradiente inestable", "Actualización de pesos"]

    lista_loss = []
    lista_latencia = []

    print("\n--- SIMULACIÓN DE EPOCHS ---")

    contador = 0
    while contador < cantidad_epochs:
        epoch_actual = contador + 1

        loss = random.uniform(0.1, 1.0)

        probabilidad_exito = random.random()

        evento = random.choice(eventos_log)

        latencia = 100 + (loss * 50)

        lista_loss.append(loss)
        lista_latencia.append(latencia)

        if probabilidad_exito >= 0.5:
            estado = "OK"
        else:
            estado = "ADVERTENCIA"

        print(f"  Epoch {epoch_actual:02d} | Loss: {loss:.4f} | Evento: {evento} | Estado: {estado}")

        contador = contador + 1

    fin_simulacion = datetime.datetime.now()
    diferencia_tiempo = fin_simulacion - inicio_simulacion
    print(f"\nTiempo total de simulación: {diferencia_tiempo.total_seconds():.4f} segundos")

    return lista_loss, lista_latencia

def analizar_rendimiento(lista_loss, lista_latencia):
    """
    Usa la biblioteca 'statistics' para analizar el comportamiento del entrenamiento.
    Requisitos: 3 llamadas distintas a la biblioteca 'statistics'.
    """

    print("\n--- ANÁLISIS DE RENDIMIENTO ---")

    media_loss = statistics.mean(lista_loss)
    print(f"Media del Loss:              {media_loss:.4f}")

    if len(lista_loss) > 1:
        desviacion_loss = statistics.stdev(lista_loss)
    else:
        desviacion_loss = 0.0
    print(f"Desviación Estándar del Loss: {desviacion_loss:.4f}")

    mediana_latencia = statistics.median(lista_latencia)
    print(f"Mediana de la Latencia:      {mediana_latencia:.2f} ms")

    print("--- FIN DEL ANÁLISIS ---\n")

    return media_loss

def calcular_rmse(predicciones, reales):
 """
 Usa la biblioteca 'math' para calcular el Root Mean Squared Error (RMSE).
 Requisitos: 3 llamadas distintas a la biblioteca 'math'.
 """
 # TODO: Implementar lógica
 pass
# ==========================================
# 4. PROGRAMA PRINCIPAL (PUNTO DE ENTRADA)
# ==========================================
if __name__ == "__main__":
 print("=== INICIANDO SIMULADOR DE AGENTES DE IA ===")
 # TODO: Invocar las funciones, orquestar el flujo y mostrar reportes ordenados.