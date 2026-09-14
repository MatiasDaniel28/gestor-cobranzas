import json
from busquedas import buscar_consultas
from decimal import Decimal
from calculos import calcular_saldo, convertir_importe

def mostrar_saldo(cliente, saldo):
    if saldo < 0:
        print(f"{cliente}: saldo a favor ${abs(saldo):.2f}")
    else:
        print(f"{cliente}: saldo pendiente ${saldo:.2f}")

def guardar_consultas(consultas):
    try:
        with open("consultas.json", "w", encoding="utf-8") as archivo:
            json.dump(
                consultas,
                archivo,
                default=str,
                ensure_ascii=False,
                indent=4,
            )
    except OSError:
        print("No se pudieron guardar las consultas.")
        return False
    return True


print("=== Gestor de cobranzas ===")

try:
    with open("consultas.json", "r", encoding="utf-8") as archivo:
        consultas = json.load(archivo, parse_float=Decimal)

        for consulta in consultas:
            for campo in ("deuda", "pago", "saldo"):
                consulta[campo] = Decimal(str(consulta[campo]))


except FileNotFoundError:
    consultas = []
except json.JSONDecodeError:
    print("El archivo tiene un formato inválido. Revisalo antes de continuar.")
    raise SystemExit

while True:
    print("\n=== Menú ===")
    print("1. Registrar consulta")
    print("2. Ver historial")
    print("3. Guardar y salir")
    print("4. Buscar consultas por nombre")

    opcion = input("Elegí una opción: ").strip()

    if opcion == "1":
        cliente = input("Nombre del cliente: ").strip()

        if not cliente:
            print("Error: ingresá un nombre.")
            continue

        try:
            deuda = convertir_importe(input("Deuda inicial: "))
            pago = convertir_importe(input("Pago Recibido: "))
        except ValueError as error:
            print(f"Error: {error}")
            continue

        saldo = calcular_saldo(deuda, pago)

        consulta = {
            "cliente": cliente,
            "deuda": deuda,
            "pago": pago,
            "saldo": saldo,
        }
        consultas.append(consulta)
        if guardar_consultas(consultas):
            print("Consulta guardada en consultas.json.")
        else:
            print("Laconsulta quedó solo en memoria. Reintentá guardar con la opción 3.")

        if saldo == 0:
            print("Deuda cancelada")
        elif saldo > 0:
            print("Todavía tiene deuda")
        else:
            print("El pago supera la deuda")

        mostrar_saldo(cliente, saldo)

    elif opcion == "2":
        print("\n=== Historial de consultas ===")

        if not consultas:
            print("Todavía no hay consultas.")
        else:
            for consulta in consultas:
                mostrar_saldo(consulta["cliente"], consulta["saldo"])

    elif opcion == "3":
        if guardar_consultas(consultas):
            print("Consultas guardadas en consultas.json.")
            print("Gracias por usar el gestor.")
            break

    elif opcion == "4":
        nombre = input("Nombre a buscar: ").strip()

        if not nombre:
            print("Error: ingresá un nombre.")
            continue

        resultados = buscar_consultas(consultas, nombre)

        if not resultados:
            print("No se encontraron consultas para ese nombre.")
        else:
            for consulta in resultados:
                mostrar_saldo(consulta["cliente"], consulta["saldo"])

    else:
        print("Opción inválida: elegí 1, 2, 3 o 4.")