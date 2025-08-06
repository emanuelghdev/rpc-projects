import glob
import sys
import math
import signal
import sys
import numpy as np

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from calculadora import CalculadoraService
from calculadora.ttypes import Operacion
from calculadora.ttypes import DivisionPorCeroException, MatrizNoCuadradaException

class CalculadoraHandler:
    def sumar(self, operando1, operando2):
        return operando1 + operando2

    def restar(self, operando1, operando2):
        return operando1 - operando2

    def multiplicar(self, operando1, operando2):
        return operando1 * operando2

    def dividir(self, operando1, operando2):
        # Verificamos que el divisor no sea 0
        if operando2 == 0:
            raise DivisionPorCeroException("No se puede dividir por cero")
        return operando1 / operando2

    def seno(self, angulo):
        return math.sin(math.radians(angulo))

    def coseno(self, angulo):
        return math.cos(math.radians(angulo))

    def tangente(self, angulo):
        return math.tan(math.radians(angulo))

    def gradosARadianes(self, grados):
        return math.radians(grados)

    def radianesAGrados(self, radianes):
        return math.degrees(radianes)

    def suma_vectores(self, vector1, vector2):
        return np.add(vector1, vector2)

    def resta_vectores(self, vector1, vector2):
        return np.subtract(vector1, vector2)

    def producto_escalar(self, vector1, vector2):
        return np.dot(vector1, vector2)

    def producto_vectorial(self, vector1, vector2):
        return np.cross(vector1, vector2)

    def suma_matrices(self, matriz1, matriz2):
        return np.add(matriz1, matriz2)

    def resta_matrices(self, matriz1, matriz2):
        return np.subtract(matriz1, matriz2)

    def producto_matricial(self, matriz1, matriz2):
        return np.matmul(matriz1, matriz2)

    def transpuesta(self, matriz):
        return np.transpose(matriz)
            
    def determinante(self, matriz):
        # Verificamos si la matriz es cuadrada
        if len(matriz) != len(matriz[0]):
            raise MatrizNoCuadradaException("La matriz no es cuadrada, no se puede calcular el determinante.")
        return np.linalg.det(matriz)

def signal_handler(sig, frame):
    print('\n\nServidor detenido.')
    sys.exit(0)

if __name__ == '__main__':
    handler = CalculadoraHandler()
    processor = CalculadoraService.Processor(handler)
    transport = TSocket.TServerSocket(host='localhost', port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print("Iniciando servidor...")
    
    # Establecer el manejador de señal para manejar SIGINT (Ctrl+C)
    signal.signal(signal.SIGINT, signal_handler)
    
    server.serve()
