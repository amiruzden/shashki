# импортируем ткинтер, чтобы создать графинтерфейс
import tkinter as tk

# функция для рисования доски
def draw_board(canvas, size): # функция будет рисовать доску, она принимает два аргумента (холст и размер)
    cell_size = size // 8 # размер одной клеточки, делим размер всей доски на 8
    
    for row in range(8): # два вложенных цикла для прохода по каждой строке и колонке доски (8 строк и 8 колонок)
        for col in range(8):
            x1 = col * cell_size # координаты верхнего левого угла клетки, рассчитываются умножением номера столбца на размер клетки
            y1 = row * cell_size # то же самое для строки
            x2 = x1 + cell_size # координаты нижнего правого угла клетки, вычисляются добавлением размера клетки к x1 и y1
            y2 = y1 + cell_size
            
            # чередуем цвета клеточек
            if (row + col) % 2 == 0:
                canvas.create_rectangle(x1, y1, x2, y2, fill="white")
            else:
                canvas.create_rectangle(x1, y1, x2, y2, fill="black")
                
# функция для размещения шашек на доске
def draw_pieces(canvas, size):
    cell_size = size // 8 # размер клеточки
    piece_radius = cell_size // 2.5 # радиус шашки
    
    # расставляем белые шашки
    for row in range(3): # по первым трем строкам
        for col in range(8): # по первым восьми колонкам
            if (row + col) % 2 != 0: # проверяем находятся ли на черном поле
                x_center = col * cell_size + cell_size // 2 # координаты центра клетки
                y_center = row * cell_size + cell_size // 2 # координаты центра клетки
                canvas.create_oval(x_center - piece_radius, y_center - piece_radius, # создаем круг (шашка) белого цвета
                                   x_center + piece_radius, y_center + piece_radius, 
                                   fill="white")
            
    # расставляем красные шашки
    for row in range(5, 8):
        for col in range(8):
            if (row + col) % 2 != 0:
                x_center = col * cell_size + cell_size // 2
                y_center = row * cell_size + cell_size // 2
                canvas.create_oval(x_center - piece_radius, y_center - piece_radius, # создае красные шашки (черные на черном не видны)
                                   x_center + piece_radius, y_center + piece_radius,
                                   fill="red")
                               
# создание основного окошка и холста
root = tk.Tk()
root.title("Шашки")

window_size = 400
canvas = tk.Canvas(root, width=window_size, height=window_size)
canvas.pack()

# вызов функции рисования доски и шашек
draw_board(canvas, window_size)
draw_pieces(canvas, window_size)

# запуск основного цикла окна
root.mainloop()                  