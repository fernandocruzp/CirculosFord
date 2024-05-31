def CalculaPrecEf(entrada, n):
    """
    Calcula el término n-ésimo de una fracción continua de forma eficiente usando programación dinámica. (Lineal)
    
    Args:
    entrada (list): Lista que contiene los coeficientes de la fracción continua.
    n (int): Índice del término a calcular.
    
    Returns:
    int: El valor del término n-ésimo.
    """
    return CalculaPrecEf_2(entrada, n - 1)

diccionario = {}

def CalculaPrecEf_2(entrada, n):
    """
    Función auxiliar para CalculaPrecEf. (Lineal)
    
    Args:
    entrada (list): Lista que contiene los coeficientes de la fracción continua.
    n (int): Índice del término a calcular.
    
    Returns:
    int: El valor del término n-ésimo.
    """
    pn = diccionario.get(n)
    if pn is not None:
        return pn
    if n == 0:
        pn = entrada[0]
        diccionario[0] = pn
        return pn
    if n == 1:
        pn = entrada[1] * CalculaPrecEf_2(entrada, 0) + 1
        diccionario[1] = pn
        return pn
    pn = entrada[n] * CalculaPrecEf_2(entrada, n - 1) + CalculaPrecEf_2(entrada, n - 2)
    diccionario[n] = pn
    return pn

diccionario2 = {}

def CalculaQrecEf(entrada, n):
    """
    Calcula el término n-ésimo del denominador de una fracción continua de forma eficiente usando programación dinámica. (Lineal)
    
    Args:
    entrada (list): Lista que contiene los coeficientes de la fracción continua.
    n (int): Índice del término a calcular.
    
    Returns:
    int: El valor del término n-ésimo.
    """
    return CalculaQrecEf_2(entrada, n - 1)

def CalculaQrecEf_2(entrada, n):
    """
    Función auxiliar para CalculaQrecEf. (Lineal)
    
    Args:
    entrada (list): Lista que contiene los coeficientes de la fracción continua.
    n (int): Índice del término a calcular.
    
    Returns:
    int: El valor del término n-ésimo.
    """
    qn = diccionario2.get(n)
    if qn is not None:
        return qn
    if n == 0:
        qn = entrada[0]
        diccionario2[0] = qn
        return qn
    if n == 1:
        qn = entrada[1] * CalculaQrecEf_2(entrada, 0)
        diccionario2[1] = qn
        return qn
    qn = entrada[n] * CalculaQrecEf_2(entrada, n - 1) + CalculaQrecEf_2(entrada, n - 2)
    diccionario2[n] = qn
    return qn

def CalcularCoeficienteR(entrada, n):
    """
    Calcula el coeficiente R de una fracción continua dada una posición. (Lineal)
    
    Args:
    entrada (list): Lista que contiene los coeficientes de la fracción continua.
    n (int): Índice del término a calcular.
    Returns:
    Convergente (list): Lista cuyo primer elemento es el numerador y el segundo el denominador
    """
    return [CalculaPrecEf(entrada, n),CalculaQrecEf(entrada, n)]

