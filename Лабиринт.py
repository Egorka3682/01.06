import tkinter as tk
from tkinter import messagebox
import random
from collections import deque


class MazeApp:
    def __init__(self, root):
        self.root = root

        self.root.title("Генератор лабиринта")

        self.cell_size = 25
        self.rows = 10
        self.cols = 10

        self.start = (0, 0)
        self.finish = (self.rows - 1, self.cols - 1)

        self.maze = []
        self.visited = []

        top_frame = tk.Frame(root)
        top_frame.pack(pady=10)

        tk.Button(top_frame, text="Сгенерировать", command=self.generate_maze).pack(side=tk.LEFT, padx=5)
        tk.Button(top_frame, text="Найти путь", command=self.find_path).pack(side=tk.LEFT, padx=5)

        self.canvas = tk.Canvas(
            root,
            width=self.cols * self.cell_size,
            height=self.rows * self.cell_size,
            bg="white"
        )
        self.canvas.pack()


        self.canvas.bind("<Button-1>", self.set_start)   # левая кнопка
        self.canvas.bind("<Button-3>", self.set_finish)  # правая кнопка

        self.generate_maze()

    def create_empty_maze(self):
        self.maze = []
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                row.append({"top": True, "right": True, "bottom": True, "left": True})
            self.maze.append(row)

    def generate_maze(self):
        self.create_empty_maze()

        self.visited = [[False]*self.cols for _ in range(self.rows)]
        self.dfs_generate(0, 0)

        self.start = (0, 0)
        self.finish = (self.rows - 1, self.cols - 1)

        self.draw_maze()

    def dfs_generate(self, r, c):
        self.visited[r][c] = True

        directions = [("top",-1,0),("right",0,1),("bottom",1,0),("left",0,-1)]
        random.shuffle(directions)

        for direction, dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < self.rows and 0 <= nc < self.cols and not self.visited[nr][nc]:
                if direction == "top":
                    self.maze[r][c]["top"] = False
                    self.maze[nr][nc]["bottom"] = False
                elif direction == "right":
                    self.maze[r][c]["right"] = False
                    self.maze[nr][nc]["left"] = False
                elif direction == "bottom":
                    self.maze[r][c]["bottom"] = False
                    self.maze[nr][nc]["top"] = False
                elif direction == "left":
                    self.maze[r][c]["left"] = False
                    self.maze[nr][nc]["right"] = False

                self.dfs_generate(nr, nc)

    def draw_maze(self):
        self.canvas.delete("all")

        for r in range(self.rows):
            for c in range(self.cols):
                x1 = c * self.cell_size
                y1 = r * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                cell = self.maze[r][c]

                if cell["top"]:
                    self.canvas.create_line(x1, y1, x2, y1)
                if cell["right"]:
                    self.canvas.create_line(x2, y1, x2, y2)
                if cell["bottom"]:
                    self.canvas.create_line(x1, y2, x2, y2)
                if cell["left"]:
                    self.canvas.create_line(x1, y1, x1, y2)

        self.draw_start_finish()

    def draw_start_finish(self):
        sr, sc = self.start
        fr, fc = self.finish

        self.paint_cell(sr, sc, "green")
        self.paint_cell(fr, fc, "red")

    def paint_cell(self, r, c, color):
        x1 = c * self.cell_size + 4
        y1 = r * self.cell_size + 4
        x2 = x1 + self.cell_size - 8
        y2 = y1 + self.cell_size - 8
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)


    def set_start(self, event):
        col = event.x // self.cell_size
        row = event.y // self.cell_size

        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.start = (row, col)
            self.draw_maze()


    def set_finish(self, event):
        col = event.x // self.cell_size
        row = event.y // self.cell_size

        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.finish = (row, col)
            self.draw_maze()

    def get_neighbors(self, r, c):
        neighbors = []
        cell = self.maze[r][c]

        if not cell["top"] and r > 0:
            neighbors.append((r-1, c))
        if not cell["right"] and c < self.cols-1:
            neighbors.append((r, c+1))
        if not cell["bottom"] and r < self.rows-1:
            neighbors.append((r+1, c))
        if not cell["left"] and c > 0:
            neighbors.append((r, c-1))

        return neighbors

    def find_path(self):
        queue = deque([self.start])
        parents = {}
        used = {self.start}

        while queue:
            cur = queue.popleft()

            if cur == self.finish:
                break

            for nxt in self.get_neighbors(cur[0], cur[1]):
                if nxt not in used:
                    used.add(nxt)
                    parents[nxt] = cur
                    queue.append(nxt)

        if self.finish not in used:
            messagebox.showinfo("Ошибка", "Путь не найден")
            return

        path = []
        cur = self.finish
        while cur != self.start:
            path.append(cur)
            cur = parents[cur]
        path.append(self.start)

        self.draw_maze()

        for r, c in path:
            x = c * self.cell_size + self.cell_size // 2
            y = r * self.cell_size + self.cell_size // 2
            self.canvas.create_oval(x-3, y-3, x+3, y+3, fill="blue")


root = tk.Tk()
app = MazeApp(root)
root.mainloop()