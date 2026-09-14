from decimal import Decimal, InvalidOperation



def convertir_importe(texto):
     try:
          importe = Decimal(texto.strip())
     except InvalidOperation:
          raise ValueError("Ingresá un número válido.")

     if not importe.is_finite():
          raise ValueError("El importe debe ser un número finito.")

     if importe < 0:
          raise ValueError("El importe no puede ser negativo.")

     return importe
     



def calcular_saldo(deuda, pago):
     return deuda - pago
