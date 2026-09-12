

print ("===Gestor de cobranzas ===")

cliente = input("Nombre del cliente: ")
deuda = float(input("Deuda inicial: "))
pago = float(input("Pago recibido: "))


saldo = deuda - pago 
if saldo == 0:
    print("Deuda Cancelada")
elif saldo > 0 :
    print("Todavia tiene deuda")
else:
    print("El pago supera la deuda")
print(f"\nCliente: {cliente}")
print(f"Saldo pendiente: ${saldo:.2f}")