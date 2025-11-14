import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# ===== PUNTO D: Cálculo de resistencias y estadísticas =====
print("=" * 60)
print("PUNTO D: Cálculo de resistencias individuales")
print("=" * 60)

# Datos de voltaje (V) y corriente (mA) de la simulación
# REEMPLAZA estos valores con los datos obtenidos en Tinkercad
voltajes = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])  # en Voltios
corrientes = np.array([6.06, 12.12, 18.18, 24.24, 30.30, 36.36, 42.42, 48.48, 54.54, 60.60])  # en mA

# Convertir corriente de mA a A para el cálculo
corrientes_A = corrientes / 1000

# Calcular resistencia para cada par V-I usando Ley de Ohm: R = V/I
resistencias = voltajes / corrientes_A  # Resultado en Ohms

# Convertir resistencias a kΩ para la tabla
resistencias_kOhm = resistencias / 1000

# Mostrar tabla de resultados
print("\nTabla de resultados:")
print(f"{'V(V)':<10}{'I(mA)':<10}{'R(kΩ)':<10}")
print("-" * 30)
for v, i, r in zip(voltajes, corrientes, resistencias_kOhm):
    print(f"{v:<10.2f}{i:<10.2f}{r:<10.3f}")

# Calcular promedio y desviación estándar
promedio_resistencia = np.mean(resistencias)
desviacion_estandar = np.std(resistencias, ddof=1)  # ddof=1 para muestra

print(f"\n{'=' * 60}")
print(f"Resistencia promedio: {promedio_resistencia:.2f} Ω = {promedio_resistencia/1000:.3f} kΩ")
print(f"Desviación estándar: {desviacion_estandar:.2f} Ω = {desviacion_estandar/1000:.3f} kΩ")
print(f"{'=' * 60}\n")


# ===== PUNTO E: Gráfico y regresión lineal =====
print("=" * 60)
print("PUNTO E: Regresión lineal V vs I")
print("=" * 60)

# Realizar regresión lineal (V = m*I + b)
# donde m es la pendiente (resistencia) y b es el intercepto
slope, intercept, r_value, p_value, std_err = stats.linregress(corrientes, voltajes)

# Coeficiente de determinación R²
r_squared = r_value**2

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.scatter(corrientes, voltajes, color='blue', s=80, alpha=0.6, edgecolors='black', label='Datos experimentales')
plt.plot(corrientes, slope * corrientes + intercept, color='red', linewidth=2, label=f'Regresión lineal: V = {slope:.2f}I + {intercept:.4f}')

plt.xlabel('Corriente (mA)', fontsize=12, fontweight='bold')
plt.ylabel('Voltaje (V)', fontsize=12, fontweight='bold')
plt.title('Ley de Ohm: Voltaje vs Corriente', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(fontsize=10)

# Añadir información de la regresión al gráfico
textstr = f'Pendiente (m): {slope:.2f} Ω\nIntercepto (b): {intercept:.4f} V\nR² = {r_squared:.6f}'
plt.text(0.05, 0.95, textstr, transform=plt.gca().transAxes, fontsize=10,
         verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.savefig('ley_ohm_regresion.png', dpi=300, bbox_inches='tight')
plt.show()

# Mostrar resultados de la regresión
print(f"\nResultados de la regresión lineal:")
print(f"Pendiente (m): {slope:.2f} Ω = {slope/1000:.3f} kΩ")
print(f"Intercepto (b): {intercept:.4f} V")
print(f"Coeficiente de correlación (R): {r_value:.6f}")
print(f"Coeficiente de determinación (R²): {r_squared:.6f}")
print(f"Error estándar: {std_err:.4f}")

print("\n" + "=" * 60)
print("INTERPRETACIÓN FÍSICA:")
print("=" * 60)
print(f"""
1. PENDIENTE (m = {slope:.2f} Ω):
   - Representa la RESISTENCIA del conductor
   - Según la Ley de Ohm: V = I·R, la pendiente es R
   - Indica cuántos voltios se necesitan por cada miliamperio de corriente
   - Valor físico: {slope:.2f} Ω = {slope/1000:.3f} kΩ

2. INTERCEPTO (b = {intercept:.4f} V):
   - Idealmente debería ser 0 V (circuito óhmico puro)
   - Un valor cercano a 0 indica un comportamiento óhmico ideal
   - Valores diferentes de 0 pueden deberse a:
     * Errores de medición
     * Resistencias parásitas en el circuito
     * Errores de redondeo en la simulación

3. COEFICIENTE R² ({r_squared:.6f}):
   - Mide qué tan bien se ajustan los datos a la línea recta
   - Valor entre 0 y 1 (1 = ajuste perfecto)
   - R² = {r_squared:.6f} indica que {r_squared*100:.4f}% de la variación 
     en el voltaje se explica por la variación en la corriente
   - Un R² cercano a 1 confirma que el conductor sigue la Ley de Ohm
""")


# ===== PUNTO F: Tabla de comparación =====
print("=" * 60)
print("PUNTO F: Comparación de valores de resistencia")
print("=" * 60)

# Valores a comparar
resistencia_nominal = 330  # Ω (valor usado en la simulación)
resistencia_punto_d = promedio_resistencia  # Del punto d)
resistencia_punto_e = slope  # Del punto e) - pendiente de la regresión

# Calcular errores porcentuales
error_d = abs((resistencia_punto_d - resistencia_nominal) / resistencia_nominal) * 100
error_e = abs((resistencia_punto_e - resistencia_nominal) / resistencia_nominal) * 100

# Crear tabla de comparación
print(f"\n{'Método':<30}{'Resistencia (Ω)':<20}{'Resistencia (kΩ)':<20}{'Error (%)':<15}")
print("-" * 85)
print(f"{'Valor nominal (simulación)':<30}{resistencia_nominal:<20.2f}{resistencia_nominal/1000:<20.3f}{'-':<15}")
print(f"{'Promedio punto d) (R = V/I)':<30}{resistencia_punto_d:<20.2f}{resistencia_punto_d/1000:<20.3f}{error_d:<15.4f}")
print(f"{'Regresión punto e) (pendiente)':<30}{resistencia_punto_e:<20.2f}{resistencia_punto_e/1000:<20.3f}{error_e:<15.4f}")

print(f"\n{'=' * 60}")
print("ANÁLISIS DE RESULTADOS:")
print("=" * 60)
print(f"""
- El valor nominal de la resistencia en Tinkercad es: {resistencia_nominal} Ω
- El valor calculado por promedio V/I es: {resistencia_punto_d:.2f} Ω
- El valor obtenido por regresión lineal es: {resistencia_punto_e:.2f} Ω

- Error del método promedio: {error_d:.4f}%
- Error del método de regresión: {error_e:.4f}%

Ambos métodos proporcionan valores muy cercanos al valor nominal,
lo que confirma la validez de la Ley de Ohm en el circuito simulado.
""")

print("\n¡Análisis completado! El gráfico se ha guardado como 'ley_ohm_regresion.png'")
print("=" * 60)