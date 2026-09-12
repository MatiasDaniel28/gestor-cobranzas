

print ("===Gestor de cobranzas ===")

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
        if saldo == 0:
            print("Deuda Cancelada")
        elif saldo > 0 :
            print("Todavia tiene deuda")
        else:
            print("El pago supera la deuda")
        print(f"\nCliente: {cliente}")
        print(f"Saldo pendiente: ${saldo:.2f}")