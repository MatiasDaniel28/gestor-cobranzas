# Gestor de cobranzas

Proyecto de aprendisaje en Python que permite consutar el saldo
de un clinete a partir de una deuda incial y un pago.

## Funcionalidades

- Solicitar el nombre del cliente, la deuda y el pago.
- Calcular el saldo pendiente.
- Informar si la deuda está cancelada o el pago supera la deuda.
- Rechazar importes negativos y entradas no numéricas.

## Cómo ejecutarlo

Requiere Python 3. No neceita bibliotecas externas.

Desde la carpeta del proyecto:

''' bash
python main.py
'''

Usar punto para los importes decimales, por ejemplo: 1500.50.

## Conceptos practicos

Variables, entrada de datos, condicionales, manejo de excepciones
con try/except y control de versiones en Git y GitHub.

## Limitaciones actuales

- Procesa un cliente por ejecución.
- No guarda los datos al cerrar.
- Utiliza float para los importes; está pendiente mejorar
  la precisión monetaria con Decimal.

  ## Próximas mejoras

  - Consultar varios clientes sin reiniciar.
  - Guardar y recuperar los datos.
  - Agregar pruebas automáticas.