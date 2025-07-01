
### 📂 Unidad 10 – Archivos

#### 📘 Análisis teórico

El manejo de archivos es un pilar clave en cualquier lenguaje de programación que interactúe con datos de manera persistente. Python simplifica esta tarea con una sintaxis clara, métodos accesibles y una estructura multiplataforma que abstrae muchos detalles del sistema operativo.

La unidad 10 del libro “Python desde cero, fundamentos claros” de Juan Pablo Sosa presenta los conceptos esenciales del tratamiento de archivos, destacando:

- **Persistencia de datos:** permite que la información sobreviva más allá de una ejecución.
- **Interacción con el mundo exterior:** muchos programas deben leer o guardar datos externos (CSV, logs, configuraciones).
- **Accesibilidad multiplataforma:** Python gestiona automáticamente diferencias entre sistemas (por ejemplo, / vs \).

##### 🛠 Principales operaciones con archivos

1. **Apertura de archivos**
   ```python
   archivo = open("datos.txt", "r", encoding="utf-8")
   ```

2. **Lectura**
   - `.read()`, `.readline()`, `.readlines()`

3. **Escritura**
   - `.write()`, `.writelines()`

4. **Cierre**
   - `archivo.close()`

El uso del contexto `with open(...) as archivo:` es la mejor práctica, ya que garantiza el cierre automático del archivo incluso si hay errores.

##### 💡 Streams y handles

- **Handle**: acceso que proporciona Python a un archivo abierto.
- **Stream**: flujo de datos entre el programa y el archivo.
- **Modos comunes**:
  - `'r'`: lectura
  - `'w'`: escritura (sobrescribe)
  - `'a'`: agregar al final
  - `'r+'`: lectura y escritura

#### 🔁 Aplicación en mi proyecto

En mi programa `gastos.py`, utilizo archivos CSV para almacenar registros de gastos:

```python
with open(GASTOS_CSV, mode='a', newline='') as archivo:
    writer = csv.writer(archivo)
    writer.writerow([fecha, monto, categoria, descripcion])
```

Este enfoque permite:
- Almacenar datos entre sesiones.
- Leer y filtrar información (por categoría, por fecha).
- Calcular totales y generar resúmenes sin usar bases de datos.

La teoría de esta unidad fundamenta directamente las operaciones que uso, como:
- apertura de archivos en modo 'r' y 'a',
- lectura de registros línea por línea con `csv.reader`,
- y la importancia de cerrar correctamente el archivo, lo cual hago con `with`.

#### 🧠 Reflexión

Esta unidad muestra cómo un concepto aparentemente técnico (streams, handles) se convierte en una herramienta práctica y concreta al momento de desarrollar proyectos reales. Entender su funcionamiento no solo mejora la eficiencia del código, sino que también prepara el camino para proyectos más avanzados que usen APIs, bases de datos o interacción con múltiples archivos.
