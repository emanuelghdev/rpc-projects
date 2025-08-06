import signal
import sys

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from calculadora import CalculadoraService

def obtener_expresion():
    while True:
        expresion = input("Introduce la expresión (La calculadora está en modo escalar, ingrese 'f' para ver el formato, 'v' para hacer operaciones con vectores): ")
        if expresion == 'v':
            return expresion
        partes = expresion.split()
        if len(partes) == 3:
            operando1, operador, operando2 = partes
            if operador.lower() in ["+", "-", "*", "/"]:
                try:
                    operando1 = float(operando1)
                    operando2 = float(operando2)
                    return operando1, operador, operando2
                except ValueError:
                    print("Error: Los operandos deben ser números.")
            else:
                print("Expresión no válida. Debe ser en el formato '<operando><operador><operando>' para las operaciones binarias\n")
        elif len(partes) == 2:
            operador, operando = partes
            if operador.lower() in ["sen", "cos", "tan", "grad->rad", "rad->grad"]:
                try:
                    operando = float(operando)
                    return operador, operando
                except ValueError:
                    print("Error: El operando debe ser un número.\n")
            else:
                print("Expresión no válida. Debe ser en el formato '<operador><operando>' para las operaciones trigonométricas o de conversión\n")
        elif len(partes) == 1 and partes[0] == "f":
            print("Formato: <operando1><operador><operando2> ó <operador_trignometrico><operando> ó <operador_conversion><operando>" +
                  "\nOperadores disponibles: suma (+), resta (-), multiplicacion (*), division (/), seno (sen), coseno (cos)," +
                  "tangente (tan), convertir grados a radianes (grad->rad), convertir radianes a grados (grad->rad)" +
                  "\nEjemplos: 5 + 12 | 84 / 12 | sen 45 | grad->rad 240\n")
        else:
            print("Expresión no válida. Debe ser en el formato '<operando><operador><operando>' para operaciones binarias o '<operador><operando>' para operaciones trigonométricas o de conversión\n")


def obtener_expresion_vectorial():
    while True:
        expresion = input("Introduce la expresión (La calculadora está en modo vectorial, ingrese 'f' para ver el formato, 'b' para hacer operaciones binarias y trignometricas): ")
        if expresion == 'b':
            return expresion
        partes = expresion.split()
        if len(partes) == 3:
            operando1, operador, operando2 = partes
            if ';' in operando1 and ';' in operando2 and operador.lower() in ["+", "-", "*"]:
                try:
                        matriz1 = [list(map(float, row.split(','))) for row in operando1.split(';')]
                        matriz2 = [list(map(float, row.split(','))) for row in operando2.split(';')]
                        return matriz1, operador, matriz2
                except ValueError:
                    print("Error: Los elementos de la matriz deben ser números y estar separados por comas (,) sin espacio entre mediasy las filas deben estar separadas por punto y coma (;) sin espacio entre medias.")
            elif operador.lower() in ["+", "-", "*", "x"]:
                try:
                    vector1 = list(map(float, operando1.split(',')))
                    vector2 = list(map(float, operando2.split(',')))
                    return vector1, operador, vector2
                except ValueError:
                    print("Error: Los operandos deben ser números y estar separados por comas (,) sin espacio entre medias.")
            else:
                print("Expresión no válida. Debe ser en el formato '<vector1><operador><vector2>' para operaciones con vectores y '<matriz1><operador><matriz2>' o '<operador><matriz>' para operaciones con matrices\n")
        elif len(partes) == 2:
            operador, operando = partes
            if operador.lower() in ["tras","inv","det"]:
                try:
                    matriz = [list(map(float, row.split(','))) for row in operando.split(';')]
                    return operador, matriz
                except ValueError:
                    print("Error: Los elementos de la matriz deben ser números y estar separados por comas (,) sin espacio entre medias y las filas deben estar separadas por punto y coma (;) sin espacio entre medias.")
            else:
                print("Expresión no válida. Debe ser en el formato '<operador><matriz>' para las operaciones de calcular la traspuesta o el determinante de la matriz\n")
        elif len(partes) == 1 and partes[0] == "f":
            print("Formato: <vector1><operador><vector2>, <matriz1><operador><matriz2> ó <operador><matriz>" +
                  "\nOperadores disponibles: suma (+), resta (-), producto escalar y matricial (*), producto vectorial (X)(solo para vectores), traspuesta de una matriz (tras) y determinante de una matriz (det)" +
                  "\nEjemplos: 1,2,3 + 4,5,6 | 3,2;5,6 * 3,4;9,1 | det 2,2;3,4;5,6\n")
        else:
            print("Expresión no válida. Debe ser en el formato '<vector1><operador><vector2>' para las operaciones con vectores y <matriz1><operador><matriz2> o '<operador><matriz>' para la operaciones de matrices\n")


def verificar_tipo_operando(operando):
    # Verificamos si el operando es una lista de listas (matriz)
    if isinstance(operando, list) and all(isinstance(row, list) for row in operando):
        # Verificamos si todas las filas tienen la misma longitud para asegurar que la matriz sea cuadrada
        if all(len(row) == len(operando[0]) for row in operando):
            return "matriz"
    # Verificamos si el operando es una lista (vector)
    elif isinstance(operando, list):
        return "vector"
    # Si no es ni matriz ni vector, entonces es un escalar
    return "escalar"


def main():
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = CalculadoraService.Client(protocol)

    transport.open()
    
    resultado = None  # Inicializamos resultado nulo
    
    def signal_handler(sig, frame):
        print('\n\nCliente detenido.')
        transport.close()
        sys.exit(0)

    # Establecer el manejador de señal para manejar SIGINT (Ctrl+C)
    signal.signal(signal.SIGINT, signal_handler)
    
    modo_vectorial = False

    while True:
        if not modo_vectorial:
            expresion = obtener_expresion()
        else:
            expresion = obtener_expresion_vectorial()

        if expresion == 'v':
            modo_vectorial = True
            continue
        elif expresion == 'b':
            modo_vectorial = False
            continue
        
        if not modo_vectorial:
            try:
                if len(expresion) == 3:
                    operando1, operador, operando2 = expresion
                    if operador == "+":
                        resultado = client.sumar(operando1, operando2)
                    elif operador == "-":
                        resultado = client.restar(operando1, operando2)
                    elif operador == "*":
                        resultado = client.multiplicar(operando1, operando2)
                    elif operador == "/":
                        resultado = client.dividir(operando1, operando2)
                    print(f"\nResultado de {operando1} {operador} {operando2} = {round(resultado, 2)}")
                elif len(expresion) == 2:
                    operador, operando = expresion
                    if operador.lower() == "sen":
                        resultado = client.seno(float(operando))
                    elif operador.lower() == "cos":
                        resultado = client.coseno(float(operando))
                    elif operador.lower() == "tan":
                        resultado = client.tangente(float(operando))
                    elif operador.lower() == "grad->rad":
                        resultado = client.gradosARadianes(float(operando))
                    elif operador.lower() == "rad->grad":
                        resultado = client.radianesAGrados(float(operando))
                    print(f"\nResultado de {operador}({operando}) = {round(resultado, 2)}")
            except Exception as e:
                print(f"Error: {e}")
        else:
            try:
                if len(expresion) == 3:
                    operando1, operador, operando2 = expresion
                    tipo_operando1 = verificar_tipo_operando(operando1)
                    tipo_operando2 = verificar_tipo_operando(operando2)    
                    if operador == "+":
                        if tipo_operando1 == "matriz" and tipo_operando2 == "matriz":
                            resultado = client.suma_matrices(operando1, operando2)
                        elif tipo_operando1 == "vector" or tipo_operando2 == "vector":
                            resultado = client.suma_vectores(operando1, operando2)
                    elif operador == "-":
                        if tipo_operando1 == "matriz" and tipo_operando2 == "matriz":
                            resultado = client.resta_matrices(operando1, operando2)
                        elif tipo_operando1 == "vector" or tipo_operando2 == "vector":
                            resultado = client.resta_vectores(operando1, operando2)
                    elif operador == "*":
                        if tipo_operando1 == "matriz" and tipo_operando2 == "matriz":
                            resultado = client.producto_matricial(operando1, operando2)
                        elif tipo_operando1 == "vector" or tipo_operando2 == "vector":
                            resultado = client.producto_escalar(operando1, operando2)
                    elif operador == "x":
                        resultado = client.producto_vectorial(operando1, operando2)
                    print(f"\nResultado de {operando1} {operador} {operando2} = {resultado}")
                elif len(expresion) == 2:
                    operador, matriz = expresion
                    if operador == "tras":
                        resultado = client.transpuesta(matriz)
                    elif operador == "det":
                        resultado = round(client.determinante(matriz), 2)
                    print(f"\nResultado de {operador}({matriz}) = {resultado}")
            except Exception as e:
                print(f"Error: {e}")

        continuar = input("\n¿Desea realizar otra operación? (s/n): ").lower()
        if continuar != 's':
            print('\n\nCliente detenido.')
            break

        print("\n")       # Añadimos dos linea en blanco entre ejecuciones     
        
    transport.close()

if __name__ == "__main__":
    main()
