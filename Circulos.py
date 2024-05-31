# Importar funciones del archivo frac_continua.py
from Convergentes import CalcularCoeficienteR
import matplotlib.pyplot as plt

def obtener_lista():
    """
    Solicita al usuario una lista de coeficientes de la fracción continua.
    """
    while True:
        try:
            entrada = input("Ingrese una lista de coeficientes separados por comas: ")
            lista = [int(x) for x in entrada.split(',')]
            if len(lista) < 2:
                raise ValueError("La lista debe contener al menos dos coeficientes.")
            return lista
        except ValueError as e:
            print(f"Entrada inválida: {e}. Intente nuevamente.")

def obtener_numero_convergentes():
    """
    Solicita al usuario el número de convergentes que desea calcular.
    """
    try:
        n = int(input("Ingrese el número de convergentes a calcular: "))
        if n < 1:
            raise ValueError("El número de convergentes debe ser al menos 1.")
        return n
    except ValueError as e:
        print(f"Entrada inválida: {e}. Intente nuevamente.")
def obtenerDatosCirculo(convergente):
    x=convergente[0]/convergente[1]
    y=1/(2*convergente[1]*convergente[1])
    return x, y, y

def dibujaCirculosFord(circulos):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # Dibujar los círculos
    for (x, y, r) in circulos:
        circulo = plt.Circle((x, y), r, fill=False)
        ax.add_artist(circulo)

    # Configurar límites del gráfico
    ax.set_xlim(circulos[0][0]-circulos[0][2],circulos[1][0]+circulos[1][2] )
    ax.set_ylim(0, circulos[0][1]+circulos[0][2])
        
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Circulos de Ford')
    plt.grid(True)
    plt.show()

def main():
    # Obtener la lista de coeficientes y el número de convergentes del usuario
    lista_coeficientes = obtener_lista()
    num_convergentes = obtener_numero_convergentes()
    
    # Calcular los convergentes y guardarlos en una lista
    convergentes = []
    circulos=[]
    for i in range(1, num_convergentes+1):
        convergente = CalcularCoeficienteR(lista_coeficientes, i)
        convergentes.append(convergente)
        circulos.append(obtenerDatosCirculo(convergente))
    
    # Mostrar los convergentes calculados
    print("Convergentes calculados:")
    for i, conv in enumerate(convergentes, start=1):
        print(f"Convergente {i}: Numerador = {conv[0]}, Denominador = {conv[1]}")

    dibujaCirculosFord(circulos)

if __name__ == "__main__":
    main()

