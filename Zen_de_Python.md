
### Zen de Python – Reflexión

**Principio elegido:**  
> "Simple is better than complex."

Este principio del Zen de Python resalta la importancia de escribir código que sea lo más simple posible. La simplicidad favorece la legibilidad, el mantenimiento del código a largo plazo y facilita el trabajo colaborativo, ya que otros programadores pueden entenderlo rápidamente.

En mi proyecto, apliqué este principio manteniendo una estructura clara: cada funcionalidad está separada en una función específica con una sola responsabilidad (como `agregar_gasto()`, `ver_total_gastado()`, etc.). Evité estructuras complejas o funciones anidadas innecesarias.

Además, utilicé formatos conocidos como `.csv` en lugar de manejar bases de datos o archivos binarios, porque para el alcance del proyecto resultaba más simple, suficiente y comprensible.

La simplicidad también está en la interfaz: un menú de texto directo que guía al usuario paso a paso, sin distracciones. Esta decisión permite que cualquier persona con conocimientos básicos pueda usar el programa.

**Ejemplo en el código:**  
```python
def ver_total_gastado():
    total = 0.0
    try:
        with open(GASTOS_CSV, mode='r') as archivo:
            reader = csv.reader(archivo)
            for fila in reader:
                total += float(fila[1])
        print(f"\n💰 Total gastado: ${total:.2f}")
    except FileNotFoundError:
        print("⚠ No hay gastos registrados aún.")
```

Este fragmento resuelve una tarea importante con una lógica muy simple y fácil de entender. No utiliza ningún módulo externo complejo ni estructuras rebuscadas. Simple y funcional.

**Conclusión:**  
Aplicar este principio me ayudó a mantener el foco en la funcionalidad y no en la sofisticación. Aprendí que muchas veces, el mejor código no es el más inteligente, sino el más claro.
