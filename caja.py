"""
Práctica D4. Gestor de la caja de un comercio.

Aplicación de consola con un menú que se repite hasta cerrar la caja.
Permite registrar ventas con su forma de pago, anular la última venta,
consultar los datos del día y cerrar la caja mostrando un resumen.

Módulo 0485 Programación · UD 3 · 1.º DAW · Curso 2026/2027
Autores: Diego Sánchez Azorín y Alejandro García Da Silva
"""

IMPORTE_MAXIMO = 10000


def mostrar_menu():
    """Muestra las opciones del menú principal."""
    print("\n===== CAJA DEL COMERCIO =====")
    print("1. Registrar una venta")
    print("2. Anular la última venta")
    print("3. Consultar la caja")
    print("4. Cerrar la caja")


def pedir_entero(mensaje, minimo, maximo):
    """Pide un número entero entre minimo y maximo y lo devuelve.

    Si no es un número o está fuera del rango, avisa y lo vuelve a pedir.
    """
    while True:
        try:
            numero = int(input(mensaje))
        except ValueError:
            print("Error: tienes que escribir un número entero")
            continue
        if minimo <= numero <= maximo:
            return numero
        print(f"Error: tiene que estar entre {minimo} y {maximo}")


def pedir_importe():
    """Pide el importe de una venta y lo devuelve redondeado a céntimos.

    Tiene que ser mayor que 0 y no pasar de IMPORTE_MAXIMO.
    Acepta los decimales con punto o con coma.
    """
    while True:
        texto = input("Importe de la venta (€): ").replace(",", ".")
        try:
            importe = float(texto)
        except ValueError:
            print("Error: el importe tiene que ser un número")
            continue
        if 0 < importe <= IMPORTE_MAXIMO:
            return round(importe, 2)
        if importe <= 0:
            print("Error: el importe tiene que ser mayor que 0")
        else:
            print(f"Error: el importe no puede pasar de {IMPORTE_MAXIMO} €")


def pedir_forma_pago():
    """Pregunta la forma de pago y devuelve su nombre."""
    print("Formas de pago: 1. Efectivo  2. Tarjeta  3. Bizum")
    opcion = pedir_entero("Elige la forma de pago: ", 1, 3)
    if opcion == 1:
        return "Efectivo"
    elif opcion == 2:
        return "Tarjeta"
    else:
        return "Bizum"


def confirmar(mensaje):
    """Hace una pregunta de s/n y devuelve True si la respuesta es s."""
    respuesta = input(mensaje).strip().lower()
    while respuesta not in ("s", "n"):
        respuesta = input("Responde s o n: ").strip().lower()
    return respuesta == "s"


def mostrar_datos(total, operaciones, mayor):
    """Muestra el total, las operaciones, el importe medio y la venta mayor."""
    if operaciones == 0:
        print("Todavía no hay ninguna venta registrada")
        return
    media = total / operaciones
    print(f"Total del día: {total:.2f} €")
    print(f"Número de operaciones: {operaciones}")
    print(f"Importe medio: {media:.2f} €")
    print(f"Venta mayor: {mayor:.2f} €")


def mostrar_resumen(total, operaciones, mayor, efectivo, tarjeta, bizum, hubo_anulacion):
    """Muestra el resumen final al cerrar la caja."""
    print("\n===== RESUMEN DEL CIERRE =====")
    mostrar_datos(total, operaciones, mayor)
    print(f"En efectivo: {efectivo:.2f} €")
    print(f"Con tarjeta: {tarjeta:.2f} €")
    print(f"Por Bizum: {bizum:.2f} €")
    if hubo_anulacion:
        print("Durante el día se ha anulado alguna venta")
    else:
        print("No se ha anulado ninguna venta")
    print("Caja cerrada. ¡Hasta mañana!")


def main():
    """Controla el menú y guarda los datos de la caja con los patrones del capítulo 8."""
    # Contador y acumuladores
    operaciones = 0
    total = 0.0
    efectivo = 0.0
    tarjeta = 0.0
    bizum = 0.0
    # Extremo: empieza en None hasta que hay una venta
    mayor = None
    # Interruptores
    hubo_anulacion = False
    puede_anular = False
    # Datos de la última venta, para poder anularla
    ultimo_importe = 0.0
    ultima_forma = ""
    mayor_previo = None

    caja_abierta = True
    while caja_abierta:
        mostrar_menu()
        opcion = pedir_entero("Elige una opción: ", 1, 4)
        match opcion:
            case 1:
                importe = pedir_importe()
                forma = pedir_forma_pago()
                operaciones += 1
                total = round(total + importe, 2)
                if forma == "Efectivo":
                    efectivo = round(efectivo + importe, 2)
                elif forma == "Tarjeta":
                    tarjeta = round(tarjeta + importe, 2)
                else:
                    bizum = round(bizum + importe, 2)
                mayor_previo = mayor
                if mayor is None or importe > mayor:
                    mayor = importe
                ultimo_importe = importe
                ultima_forma = forma
                puede_anular = True
                print(f"Venta registrada: {importe:.2f} € ({forma})")
            case 2:
                if not puede_anular:
                    print("No hay ninguna venta que se pueda anular")
                else:
                    operaciones -= 1
                    total = round(total - ultimo_importe, 2)
                    if ultima_forma == "Efectivo":
                        efectivo = round(efectivo - ultimo_importe, 2)
                    elif ultima_forma == "Tarjeta":
                        tarjeta = round(tarjeta - ultimo_importe, 2)
                    else:
                        bizum = round(bizum - ultimo_importe, 2)
                    mayor = mayor_previo
                    puede_anular = False
                    hubo_anulacion = True
                    print(f"Venta anulada: {ultimo_importe:.2f} € ({ultima_forma})")
            case 3:
                mostrar_datos(total, operaciones, mayor)
            case 4:
                if confirmar("¿Seguro que quieres cerrar la caja? (s/n): "):
                    mostrar_resumen(total, operaciones, mayor, efectivo, tarjeta, bizum, hubo_anulacion)
                    caja_abierta = False


main()
