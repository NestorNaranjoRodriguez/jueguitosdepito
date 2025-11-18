import random

print("🌟 ¡Bienvenido a Piedra, Papel, Tijera, Lagarto, Spock!")
print("="*60)
print("REGLAS:")
print("• Piedra aplasta Tijera y Lagarto")
print("• Papel cubre Piedra y desautoriza Spock")
print("• Tijera corta Papel y decapita Lagarto")
print("• Lagarto envenena Spock y come Papel")
print("• Spock rompe Tijera y vaporiza Piedra")
print("="*60)

# Contadores
victorias_jugador = 0
victorias_computadora = 0
empates = 0

while True:
    # El jugador elige
    while True:
        eleccion = input("Elige: piedra, papel, tijera, lagarto o spock → ").strip().lower()
        if eleccion == "piedra" or eleccion == "papel" or eleccion == "tijera" or eleccion == "lagarto" or eleccion == "spock":
            break
        else:
            print("❌ Opción inválida. Inténtalo de nuevo.")

    # La computadora elige
    opciones = ["piedra", "papel", "tijera", "lagarto", "spock"]
    idx = random.randint(0, 4)
    computadora = opciones[idx]

    print(f"\n🧑 Tú: {eleccion.capitalize()}")
    print(f"🤖 IA: {computadora.capitalize()}")

    # Determinar resultado con if/elif/else
    if eleccion == computadora:
        print("🤝 ¡Empate!")
        empates = empates + 1

    elif eleccion == "piedra":
        if computadora == "tijera":
            print("🎉 ¡Ganaste! → Piedra aplasta Tijera")
            victorias_jugador = victorias_jugador + 1
        elif computadora == "lagarto":
            print("🎉 ¡Ganaste! → Piedra aplasta Lagarto")
            victorias_jugador = victorias_jugador + 1
        elif computadora == "papel":
            print("💔 Perdiste → Papel cubre Piedra")
            victorias_computadora = victorias_computadora + 1
        else:
            print("💔 Perdiste → Spock vaporiza Piedra")
            victorias_computadora = victorias_computadora + 1

    elif eleccion == "papel":
        if computadora == "piedra":
            print("🎉 ¡Ganaste! → Papel cubre Piedra")
            victorias_jugador = victorias_jugador + 1
        elif computadora == "spock":
            print("🎉 ¡Ganaste! → Papel desautoriza a Spock")
            victorias_jugador = victorias_jugador + 1
        elif computadora == "tijera":
            print("💔 Perdiste → Tijera corta Papel")
            victorias_computadora = victorias_computadora + 1
        else:
            print("💔 Perdiste → Lagarto come Papel")
            victorias_computadora = victorias_computadora + 1

    elif eleccion == "tijera":
        if computadora == "papel":
            print("🎉 ¡Ganaste! → Tijera corta Papel")
            victorias_jugador = victorias_jugador + 1
        elif computadora == "lagarto":
            print("🎉 ¡Ganaste! → Tijera decapita Lagarto")
            victorias_jugador = victorias_jugador + 1
        elif computadora == "piedra":
            print("💔 Perdiste → Piedra aplasta Tijera")
            victorias_computadora = victorias_computadora + 1
        else:
            print("💔 Perdiste → Spock rompe Tijera")
            victorias_computadora = victorias_computadora + 1

    elif eleccion == "lagarto":
        if computadora == "spock":
            print("🎉 ¡Ganaste! → Lagarto envenena a Spock")
            victorias_jugador = victorias_jugador + 1
        elif computadora == "papel":
            print("🎉 ¡Ganaste! → Lagarto come Papel")
            victorias_jugador = victorias_jugador + 1
        elif computadora == "piedra":
            print("💔 Perdiste → Piedra aplasta Lagarto")
            victorias_computadora = victorias_computadora + 1
        else:
            print("💔 Perdiste → Tijera decapita Lagarto")
            victorias_computadora = victorias_computadora + 1

    elif eleccion == "spock":
        if computadora == "tijera":
            print("🎉 ¡Ganaste! → Spock rompe Tijera")
            victorias_jugador = victorias_jugador + 1
        elif computadora == "piedra":
            print("🎉 ¡Ganaste! → Spock vaporiza Piedra")
            victorias_jugador = victorias_jugador + 1
        elif computadora == "papel":
            print("💔 Perdiste → Papel desautoriza a Spock")
            victorias_computadora = victorias_computadora + 1
        else:
            print("💔 Perdiste → Lagarto envenena a Spock")
            victorias_computadora = victorias_computadora + 1

    total = victorias_jugador + victorias_computadora + empates
    print(f"\n📊 Marcador actual: Tú {victorias_jugador} - {victorias_computadora} IA (Empates: {empates})")

    while True:
        accion = input("\n¿Qué quieres hacer? (s = seguir, n/fin = salir, resumen = ver estadísticas) → ").strip().lower()
        if accion == "s" or accion == "si" or accion == "y" or accion == "yes":
            break
        elif accion == "n" or accion == "no" or accion == "fin" or accion == "salir":
            # Salir del juego
            print("\nCloseOperation iniciada...")
            break
        elif accion == "resumen":
            # Mostrar resumen detallado y seguir jugando
            print("\n" + "📈 RESUMEN DETALLADO".center(50))
            print("-"*50)
            print(f"Partidas jugadas: {total}")
            print(f"Tú ganaste:      {victorias_jugador}")
            print(f"IA ganó:         {victorias_computadora}")
            print(f"Empates:         {empates}")
            if total > 0:
                porc_j = (victorias_jugador * 100) // total
                porc_c = (victorias_computadora * 100) // total
                porc_e = (empates * 100) // total
                print(f"\nPorcentajes (aprox.):")
                print(f"  Tú:      {porc_j}%")
                print(f"  IA:      {porc_c}%")
                print(f"  Empate:  {porc_e}%")
            print("-"*50)
        else:
            print("⚠️ Por favor, escribe 's', 'n', 'fin' o 'resumen'.")

    if accion == "n" or accion == "no" or accion == "fin" or accion == "salir":
        break

# RESUMEN FINAL
print("\n" + "🏆 RESUMEN FINAL 🏆".center(50))
print("-"*50)
total = victorias_jugador + victorias_computadora + empates
print(f"Partidas jugadas: {total}")
print(f"Tú ganaste:      {victorias_jugador}")
print(f"IA ganó:         {victorias_computadora}")
print(f"Empates:         {empates}")

if total > 0:
    # Porcentajes con decimales
    porc_j = (victorias_jugador / total) * 100
    porc_c = (victorias_computadora / total) * 100
    porc_e = (empates / total) * 100
    # Mostrar con un decimal
    print(f"\nPorcentajes:")
    print(f"  Tú:      {int(porc_j * 10) / 10}%")
    print(f"  IA:      {int(porc_c * 10) / 10}%")
    print(f"  Empate:  {int(porc_e * 10) / 10}%")

    if victorias_jugador > victorias_computadora:
        print("\n✨ ¡Ganaste el duelo global!")
    elif victorias_computadora > victorias_jugador:
        print("\n🤖 La IA domina… pero ¡puedes vencerla en la revancha!")
    else:
        print("\n⚖️  ¡Equilibrio perfecto! Ni el caos ni el orden prevalecen.")
else:
    print("\nNo se jugó ninguna partida. ¡Hasta la próxima!")

print("\n🚀 ¡Gracias por jugar! Que la lógica esté contigo.")