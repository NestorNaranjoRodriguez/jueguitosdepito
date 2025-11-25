## 🎮 Descripción de los Juegos

- **Juego 1: 🎲 Pares y Nones 🎲(azar)**  
  Se lanzan varios dados.  
  - El **Jugador 1** gana puntos por cada dado **par**.  
  - El **Jugador 2** gana puntos por cada dado **impar**.  
  - El jugador con más puntos es el ganador.  

- **Juego 2:🪨 Piedra, 📄 Papel, ✂️ Tijera, 🦎 Lagarto, 🖖 Spock(lógica)**  
  Versión clásica entre dos jugadores (Himar y Antonio):  
  - **Piedra aplasta Tijera y Lagarto**  
  - **Papel cubre Piedra y desautoriza Spock**  
  - **Tijera corta Papel y decapita Lagarto**  
  - **Lagarto envenena Spock y come Papel**  
  - **Spock rompe Tijera y vaporiza Piedra**  
  Variante extendida: se añaden **Lagarto y Spock**, ampliando las combinaciones y reduciendo los empates.  

- **Juego 3: 🐍 Snake (gráfico con pygame)**  
  El jugador controla una serpiente que se mueve por la pantalla.  
  - Objetivo: **comer comida** para crecer.  
  - Pierde si choca contra los bordes o contra sí misma.  
  - Controles: Flechas ↑ ↓ ← →.  
  - Se muestra el puntaje y un mensaje de *Game Over* al perder.  

- **Juego 4: 🃏 Blackjack (estrategia y azar)**  
  Juego clásico de cartas contra el crupier.  
  - Objetivo: **acercarse a 21 puntos sin pasarse**.  
  - Valores de cartas:  
    - Números (2–10): su valor.  
    - J, Q, K: valen 10.  
    - As: vale 1 u 11 según convenga.  
  - Desarrollo:  
    - Se reparten dos cartas al jugador y dos al crupier (una visible, otra oculta).  
    - El jugador puede:  
      - **[P] Pedir carta** → recibe una carta adicional.  
      - **[Q] Quedarse** → mantiene su mano y pasa turno al crupier.  
      - **[S] Salir** → termina el juego.  
    - El crupier pide cartas hasta llegar a 17 o más.  
  - Condiciones especiales:  
    - **Blackjack natural (21 con dos cartas)** se comprueba al inicio.  
    - Si ambos tienen Blackjack → empate.  
    - Si solo uno lo tiene → gana automáticamente.  
  - Final de la ronda:  
    - Si el jugador se pasa de 21 → pierde.  
    - Si el crupier se pasa de 21 → gana el jugador.  
    - Si el jugador tiene más puntos → gana.  
    - Si el crupier tiene más puntos → gana el crupier.  
    - Si son iguales → empate.  
  - Se muestran los contadores de **victorias, derrotas y empates** en pantalla.  
  - Al terminar, se pregunta si el jugador quiere jugar otra vez; si la baraja se queda con pocas cartas, se reinicia automáticamente.  
