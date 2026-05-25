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
    print("--- CÁLCULO DE RMSE ---")

    n = len(predicciones)
    suma_cuadrados = 0.0

    contador = 0
    while contador < n:
        diferencia = predicciones[contador] - reales[contador]

        cuadrado = math.pow(diferencia, 2)

        cuadrado_abs = math.fabs(cuadrado)

        suma_cuadrados = suma_cuadrados + cuadrado_abs
        contador = contador + 1

    mse = suma_cuadrados / n
    rmse = math.sqrt(mse)
    epochs_necesarios = math.ceil(rmse * MAX_EPOCHS)

    print(f"RMSE calculado:              {rmse:.4f}")
    print(f"Epochs recomendados:         {epochs_necesarios}")
    print("--- FIN DEL CÁLCULO RMSE ---\n")

    return rmse

# ==========================================
# 4. PROGRAMA PRINCIPAL (PUNTO DE ENTRADA)
# ==========================================
if __name__ == "__main__":
    print("=" * 48)
    print("=== INICIANDO SIMULADOR DE AGENTES DE IA ===")
    print("=" * 48)

    obtener_info_sistema()

    lista_loss, lista_latencia = simular_metricas_entrenamiento(MAX_EPOCHS)

    media_loss = analizar_rendimiento(lista_loss, lista_latencia)

    predicciones_simuladas = lista_loss
    valores_reales_simulados = []
    indice = 0
    while indice < len(lista_loss):
        valor_real = lista_loss[indice] - 0.05
        valores_reales_simulados.append(valor_real)
        indice = indice + 1

    rmse_final = calcular_rmse(predicciones_simuladas, valores_reales_simulados)

    print("=" * 48)
    print("           REPORTE FINAL DEL ENTRENAMIENTO")
    print("=" * 48)
    print(f"  Media Loss:    {media_loss:.4f}")
    print(f"  RMSE Final:    {rmse_final:.4f}")
    print(f"  Umbral crítico: {UMBRAL_ERROR_CRITICO}")

    if media_loss >= UMBRAL_ERROR_CRITICO:
        print("\n[CRÍTICO] La media del Loss supera el umbral permitido.")
        print("Finalizando el programa con código de error 1...")
        sys.exit(1)
    else:
        print("\n[OK] Las métricas están dentro del rango aceptable.")
        print("Simulación completada exitosamente.")
        print("=" * 48)

"""
CUESTIONARIO DE ANÁLISIS DE BIBLIOTECAS

1. Uso de Objetos y Métodos:
   En datetime.datetime.now(), el objeto/clase es datetime,
   y el método que se llama es now()
   El primer datetime es el nombre de la biblioteca que importamos,
   como esta biblioteca no la creamos nosotros es una biblioteca externa

2. Diferenciación Técnica:
   Cuando usamos import math, para llamar una función tenemos que escribir
   el nombre del módulo primero, mientras que cuando usamos 
   from math import sqrt, ya no necesitamos escribir math.
   adelante, simplemente escribimos sqrt directamente

3. Flujo y Lógica:
   Primero la función simular_metricas_entrenamiento() genera un valor de
   loss aleatorio por cada epoch y los va guardando en una lista llamada
   lista_loss. Al terminar, esa lista se retorna
   En el programa principal ese valor retornado se guarda en una variable
   también llamada lista_loss, luego esa misma variable se pasa como
   argumento a la función calcular_rmse(lista_loss) que recorre la lista,
   calcula las diferencias contra un valor ideal y aplica la fórmula del
   RMSE

4. Mapeo de Tipos de Datos:
   Use dos listas como tipos de datos complejos :
   - lista_loss: guarda todos los valores de loss generados en cada epoch
   - eventos: guarda los posibles mensajes de log del entrenamiento
   Se eligió la lista en lugar de variables simples porque necesitaba
   almacenar múltiples valores del mismo tipo, si hubiéramos usado variables
   simples no podríamos pasarlos fácilmente a las
   funciones

5. Autoevaluación de Abstracción:
   No, no fue necesario programar la fórmula matemática de la desviación
   estándar, solo se escribió statistics.stdev(lista_loss) y la biblioteca
   hizo todo el cálculo internamente, solo necesitamos saber qué
   hace y cómo usarla
"""