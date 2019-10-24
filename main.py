# Author: Mariana Perez
# D compiler
# Can be run using the following command: python main.py

import calc as calc

if __name__ == "__main__":
    import sys

    # -------------------------------------------------------
    #                       PASSING TESTS
    # -------------------------------------------------------
    print("--------Valid Tests--------")
    # Test1: Un programa sencillo con un comentario de una palabra
    print("Test 1: Comentario de una palabra")
    f = open('./Tests/Test1.d', 'r')
    data = f.read()
    f.close()
    calc.process(data)

    #Test2: Un programa sencillo con un comentario de una linea
    print("Test 2: Comentario de una linea")
    f = open('./Tests/Test2.d', 'r')
    data = f.read()
    f.close()
    calc.process(data)

    # Test3: Un programa sencillo con la definicion de una variable.
    print("Test 3: Definicion de una variable")
    f = open('./Tests/Test3.d', 'r')
    data = f.read()
    f.close()
    calc.process(data)

    # Test4: Un programa sencillo con la definicion de una constante.
    print("Test 4: Definicion de una constante")
    f = open('./Tests/Test4.d', 'r')
    data = f.read()
    f.close()
    calc.process(data)

    # Test5: Un programa sencillo con cadenas.
    print("Test 5: Programa con cadenas")
    f = open('./Tests/Test5.d', 'r')
    data = f.read()
    f.close()
    calc.process(data)

    # Test6: Un programa sencillo con variables de todos los tipos de datos.
    print("Test 6: Todos los tipos de datos")
    f = open('./Tests/Test6.d', 'r')
    data = f.read()
    f.close()
    calc.process(data)

    # Test7: Un programa sencillo con un ciclo y una condicional.
    print("Test 7: ciclo y una condicional")
    f = open('./Tests/Test7.d', 'r')
    data = f.read()
    f.close()
    calc.process(data)

    # Test8: Un programa sencillo con un ciclo y una condicional anidada.
    print("Test 8: ciclo y una condicional anidados")
    f = open('./Tests/Test8.d', 'r')
    data = f.read()
    f.close()
    calc.process(data)

    # Test9: Un programa sencillo usando las instrucciones de entrada y salida.
    print("Test 9: Instrucciones de entrada y de salida")
    f = open('./Tests/Test9.d', 'r')
    data = f.read()
    f.close()
    calc.process(data)

    # Test10: Un programa sencillo con todas las instrucciones que has definido.
    print("Test 10: Todas las instrucciones definidas")
    f = open('./Tests/Test10.d', 'r')
    data = f.read()
    f.close()
    calc.process(data)

# -------------------------------------------------------
#                       FAILING TESTS
# -------------------------------------------------------

    # Test11 y 12: Un programa sencillo con la definicion de una variable en el lugar incorrecto y en el orden incorrecto.
    print("\n--------Invalid tests--------")
    print("Test 11: Variable en el lugar incorrecto")
    f = open('./Tests/Test11.d', 'r')
    data = f.read()
    f.close()
    calc.process(data)

    print("Test 12: Varible en el orden incorrecto.")
    f = open('./Tests/Test12.d', 'r')
    data = f.read()
    f.close()
    calc.process(data)

    # Test13: Un programa sencillo que utiliza una cadena, variable y constante en un lugar que no esta permitido.
    print("Test 13: Cadena en un lugar no permitido")
    f = open('./Tests/Test13.d', 'r')
    data = f.read()
    f.close()
    calc.process(data)

    # Test14: Un programa sencillo con un ciclo definido pero usando una gramatica incorrecta.
    print("Test 14: Ciclo definido pero usando gramatica incorrecta")
    f = open('./Tests/Test14.d', 'r')
    data = f.read()
    f.close()
    calc.process(data)

    print("Test 15: Constante en el lugar incorrecto")
    f = open('./Tests/Test15.d', 'r')
    data = f.read()
    f.close()
    calc.process(data)

    print("Test 16: Asignar el valor a una variable que no corresponde con su tipo.")
    f = open('./Tests/Test16.d', 'r')
    data = f.read()
    f.close()
    calc.process(data)

    print("Test 17: Usar una variable fuera de su alcance")
    f = open('./Tests/Test17.d', 'r')
    data = f.read()
    f.close()
    calc.process(data)
