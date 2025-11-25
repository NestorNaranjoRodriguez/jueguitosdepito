import tkinter as tk
import random

# Configuración inicial
WIDTH = 600
HEIGHT = 400
BLOCK_SIZE = 20
SPEED = 150

# Colores mejorados
DARK_GREEN = "#006400"   # Fondo más oscuro para simular césped
SNAKE_HEAD = "#32CD32"   # Verde lima para la cabeza
SNAKE_BODY = "#228B22"   # Verde bosque para el cuerpo
APPLE_RED = "#DC143C"    # Rojo carmesí para la manzana
APPLE_STEM = "#8B4513"   # Marrón para el tallo
APPLE_LEAF = "#228B22"   # Verde para la hoja
WHITE = "#FFFFFF"
BLACK = "#000000"
SCORE_COLOR = "#FFD700"  # Dorado para el puntaje

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=DARK_GREEN)
        self.canvas.pack()
        
        # La serpiente empezará en el centro
        self.snake = [(WIDTH // 2, HEIGHT // 2)]
        # Dirección actual (usada para moverse)
        self.direction = (0, -BLOCK_SIZE)  # Inicia hacia arriba
        # Dirección pendiente (solicitada por teclas, se valida antes de mover)
        self.pending_direction = (0, -BLOCK_SIZE)
        
        # Manzana
        self.food = self.random_manzana()
        
        # Puntuación
        self.score = 0
        
        # Estado del juego
        self.game_over = False
        
        # Dibujar elementos iniciales
        self.draw()
        
        # Controles con las flechas
        self.root.bind("<Up>", lambda e: self.change_direction((0, -BLOCK_SIZE)))
        self.root.bind("<Down>", lambda e: self.change_direction((0, BLOCK_SIZE)))
        self.root.bind("<Left>", lambda e: self.change_direction((-BLOCK_SIZE, 0)))
        self.root.bind("<Right>", lambda e: self.change_direction((BLOCK_SIZE, 0)))
        self.root.bind("<space>", self.restart)  # Reiniciar con Espacio
        
        # Iniciar loop del juego
        self.update()
    
    def random_manzana(self):
        x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        return (x, y)
    
    def change_direction(self, new_dir):
        if not self.game_over:
            # Solo almacenamos la solicitud; la validación ocurre en move_snake()
            self.pending_direction = new_dir
    
    def move_snake(self):
        if self.game_over:
            return
        
        # Aplicar dirección pendiente solo si NO es opuesta a la dirección actual (evita 180°)
        pending = self.pending_direction
        current = self.direction
        if not (pending[0] == -current[0] and pending[1] == -current[1]):
            self.direction = pending
        
        # Calcular nueva cabeza con la dirección segura
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        
        # Verificar colisión con bordes
        if (new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT):
            self.game_over = True
            return
        
        # Verificar colisión con el cuerpo
        if new_head in self.snake:
            self.game_over = True
            return
        
        # Agregar nueva cabeza
        self.snake.insert(0, new_head)
        
        # Verificar si come manzana
        if new_head == self.food:
            self.score += 1
            # Evitar que la nueva manzana aparezca en la serpiente
            while self.food in self.snake:
                self.food = self.random_manzana()
        else:
            self.snake.pop()  # Quitar cola si no comió
    
    def draw(self):
        self.canvas.delete("all")
        
        # Dibujar serpiente
        for i, segment in enumerate(self.snake):
            if i == 0:  # Cabeza
                self.canvas.create_rectangle(
                    segment[0], segment[1],
                    segment[0] + BLOCK_SIZE, segment[1] + BLOCK_SIZE,
                    fill=SNAKE_HEAD, outline=BLACK, width=2
                )
                # Ojos
                eye_size = 4
                eye_offset = 4
                self.canvas.create_oval(
                    segment[0] + eye_offset, segment[1] + eye_offset,
                    segment[0] + eye_offset + eye_size, segment[1] + eye_offset + eye_size,
                    fill=BLACK
                )
                self.canvas.create_oval(
                    segment[0] + BLOCK_SIZE - eye_offset - eye_size, segment[1] + eye_offset,
                    segment[0] + BLOCK_SIZE - eye_offset, segment[1] + eye_offset + eye_size,
                    fill=BLACK
                )
                # Pupilas blancas
                pupil_size = 2
                self.canvas.create_oval(
                    segment[0] + eye_offset + 1, segment[1] + eye_offset + 1,
                    segment[0] + eye_offset + pupil_size, segment[1] + eye_offset + pupil_size,
                    fill=WHITE
                )
                self.canvas.create_oval(
                    segment[0] + BLOCK_SIZE - eye_offset - pupil_size, segment[1] + eye_offset + 1,
                    segment[0] + BLOCK_SIZE - eye_offset - 1, segment[1] + eye_offset + pupil_size,
                    fill=WHITE
                )
                # Boca
                mouth_y = segment[1] + BLOCK_SIZE - 5
                self.canvas.create_arc(
                    segment[0] + 5, mouth_y,
                    segment[0] + BLOCK_SIZE - 5, mouth_y + 5,
                    start=0, extent=180, fill=BLACK, outline=BLACK
                )
            else:  # Cuerpo
                self.canvas.create_rectangle(
                    segment[0], segment[1],
                    segment[0] + BLOCK_SIZE, segment[1] + BLOCK_SIZE,
                    fill=SNAKE_BODY, outline=BLACK, width=1
                )
        
        # Dibujar manzana mejorada
        apple_x, apple_y = self.food
        # Sombra
        self.canvas.create_oval(
            apple_x + 2, apple_y + 4,
            apple_x + BLOCK_SIZE + 2, apple_y + BLOCK_SIZE + 2,
            fill="#8B0000", outline=""
        )
        # Manzana
        self.canvas.create_oval(
            apple_x, apple_y,
            apple_x + BLOCK_SIZE, apple_y + BLOCK_SIZE,
            fill=APPLE_RED, outline=BLACK, width=1
        )
        # Tallo
        stem_height = 6
        self.canvas.create_rectangle(
            apple_x + BLOCK_SIZE // 2 - 1, apple_y - stem_height,
            apple_x + BLOCK_SIZE // 2 + 1, apple_y,
            fill=APPLE_STEM, outline=APPLE_STEM
        )
        # Hoja
        leaf_x = apple_x + BLOCK_SIZE // 2 + 2
        leaf_y = apple_y - stem_height
        self.canvas.create_oval(
            leaf_x, leaf_y, leaf_x + 6, leaf_y + 4,
            fill=APPLE_LEAF, outline=BLACK, width=1
        )
        
        # Puntaje
        score_text = f"Puntaje: {self.score}"
        self.canvas.create_text(52, 22, text=score_text, fill=BLACK, font=("Arial", 16, "bold"))
        self.canvas.create_text(50, 20, text=score_text, fill=SCORE_COLOR, font=("Arial", 16, "bold"))
        
        # Game Over
        if self.game_over:
            self.canvas.create_text(WIDTH // 2 + 2, HEIGHT // 2 + 2, text="Game Over", fill=BLACK, font=("Arial", 28, "bold"))
            self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over", fill=WHITE, font=("Arial", 28, "bold"))
            self.canvas.create_text(WIDTH // 2 + 1, HEIGHT // 2 + 32, text="Presiona Espacio para reiniciar", fill=BLACK, font=("Arial", 14))
            self.canvas.create_text(WIDTH // 2, HEIGHT // 2 + 30, text="Presiona Espacio para reiniciar", fill=WHITE, font=("Arial", 14))
    
    def update(self):
        self.move_snake()
        self.draw()
        if not self.game_over:
            self.root.after(SPEED, self.update)
    
    def restart(self, event=None):
        self.snake = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (0, -BLOCK_SIZE)
        self.pending_direction = (0, -BLOCK_SIZE)
        self.food = self.random_manzana()
        self.score = 0
        self.game_over = False
        self.update()

# Ejecuta el juego
if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()