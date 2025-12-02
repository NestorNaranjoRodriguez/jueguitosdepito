import random
import time

def juego_pares_y_nones():
    """
    Juego de Pares y Nones con dados.
    El usuario elige si juega con pares o impares.
    """
    print("🎲✨ JUEGO: PARES Y NONES ✨🎲")
    print("-" * 30)

    # Bucle que pide al usuario elegir bando hasta que dé una respuesta válida.
    while True:
        eleccion = input("¿Quieres jugar como Pares (P) o como Impares (I)?: ").strip().upper()
        if eleccion == 'P':
            jugador_humano_bando = 'Pares'
            jugador_maquina_bando = 'Impares'
            break
        elif eleccion == 'I':
            jugador_humano_bando = 'Impares'
            jugador_maquina_bando = 'Pares'
            break
        else:
            print("❌ Opción no válida. Debes escribir 'P' o 'I'.")

    print("")
    print("Has elegido jugar como:", jugador_humano_bando)
    print("La máquina jugará como:", jugador_maquina_bando)

    # Pedimos el número de dados y usamos try/except para detectar errores de entrada.
    while True:
        try:
            dados = int(input("\n¿Cuántos dados quieres lanzar (ej. 5)?: "))
            if dados > 0:
                break
            else:
                print("❌ Debes ingresar un número mayor que cero.")
        except ValueError:
            print("❌ Entrada inválida. Escribe un número entero.")

    # Contadores para los puntos acumulados durante los lanzamientos.
    puntos_humano = 0
    puntos_maquina = 0

    print("\n🔥 Preparando el lanzamiento de " + str(dados) + " dados...")
    time.sleep(1.5)

    print("\n--- ¡LANZAMIENTO! ---\n")

    # Recorremos un bucle que simula cada lanzamiento de dado usando randint.
    for i in range(1, dados + 1):
        tiro = random.randint(1, 6)  # simulamos un dado real
        es_par = (tiro % 2 == 0)
        resultado_str = "PAR" if es_par else "IMPAR"

        print("✨ Dado", i, ": ", tiro, " (", resultado_str, ")", sep="")

        # Usamos una condición para decidir si el punto lo gana el jugador o la máquina.
        if (es_par and jugador_humano_bando == 'Pares') or (not es_par and jugador_humano_bando == 'Impares'):
            puntos_humano += 1
            print("   --> ¡Punto para ti! 🎉")
        else:
            puntos_maquina += 1
            print("   --> Punto para la máquina. 🤖")

        time.sleep(0.5)

    # Mostramos el resumen general tras todos los lanzamientos del bucle.
    print("\n" + "=" * 40)
    print("🏆 RESULTADOS FINALES 🏆")
    print("=" * 40)
    print("Tu puntuación (" + jugador_humano_bando + "):", puntos_humano)
    print("Puntuación de la máquina (" + jugador_maquina_bando + "):", puntos_maquina)
    print("-" * 40)

    # Determinamos quién gana comparando los dos contadores acumulados.
    if puntos_humano > puntos_maquina:
        print("🥇🥳 ¡FELICIDADES! HAS GANADO LA PARTIDA. 🥳🥇")
    elif puntos_maquina > puntos_humano:
        print("😔 ¡Oh no! La máquina gana. ¡Intenta de nuevo! 🤖")
    else:
        print("🤝 ¡EMPATE! Ha sido una partida muy disputada. 🤝")

    print("\n" + "=" * 40)

if __name__ == "__main__":
    juego_pares_y_nones()
