import tkinter as tk
import random

#Configuración inicial
WIDTH = 600
HEIGHT = 400
#Tamaño del bloque que representa la serpiente y la manzana
BLOCK_SIZE = 20
#Velocidad(Menor valor más rapido y fluido va)
SPEED = 150

#Colores
BLACK = "#189100"
GREEN = "#00FF00"
RED = "#FF0000"
WHITE = "#FFFFFF"
BROWN = "#8B4513"  # Para el tallo de la manzana

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=BLACK)
        self.canvas.pack()
        
        #La serpiente empezará en el centro
        self.snake = [(WIDTH // 2, HEIGHT // 2)]
        #Se desplazará hacia arriba al inicio
        self.direction = (0, -BLOCK_SIZE)
        
        #Manzana
        self.food = self.random_manzana()
        
        #Puntuación
        self.score = 0
        
        # Estado del juego
        self.game_over = False
        
        # Dibujar elementos iniciales
        self.draw()
        
        #Controles con las flechas
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
            #Evitar reversa inmediata
            if (new_dir[0] * -1, new_dir[1] * -1) != self.direction:
                self.direction = new_dir
    
    def move_snake(self):
        if self.game_over:
            return
        
        #Calcula la nueva posición de la cabeza
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        
        #Verifica la colisión con bordes
        if (new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT):
            self.game_over = True
            return
        
        #Verificar la colisión con el cuerpo
        if new_head in self.snake:
            self.game_over = True
            return
        
        #Agrega nueva cabeza al comer
        self.snake.insert(0, new_head)
        
        # Verifica si come manzana
        if new_head == self.food:
            self.score += 1
            self.food = self.random_manzana()
        else:
            self.snake.pop()
    
    def draw(self):
        self.canvas.delete("all")
        
        #Dibujar serpiente
        for i, segment in enumerate(self.snake):
            if i == 0:  # Cabeza
                self.canvas.create_rectangle(segment[0], segment[1], 
                                             segment[0] + BLOCK_SIZE, segment[1] + BLOCK_SIZE, 
                                             fill=GREEN)
                #Ojos de la cabeza
                eye_size = 3
                eye_offset = 5
                self.canvas.create_oval(segment[0] + eye_offset, segment[1] + eye_offset,
                                        segment[0] + eye_offset + eye_size, segment[1] + eye_offset + eye_size,
                                        fill=BLACK)
                self.canvas.create_oval(segment[0] + BLOCK_SIZE - eye_offset - eye_size, segment[1] + eye_offset,
                                        segment[0] + BLOCK_SIZE - eye_offset, segment[1] + eye_offset + eye_size,
                                        fill=BLACK)
            else:
                self.canvas.create_rectangle(segment[0], segment[1], 
                                             segment[0] + BLOCK_SIZE, segment[1] + BLOCK_SIZE, 
                                             fill=GREEN)
        
        #Manzana
        self.canvas.create_oval(self.food[0], self.food[1] + 2, 
                                self.food[0] + BLOCK_SIZE, self.food[1] + BLOCK_SIZE, 
                                fill=RED)
        self.canvas.create_line(self.food[0] + BLOCK_SIZE // 2, self.food[1], 
                                self.food[0] + BLOCK_SIZE // 2, self.food[1] + 2, 
                                fill=BROWN, width=2)
        
        #Puntaje
        self.canvas.create_text(50, 20, text=f"Puntaje: {self.score}", fill=WHITE, font=("Arial", 16))
        
        #Gameover
        if self.game_over:
            self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over", fill=WHITE, font=("Arial", 24))
            self.canvas.create_text(WIDTH // 2, HEIGHT // 2 + 30, text="Presiona Espacio para reiniciar", fill=WHITE, font=("Arial", 12))
    
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

#Ejecuta el juego
if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
