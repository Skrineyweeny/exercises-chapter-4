import numpy as np
from matplotlib import pyplot
from scipy.signal import convolve2d

glider = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])

blinker = np.array([
    [0, 0, 0],
    [1, 1, 1],
    [0, 0, 0]]
)

glider_gun = np.array([
    [0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0]
])


class Game:
    """Initialise the Game class."""

    def __init__(self, size):
        """Initialise Game class."""
        self.board = np.zeros((size, size))

    def play(self):
        """Play module."""
        print("Playing life. Press ctrl + c to stop.")
        pyplot.ion()
        while True:
            self.move()
            self.show()
            pyplot.pause(0.0000005)

    def move(self):
        """Move module."""
        stencil = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        neighbour_count = convolve2d(self.board, stencil, mode='same')

        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                self.board[i, j] = 1 if (neighbour_count[i, j] == 3
                                         or (neighbour_count[i, j] == 2
                                             and self.board[i, j])) else 0

    def __setitem__(self, key, value):
        """Setitem module."""
        self.board[key] = value

    def show(self):
        """Show module."""
        pyplot.clf()
        pyplot.matshow(self.board, fignum=0, cmap='binary')
        pyplot.show()

    def insert(self, other, coords):
        """Insert patterns into the main grid."""
        if isinstance(other, Pattern):
            if isinstance(coords, list or tuple or np.ndarray):
                if len(coords) == 2:
                    n_by_n = len(other.grid)
                    coords_x = coords[0]
                    coords_y = coords[1]
                    for i in range(n_by_n):
                        for j in range(n_by_n):
                            self.board[
                                i + coords_x - n_by_n//2,
                                j + coords_y - n_by_n//2
                                      ] = other.grid[i, j]
                else:
                    return NotImplemented
        else:
            return NotImplemented


class Pattern:
    """Initialise the pattern class."""

    def __init__(self, grid):
        """Initialise the pattern."""
        self.grid = grid

    def flip_vertical(self):
        """Flip a given pattern vertically."""
        return Pattern(self.grid[::-1])

    def flip_horizontal(self):
        """Flip a given pattern horizontally."""
        a = np.zeros_like(self.grid)
        rows, cols = np.shape(a)

        for i in range(rows):
            for j in range(cols):
                a[i, cols - 1 - j] = self.grid[i, j]

        return Pattern(a)

    def flip_diag(self):
        """Flip a given pattern diagonally."""
        return Pattern(np.transpose(self.grid))

    def rotate(self, n):
        """Rotate oneself."""
        result = self
        for i in range(n % 4):
            result = result.flip_diag().flip_vertical()

        return result
