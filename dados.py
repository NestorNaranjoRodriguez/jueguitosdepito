import random

def juego_pares_y_nones():
    print("\nJUEGO: PARES Y NONES")

    dados = int(input("¿Cuántos dados quieres lanzar?: "))

    puntos_j1 = 0
    puntos_j2 = 0

    print("\nLanzando dados...\n")

    contador = 1
    while contador <= dados:
        tiro = random.randint(1, 6)
        print("Dado " + str(contador) + ": " + str(tiro))

        if tiro % 2 == 0:
            puntos_j1 += 1
        else:
            puntos_j2 += 1

        contador += 1

    print("\n--- RESULTADOS ---")
    print("Jugador 1 (pares): " + str(puntos_j1) + " puntos")
    print("Jugador 2 (impares): " + str(puntos_j2) + " puntos")

    if puntos_j1 > puntos_j2:
        print("Gana el Jugador 1")
    elif puntos_j2 > puntos_j1:
        print("Gana el Jugador 2")
    else:
        print("Empate")

if __name__ == "__main__":
    juego_pares_y_nones()
