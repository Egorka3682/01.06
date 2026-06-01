class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[None for _ in range(width)] for _ in range(height)]