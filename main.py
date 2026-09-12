import json
from calculos import calcular_saldo


def mostrar_saldo(cliente, saldo):
    if saldo < 0:
        print(f"{cliente}: saldo a favor ${abs(saldo):.2f}")
    else:
        print(f"{cliente}: saldo pendiente ${saldo:.2f}")


print("=== Gestor de cobranzas ===")

try:
    with open("consultas.json", "r", encoding="utf-8") as archivo:
        consultas = json.load(archivo)
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

    opcion = input("Elegí una opción: ").strip()

    if opcion == "1":
        cliente = input("Nombre del cliente: ").strip()

        if not cliente:
            print("Error: ingresá un nombre.")
            continue

        try:
            deuda = float(input("Deuda inicial: "))
            pago = float(input("Pago recibido: "))
        except ValueError:
            print("Error: ingresá números. Para decimales, usá punto.")
            continue

        if deuda < 0 or pago < 0:
            print("Error: la deuda y el pago no pueden ser negativos.")
            continue

        saldo = calcular_saldo(deuda, pago)

        consulta = {
            "cliente": cliente,
            "deuda": deuda,
            "pago": pago,
            "saldo": saldo,
        }
        consultas.append(consulta)

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
        try:
            with open("consultas.json", "w", encoding="utf-8") as archivo:
                json.dump(consultas, archivo, ensure_ascii=False, indent=4)
        except OSError:
            print("No se pudieron guardar las consultas. Intentá nuevamente.")
        else:
            print("Consultas guardadas en consultas.json.")
            print("Gracias por usar el gestor.")
            break

    else:
        print("Opción inválida: elegí 1, 2 o 3.")