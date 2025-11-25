import tkinter as tk
import random

# Configuración inicial
WIDTH = 600
HEIGHT = 400
# Tamaño del bloque que representa la serpiente y la manzana
BLOCK_SIZE = 20
# Velocidad (Menor valor más rápido y fluido va)
SPEED = 150

# Colores mejorados para un aspecto más atractivo
DARK_GREEN = "#006400"  # Fondo más oscuro para simular césped
SNAKE_HEAD = "#32CD32"  # Verde lima para la cabeza
SNAKE_BODY = "#228B22"  # Verde bosque para el cuerpo
APPLE_RED = "#DC143C"   # Rojo carmesí para la manzana
APPLE_STEM = "#8B4513"  # Marrón para el tallo
APPLE_LEAF = "#228B22"  # Verde para la hoja
WHITE = "#FFFFFF"
BLACK = "#000000"
SCORE_COLOR = "#FFD700"  # Dorado para el puntaje

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game - Mejora Gráfica")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=DARK_GREEN)
        self.canvas.pack()
        
        # La serpiente empezará en el centro
        self.snake = [(WIDTH // 2, HEIGHT // 2)]
        # Se desplazará hacia arriba al inicio
        self.direction = (0, -BLOCK_SIZE)
        
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
            # Evitar reversa inmediata
            if (new_dir[0] * -1, new_dir[1] * -1) != self.direction:
                self.direction = new_dir
    
    def move_snake(self):
        if self.game_over:
            return
        
        # Calcula la nueva posición de la cabeza
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        
        # Verifica la colisión con bordes
        if (new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT):
            self.game_over = True
            return
        
        # Verificar la colisión con el cuerpo
        if new_head in self.snake:
            self.game_over = True
            return
        
        # Agrega nueva cabeza al comer
        self.snake.insert(0, new_head)
        
        # Verifica si come manzana
        if new_head == self.food:
            self.score += 1
            self.food = self.random_manzana()
        else:
            self.snake.pop()
    
    def draw(self):
        self.canvas.delete("all")
        
        # Dibujar serpiente con mejoras: cabeza con ojos más detallados y cuerpo con borde
        for i, segment in enumerate(self.snake):
            if i == 0:  # Cabeza con ojos y boca
                # Cabeza con borde negro
                self.canvas.create_rectangle(segment[0], segment[1], 
                                             segment[0] + BLOCK_SIZE, segment[1] + BLOCK_SIZE, 
                                             fill=SNAKE_HEAD, outline=BLACK, width=2)
                # Ojos más grandes y expresivos
                eye_size = 4
                eye_offset = 4
                self.canvas.create_oval(segment[0] + eye_offset, segment[1] + eye_offset,
                                        segment[0] + eye_offset + eye_size, segment[1] + eye_offset + eye_size,
                                        fill=BLACK)
                self.canvas.create_oval(segment[0] + BLOCK_SIZE - eye_offset - eye_size, segment[1] + eye_offset,
                                        segment[0] + BLOCK_SIZE - eye_offset, segment[1] + eye_offset + eye_size,
                                        fill=BLACK)
                # Pupilas blancas para realismo
                pupil_size = 2
                self.canvas.create_oval(segment[0] + eye_offset + 1, segment[1] + eye_offset + 1,
                                        segment[0] + eye_offset + pupil_size, segment[1] + eye_offset + pupil_size,
                                        fill=WHITE)
                self.canvas.create_oval(segment[0] + BLOCK_SIZE - eye_offset - pupil_size, segment[1] + eye_offset + 1,
                                        segment[0] + BLOCK_SIZE - eye_offset - 1, segment[1] + eye_offset + pupil_size,
                                        fill=WHITE)
                # Boca simple
                mouth_y = segment[1] + BLOCK_SIZE - 5
                self.canvas.create_arc(segment[0] + 5, mouth_y, segment[0] + BLOCK_SIZE - 5, mouth_y + 5,
                                       start=0, extent=180, fill=BLACK, outline=BLACK)
            else:
                # Cuerpo con borde para profundidad
                self.canvas.create_rectangle(segment[0], segment[1], 
                                             segment[0] + BLOCK_SIZE, segment[1] + BLOCK_SIZE, 
                                             fill=SNAKE_BODY, outline=BLACK, width=1)
        
        # Manzana mejorada: con tallo, hoja y sombreado
        apple_x, apple_y = self.food
        # Sombra para profundidad
        self.canvas.create_oval(apple_x + 2, apple_y + 4, 
                                apple_x + BLOCK_SIZE + 2, apple_y + BLOCK_SIZE + 2, 
                                fill="#8B0000", outline="")
        # Manzana principal
        self.canvas.create_oval(apple_x, apple_y, 
                                apple_x + BLOCK_SIZE, apple_y + BLOCK_SIZE, 
                                fill=APPLE_RED, outline=BLACK, width=1)
        # Tallo
        stem_height = 6
        self.canvas.create_rectangle(apple_x + BLOCK_SIZE // 2 - 1, apple_y - stem_height, 
                                     apple_x + BLOCK_SIZE // 2 + 1, apple_y, 
                                     fill=APPLE_STEM, outline=APPLE_STEM)
        # Hoja
        leaf_x = apple_x + BLOCK_SIZE // 2 + 2
        leaf_y = apple_y - stem_height
        self.canvas.create_oval(leaf_x, leaf_y, leaf_x + 6, leaf_y + 4, fill=APPLE_LEAF, outline=BLACK, width=1)
        
        # Puntaje con fuente mejorada y sombra
        score_text = f"Puntaje: {self.score}"
        self.canvas.create_text(52, 22, text=score_text, fill=BLACK, font=("Arial", 16, "bold"))  # Sombra
        self.canvas.create_text(50, 20, text=score_text, fill=SCORE_COLOR, font=("Arial", 16, "bold"))
        
        # Game Over con estilo mejorado
        if self.game_over:
            self.canvas.create_text(WIDTH // 2 + 2, HEIGHT // 2 + 2, text="Game Over", fill=BLACK, font=("Arial", 28, "bold"))  # Sombra
            self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over", fill=WHITE, font=("Arial", 28, "bold"))
            self.canvas.create_text(WIDTH // 2 + 1, HEIGHT // 2 + 32, text="Presiona Espacio para reiniciar", fill=BLACK, font=("Arial", 14))  # Sombra
            self.canvas.create_text(WIDTH // 2, HEIGHT // 2 + 30, text="Presiona Espacio para reiniciar", fill=WHITE, font=("Arial", 14))
    
    def update(self):
        self.move_snake()
        self.draw()
        if not self.game_over:
            self.root.after(SPEED, self.update)
    
    def restart(self, event=None):
        self.snake = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (0, -BLOCK_SIZE)
        self.food = self.random_manzana()
        self.score = 0
        self.game_over = False
        self.update()

# Ejecuta el juego
if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
