import csv
from datetime import datetime
from collections import defaultdict

GASTOS_CSV = "gastos.csv"

def mostrar_menu():
    """Muestra el menú principal del programa."""
    print("\n--- Registro de Gastos Personales ---")
    print("1. Agregar gasto")
    print("2. Ver todos los gastos")
    print("3. Ver total gastado")
    print("4. Filtrar por categoría")
    print("5. Ver resumen mensual")
    print("6. Salir")

def agregar_gasto():
    """Solicita al usuario los datos de un gasto y lo guarda en el archivo CSV."""
    monto = input("Monto del gasto: $")
    categoria = input("Categoría (ej: comida, transporte, ocio): ")
    descripcion = input("Descripción del gasto: ")
    fecha = datetime.now().strftime("%Y-%m-%d")  # Fecha automática

    with open(GASTOS_CSV, mode='a', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([fecha, monto, categoria, descripcion])
    print("✔ Gasto agregado correctamente.")

def ver_gastos():
    """Lee y muestra todos los gastos registrados."""
    try:
        with open(GASTOS_CSV, mode='r') as archivo:
            reader = csv.reader(archivo)
            print("\nFecha       | Monto  | Categoría   | Descripción")
            print("-" * 50)
            for fila in reader:
                print(f"{fila[0]} | ${fila[1]:<6} | {fila[2]:<10} | {fila[3]}")
    except FileNotFoundError:
        print("⚠ No hay gastos registrados aún.")

def ver_total_gastado():
    """Calcula y muestra el total gastado sumando todos los montos."""
    total = 0.0
    try:
        with open(GASTOS_CSV, mode='r') as archivo:
            reader = csv.reader(archivo)
            for fila in reader:
                total += float(fila[1])
        print(f"\n💰 Total gastado: ${total:.2f}")
    except FileNotFoundError:
        print("⚠ No hay gastos registrados aún.")

def filtrar_por_categoria():
    """Muestra los gastos que pertenecen a una categoría específica."""
    categoria_buscada = input("Ingresá la categoría a filtrar: ").lower()
    encontrados = False
    try:
        with open(GASTOS_CSV, mode='r') as archivo:
            reader = csv.reader(archivo)
            print("\nFecha       | Monto  | Categoría   | Descripción")
            print("-" * 50)
            for fila in reader:
                if fila[2].lower() == categoria_buscada:
                    print(f"{fila[0]} | ${fila[1]:<6} | {fila[2]:<10} | {fila[3]}")
                    encontrados = True
        if not encontrados:
            print("⚠ No se encontraron gastos en esa categoría.")
    except FileNotFoundError:
        print("⚠ No hay gastos registrados aún.")

def resumen_mensual():
    """Calcula y muestra el total gastado por mes (año-mes)."""
    resumen = defaultdict(float)
    try:
        with open(GASTOS_CSV, mode='r') as archivo:
            reader = csv.reader(archivo)
            for fila in reader:
                fecha = fila[0]
                monto = float(fila[1])
                mes = fecha[:7]  # yyyy-mm
                resumen[mes] += monto

        print("\n🗓 Resumen mensual de gastos:")
        for mes, total in sorted(resumen.items()):
            print(f"{mes}: ${total:.2f}")
    except FileNotFoundError:
        print("⚠ No hay gastos registrados aún.")

def main():
    """Función principal que ejecuta el menú."""
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ")

        if opcion == '1':
            agregar_gasto()
        elif opcion == '2':
            ver_gastos()
        elif opcion == '3':
            ver_total_gastado()
        elif opcion == '4':
            filtrar_por_categoria()
        elif opcion == '5':
            resumen_mensual()
        elif opcion == '6':
            print("Hasta la próxima 👋")
            break
        else:
            print("Opción no válida. Intentá de nuevo.")

if __name__ == "__main__":
    main()
