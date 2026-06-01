import tkinter as tk
import random
from collections import deque

CELL_SIZE = 30
ROWS = 15
COLS = 15
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE


class MazeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор лабиринта")

        self.mode = None
        self.start = None
        self.finish = None
        self.path = []

        top_frame = tk.Frame(root)
        top_frame.pack(pady=5)

        tk.Button(top_frame, text="Сгенерировать", command=self.generate_maze).pack(side=tk.LEFT, padx=5)
        tk.Button(top_frame, text="Выбрать старт", command=lambda: self.set_mode("start")).pack(side=tk.LEFT, padx=5)
        tk.Button(top_frame, text="Выбрать финиш", command=lambda: self.set_mode("finish")).pack(side=tk.LEFT, padx=5)
        tk.Button(top_frame, text="Найти путь", command=self.find_path).pack(side=tk.LEFT, padx=5)

        self.info_label = tk.Label(root, text="Нажмите 'Сгенерировать'")
        self.info_label.pack()

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
        self.canvas.pack(pady=10)
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        self.cells = []
        self.generate_maze()

    def set_mode(self, mode):
        self.mode = mode
        if mode == "start":
            self.info_label.config(text="Кликните по клетке для выбора старта")
        else:
            self.info_label.config(text="Кликните по клетке для выбора финиша")

    def init_cells(self):
        self.cells = []
        for r in range(ROWS):
            row = []
            for c in range(COLS):
                row.append({
                    "top": True,
                    "right": True,
                    "bottom": True,
                    "left": True,
                    "visited": False
                })
            self.cells.append(row)

    def generate_maze(self):
        self.init_cells()
        self.start = None
        self.finish = None
        self.path = []

        stack = []
        r, c = 0, 0
        self.cells[r][c]["visited"] = True
        stack.append((r, c))

        while stack:
            r, c = stack[-1]
            neighbors = self.get_unvisited_neighbors(r, c)

            if neighbors:
                nr, nc, direction = random.choice(neighbors)
                self.remove_wall(r, c, nr, nc, direction)
                self.cells[nr][nc]["visited"] = True
                stack.append((nr, nc))
            else:
                stack.pop()

        for r in range(ROWS):
            for c in range(COLS):
                self.cells[r][c]["visited"] = False

        self.draw_maze()
        self.info_label.config(text="Лабиринт создан")

    def get_unvisited_neighbors(self, r, c):
        neighbors = []

        if r > 0 and not self.cells[r - 1][c]["visited"]:
            neighbors.append((r - 1, c, "top"))
        if c < COLS - 1 and not self.cells[r][c + 1]["visited"]:
            neighbors.append((r, c + 1, "right"))
        if r < ROWS - 1 and not self.cells[r + 1][c]["visited"]:
            neighbors.append((r + 1, c, "bottom"))
        if c > 0 and not self.cells[r][c - 1]["visited"]:
            neighbors.append((r, c - 1, "left"))

        return neighbors

    def remove_wall(self, r, c, nr, nc, direction):
        if direction == "top":
            self.cells[r][c]["top"] = False
            self.cells[nr][nc]["bottom"] = False
        elif direction == "right":
            self.cells[r][c]["right"] = False
            self.cells[nr][nc]["left"] = False
        elif direction == "bottom":
            self.cells[r][c]["bottom"] = False
            self.cells[nr][nc]["top"] = False
        elif direction == "left":
            self.cells[r][c]["left"] = False
            self.cells[nr][nc]["right"] = False

    def draw_maze(self):
        self.canvas.delete("all")

        for r in range(ROWS):
            for c in range(COLS):
                x1 = c * CELL_SIZE
                y1 = r * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                cell = self.cells[r][c]

                if cell["top"]:
                    self.canvas.create_line(x1, y1, x2, y1, width=2)
                if cell["right"]:
                    self.canvas.create_line(x2, y1, x2, y2, width=2)
                if cell["bottom"]:
                    self.canvas.create_line(x1, y2, x2, y2, width=2)
                if cell["left"]:
                    self.canvas.create_line(x1, y1, x1, y2, width=2)

        if self.start:
            self.draw_marker(self.start, "green")
        if self.finish:
            self.draw_marker(self.finish, "red")
        if self.path:
            self.draw_path()

    def draw_marker(self, cell_pos, color):
        r, c = cell_pos
        x1 = c * CELL_SIZE + 8
        y1 = r * CELL_SIZE + 8
        x2 = x1 + CELL_SIZE - 16
        y2 = y1 + CELL_SIZE - 16
        self.canvas.create_oval(x1, y1, x2, y2, fill=color)

    def draw_path(self):
        for r, c in self.path:
            x1 = c * CELL_SIZE + 10
            y1 = r * CELL_SIZE + 10
            x2 = x1 + CELL_SIZE - 20
            y2 = y1 + CELL_SIZE - 20
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="yellow", outline="")

        if self.start:
            self.draw_marker(self.start, "green")
        if self.finish:
            self.draw_marker(self.finish, "red")

    def on_canvas_click(self, event):
        c = event.x // CELL_SIZE
        r = event.y // CELL_SIZE

        if 0 <= r < ROWS and 0 <= c < COLS:
            if self.mode == "start":
                self.start = (r, c)
                self.path = []
                self.info_label.config(text=f"Старт: {self.start}")
            elif self.mode == "finish":
                self.finish = (r, c)
                self.path = []
                self.info_label.config(text=f"Финиш: {self.finish}")

            self.draw_maze()

    def get_neighbors_without_walls(self, r, c):
        neighbors = []
        cell = self.cells[r][c]

        if not cell["top"] and r > 0:
            neighbors.append((r - 1, c))
        if not cell["right"] and c < COLS - 1:
            neighbors.append((r, c + 1))
        if not cell["bottom"] and r < ROWS - 1:
            neighbors.append((r + 1, c))
        if not cell["left"] and c > 0:
            neighbors.append((r, c - 1))

        return neighbors

    def find_path(self):
        if not self.start or not self.finish:
            self.info_label.config(text="Сначала выберите старт и финиш")
            return

        queue = deque([self.start])
        came_from = {self.start: None}

        while queue:
            current = queue.popleft()

            if current == self.finish:
                break

            for neighbor in self.get_neighbors_without_walls(*current):
                if neighbor not in came_from:
                    queue.append(neighbor)
                    came_from[neighbor] = current

        if self.finish not in came_from:
            self.info_label.config(text="Путь не найден")
            return

        path = []
        cur = self.finish
        while cur is not None:
            path.append(cur)
            cur = came_from[cur]

        path.reverse()
        self.path = path
        self.draw_maze()
        self.info_label.config(text=f"Путь найден, длина: {len(path)}")

root = tk.Tk()
app = MazeApp(root)
root.mainloop()