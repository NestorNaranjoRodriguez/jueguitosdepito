import random

def juego_pares_y_nones():
    print("\n🎲 JUEGO: PARES Y NONES 🎲")

    # Pedir número de dados
    dados = int(input("¿Cuántos dados quieres lanzar?: "))

    puntos_j1 = 0
    puntos_j2 = 0

    print("\nLanzando dados...\n")

    for i in range(dados):
        tiro = random.randint(1, 6)
        print(f"Dado {i+1}: {tiro}")

        if tiro % 2 == 0:
            puntos_j1 += 1
        else:
            puntos_j2 += 1

    print("\n--- RESULTADOS ---")
    print(f"Jugador 1 (pares): {puntos_j1} puntos")
    print(f"Jugador 2 (impares): {puntos_j2} puntos")

    # Determinar ganador
    if puntos_j1 > puntos_j2:
        print("🏆 ¡Gana el Jugador 1!")
    elif puntos_j2 > puntos_j1:
        print("🏆 ¡Gana el Jugador 2!")
    else:
        print("🤝 ¡Empate!")
    
    input("\nPulsa ENTER para volver al menú...")