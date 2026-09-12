import json

print ("===Gestor de cobranzas ===")

try:
    with open("consultas.json", "r", encoding="utf-8") as archivo:
        consultas = json.load(archivo)
except FileNotFoundErrir:
    consultas = []
except json.JSONDecodeError:
    print("El archivo tiene un formato inválido. Revisalo antes de contuinuar.")
    raise SystemExit

while True:

    cliente = input("Nombre del cliente: ")

    try:
        deuda = float(input("Deuda inicial: "))
        pago = float(input("Pago recibido: "))
    except ValueError:
        print("Error: ingresá números. Para decimales, usá punto.")
    else:
        
        if deuda < 0 or pago <0:
            print("Error: La deuda y el pago no pueden ser negativos.")
        else:
            saldo = deuda - pago 
            consulta = {
                "cliente": cliente,
                "deuda": deuda,
                "pago": pago,
                "saldo": saldo,
            }
            consultas.append(consulta)
            if saldo == 0:
                print("Deuda Cancelada")
            elif saldo > 0 :
                print("Todavia tiene deuda")
            else:
                print("El pago supera la deuda")
            print(f"\nCliente: {cliente}")
            print(f"Saldo pendiente: ${saldo:.2f}")
    continuar = input("\n¿Consutar otro cliente? (s/n): ").strip().lower()
    if continuar != "s":
        print("Gracias por usar el gestor.")
        break

print("\n=== Resumen de consultas ===")

for consulta in consultas:
    print(f"{consulta['cliente']}: saldo ${consulta['saldo']:.2f}")

try: 
    with open("consultas.json", "w", encoding="utf-8") as archivo:
        json.dump(consultas, archivo, ensure_ascii=False, indent=4)
except OSError:
    print("No se pudieron guardar las consultas.")
else:
    print("Consultas guardadas en consultas.json.")