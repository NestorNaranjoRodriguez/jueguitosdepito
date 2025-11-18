import os
import random
import sys

# Pedir número de barajas
while True:
    try:
        barajas = int(input("Ingrese el número de barajas a usar: "))
        if barajas < 1:
            print("Por favor, ingrese un número mayor que 0.")
            continue
        break
    except ValueError:
        print("Ingrese un número válido.")

# Inicializar baraja
baraja = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * (barajas * 4)

# Contadores
victorias = 0
derrotas = 0
empates = 0


def repartir(baraja):
    mano = []
    for _ in range(2):
        random.shuffle(baraja)
        carta = baraja.pop()
        if carta == 11: carta = "J"
        elif carta == 12: carta = "Q"
        elif carta == 13: carta = "K"
        elif carta == 14: carta = "A"
        mano.append(carta)
    return mano


def jugar_de_nuevo():
    otra = input("¿Quieres jugar otra vez? (S/N): ").lower()
    if otra == "s":
        global baraja
        if len(baraja) < 10:
            baraja = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * (barajas * 4)
        juego()
    else:
        print("¡Hasta luego!")
        sys.exit()


def total(mano):
    t = 0
    ases = 0
    for carta in mano:
        if carta in ("J", "Q", "K"):
            t += 10
        elif carta == "A":
            ases += 1
        else:
            t += carta
    for _ in range(ases):
        if t + 11 > 21:
            t += 1
        else:
            t += 11
    return t


def pedir_carta(mano):
    carta = baraja.pop()
    if carta == 11: carta = "J"
    elif carta == 12: carta = "Q"
    elif carta == 13: carta = "K"
    elif carta == 14: carta = "A"
    mano.append(carta)
    return mano


def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_resultados(mano_crupier, mano_jugador):
    limpiar()
    print("\n    🃏 BIENVENIDO AL BLACKJACK 🃏\n")
    print("-" * 40)

    # Colores ANSI: verde, rojo, azul
    print(f"\033[1;32mVICTORIAS: {victorias}\033[0m   "
          f"\033[1;31mDERROTAS: {derrotas}\033[0m   "
          f"\033[1;34mEMPATES: {empates}\033[0m")

    print("-" * 40 + "\n")
    print(f"El crupier tiene: {mano_crupier} (total: {total(mano_crupier)})")
    print(f"Tú tienes: {mano_jugador} (total: {total(mano_jugador)})\n")


def comprobar_blackjack(mano_crupier, mano_jugador):
    global victorias, derrotas, empates

    total_jugador = total(mano_jugador)
    total_crupier = total(mano_crupier)

    if total_jugador == 21 and total_crupier != 21:
        mostrar_resultados(mano_crupier, mano_jugador)
        print("🎉 ¡Felicidades! ¡Tienes un Blackjack!\n")
        victorias += 1
        jugar_de_nuevo()
    elif total_crupier == 21 and total_jugador != 21:
        mostrar_resultados(mano_crupier, mano_jugador)
        print("😞 El crupier tiene Blackjack. Has perdido.\n")
        derrotas += 1
        jugar_de_nuevo()
    elif total_jugador == total_crupier == 21:
        mostrar_resultados(mano_crupier, mano_jugador)
        print("🤝 ¡Ambos tienen Blackjack! Es un empate.\n")
        empates += 1
        jugar_de_nuevo()


def puntuar(mano_crupier, mano_jugador):
    global victorias, derrotas, empates

    total_jugador = total(mano_jugador)
    total_crupier = total(mano_crupier)

    mostrar_resultados(mano_crupier, mano_jugador)

    if total_jugador > 21:
        print("😞 Te pasaste de 21. Pierdes.\n")
        derrotas += 1
    elif total_crupier > 21:
        print("🎉 El crupier se pasó de 21. ¡Ganas!\n")
        victorias += 1
    elif total_jugador > total_crupier:
        print("🎉 Tu puntuación es mayor. ¡Ganas!\n")
        victorias += 1
    elif total_jugador < total_crupier:
        print("😞 El crupier gana.\n")
        derrotas += 1
    else:
        print("🤝 Es un empate.\n")
        empates += 1


def juego():
    global victorias, derrotas, empates

    limpiar()
    print("\n    🃏 BIENVENIDO AL BLACKJACK 🃏\n")
    print("-" * 40)
    print(f"\033[1;32mVICTORIAS: {victorias}\033[0m   "
          f"\033[1;31mDERROTAS: {derrotas}\033[0m   "
          f"\033[1;34mEMPATES: {empates}\033[0m")
    print("-" * 40 + "\n")

    mano_crupier = repartir(baraja)
    mano_jugador = repartir(baraja)

    print(f"El crupier muestra: {mano_crupier[0]}")
    print(f"Tus cartas: {mano_jugador} (total: {total(mano_jugador)})")

    comprobar_blackjack(mano_crupier, mano_jugador)

    while True:
        eleccion = input("¿Quieres [P]edir, [Q]uedarte o [S]alir?: ").lower()
        if eleccion == "p":
            pedir_carta(mano_jugador)
            print(f"Tus cartas: {mano_jugador} (total: {total(mano_jugador)})")
            if total(mano_jugador) > 21:
                print("😞 Te pasaste de 21.")
                derrotas += 1
                jugar_de_nuevo()
        elif eleccion == "q":
            while total(mano_crupier) < 17:
                pedir_carta(mano_crupier)
            puntuar(mano_crupier, mano_jugador)
            jugar_de_nuevo()
        elif eleccion == "s":
            print("¡Hasta luego!")
            sys.exit()
        else:
            print("Opción inválida. Usa P, Q o S.")


if __name__ == "__main__":
    juego()
