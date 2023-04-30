import unittest
from GUIsudoku import Grid

class TestSudokuSolver(unittest.TestCase):
    
    def setUp(self):
        self.grid = Grid(9, 9, 540, 540, None)

    def test_place(self):
        self.assertFalse(self.grid.place(5))
        self.assertTrue(self.grid.place(1))
        self.assertFalse(self.grid.place(1))
        self.assertTrue(self.grid.place(2))

    def test_sketch(self):
        self.grid.select(0, 0)
        self.grid.sketch(5)
        self.assertEqual(self.grid.cubes[0][0].temp, 5)

    def test_click(self):
        pos = (200, 200) # arbitrary position
        self.assertEqual(self.grid.click(pos), (2, 2))

    def test_is_finished(self):
        self.assertFalse(self.grid.is_finished())
        self.grid.solve()
        self.assertTrue(self.grid.is_finished())

    def test_solve(self):
        # The following board can be solved using the given solver
        board = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]
        self.grid.board = board
        self.grid.solve()
        for i in range(9):
            self.assertTrue(all(0 < x < 10 for x in self.grid.model[i]))
            self.assertTrue(len(set(self.grid.model[i])) == 9)
            self.assertTrue(all(0 < x < 10 for x in [self.grid.model[j][i] for j in range(9)]))
            self.assertTrue(len(set([self.grid.model[j][i] for j in range(9)])) == 9)
        for i in range(3):
            for j in range(3):
                self.assertTrue(len(set([self.grid.model[x][y] for x in range(3*i, 3*i+3) for y in range(3*j, 3*j+3)])) == 9)
