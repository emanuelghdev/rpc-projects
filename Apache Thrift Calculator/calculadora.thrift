namespace py calculadora

struct Operacion {
    1: double operando1,
    2: double operando2,
    3: string operador
}

exception DivisionPorCeroException {
    1: string mensaje
}

exception MatrizNoCuadradaException {
    1: string mensaje
}

service CalculadoraService {
    double sumar(1: double operando1, 2: double operando2),
    double restar(1: double operando1, 2: double operando2),
    double multiplicar(1: double operando1, 2: double operando2),
    double dividir(1: double operando1, 2: double operando2),
    double seno(1: double angulo),
    double coseno(1: double angulo),
    double tangente(1: double angulo),
    double gradosARadianes(1: double grados),
    double radianesAGrados(1: double radianes),
    list<double> suma_vectores(1: list<double> vector1, 2: list<double> vector2),
    list<double> resta_vectores(1: list<double> vector1, 2: list<double> vector2),
    double producto_escalar(1: list<double> vector1, 2: list<double> vector2),
    list<double> producto_vectorial(1: list<double> vector1, 2: list<double> vector2),
    list<list<double>> suma_matrices(1: list<list<double>> matriz1, 2: list<list<double>> matriz2),
    list<list<double>> resta_matrices(1: list<list<double>> matriz1, 2: list<list<double>> matriz2),
    list<list<double>> producto_matricial(1: list<list<double>> matriz1, 2: list<list<double>> matriz2),
    list<list<double>> transpuesta(1: list<list<double>> matriz),
    list<list<double>> inversa(1: list<list<double>> matriz),
    double determinante(1: list<list<double>> matriz)
}
