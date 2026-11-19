# Práctica D4. Gestor de la caja de un comercio

Módulo 0485 Programación · UD 3 · 1.º DAW · Curso 2026/2027
Autores: Diego Sánchez Azorín y Alejandro García Da Silva

## Qué hace

Es una aplicación de consola para llevar la caja de un comercio durante un día. Tiene un menú que se repite hasta que se cierra la caja:

1. Registrar una venta (importe y forma de pago: efectivo, tarjeta o Bizum)
2. Anular la última venta
3. Consultar la caja (total del día, número de operaciones, importe medio y venta mayor)
4. Cerrar la caja mostrando un resumen

## Cómo ejecutarlo

```
python caja.py
```

## Cómo está hecho

El menú es un `while` que se repite mientras la caja esté abierta, y la opción se elige con `match`. La forma de pago se elige con `if` / `elif` / `else`.

Los datos se guardan con los cuatro patrones del capítulo 8: un contador de operaciones, acumuladores para el total y para cada forma de pago, un extremo para la venta mayor y dos interruptores, uno para saber si se puede anular y otro para saber si se ha anulado alguna venta.

Todas las entradas tienen control de excepciones con `try/except`. El importe tiene que ser mayor que 0 y como mucho 10000 €, y admite coma o punto para los decimales.

El código está repartido en funciones con docstring: `mostrar_menu`, `pedir_entero`, `pedir_importe`, `pedir_forma_pago`, `confirmar`, `mostrar_datos`, `mostrar_resumen` y `main`.
