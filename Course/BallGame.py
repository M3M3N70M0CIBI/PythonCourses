from tkinter import *
import time
import random

# Окно приложения
tk = Tk()
tk.title('Ball Game')
tk.resizable(0,0)
tk.wm_attributes('-topmost', 1)

# Полотно игры
canvas = Canvas(tk, width=500, height=400, highlightthickness=0)
canvas.pack()
tk.update()

# Класс объекта игры: шарик
class Ball:

    def __init__(self, canvas, paddle, score, color):

        self.canvas = canvas
        self.paddle = paddle
        self.score = score

        # Обозначение шарика в пространстве
        self.id = canvas.create_oval(10,10,25,25, fill=color)
        self.canvas.move(self.id, 245, 100)

        # Начальные точки
        startPoint = [-2, -1, 1, 2]
        
        random.shuffle(startPoint)

        self.x = startPoint[0]
        self.y = -2

        # Определение позиции шарика на полотне
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        # Логика: коснулся ли шарик низа?
        self.hit_bottom = False
        
    def hit_paddle(self, pos):

        paddle_pos = self.canvas.coords(self.paddle.id)
        
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.score.hit()
                return True
            
        return False
    
    # Отрисовка шарика
    def draw(self):

        self.canvas.move(self.id, self.x, self.y)

        pos = self.canvas.coords(self.id)

        # Падение сверху
        if pos[1] <= 0:
            self.y = 2

        # Падение шарика на дно
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            canvas.create_text(250, 120, text='Вы проиграли', font=('Comic Sans MS', 30), fill='red')

        # Касание платформы
        if self.hit_paddle(pos) == True:
            self.y = -2
        
        # Касание левой стенки
        if pos[0] <= 0:
            self.x = 2
        
        # Касание правой стенки
        if pos[2] >= self.canvas_width:
            self.x = -2

# Класс объекта игры: платформы
class Paddle:

    def __init__(self, canvas, color):
        
        self.canvas = canvas

        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)

        # Начальные точки
        startPoints = [40, 60, 90, 120, 150, 180, 200]
        random.shuffle(startPoints)

        self.starting_point_x = startPoints[0]
        self.canvas.move(self.id, self.starting_point_x, 300)

        self.x = 0

        self.canvas_width = self.canvas.winfo_width()

        # Обработчик нажатий

        # Если стрелка вправо — turn_right()
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

        # Если стрелка влево — turn_left()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)

        # Блок до запуска игры
        self.started = False

        # При нажатии на Enter - игра запускается
        self.canvas.bind_all('<KeyPress-Return>', self.start_game)
    
    def turn_right(self, event):

        self.x = 2
    
    def turn_left(self, event):
        
        self.x = -2

    def start_game(self, event):

        self.started = True

    # Отрисовка платформы и ее движений
    def draw(self):

        self.canvas.move(self.id, self.x, 0)
        
        pos = self.canvas.coords(self.id)

        # Остановка при столкновении с левой границей
        if pos[0] <= 0:
            
            self.x = 0

        # Остановка при столкновении с правой границей
        elif pos[2] >= self.canvas_width:

            self.x = 0

# Класс объекта игры: счёт
class Score:

    def __init__(self, canvas, color):

        self.score = 0
        self.canvas = canvas

        self.id = canvas.create_text(450, 10, text=self.score, font=('Comic Sans MS', 20), fill= color)
    
    def hit(self):
        
        self.score += 1

        self.canvas.itemconfig(self.id, text=self.score)
        

# Код игры

# Функция выхода при нажатии на кнопку ESC
def on_escape(event):
    tk.destroy()
    quit('Игра закрыта!')
    
       
canvas.bind_all("<Escape>", on_escape)

while True:
    score = Score(canvas, 'white')

    paddle = Paddle(canvas, 'white')

    ball = Ball(canvas, paddle, score, 'red')

    while not ball.hit_bottom:

        if paddle.started == True:
            
            ball.draw()
            
            paddle.draw()
        
        # Обновление поля: draw()
        tk.update_idletasks()

        # Обновление поля: функции
        tk.update()

        time.sleep(0.01)

    time.sleep(3)
    
    canvas.delete('all')