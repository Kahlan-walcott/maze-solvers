import unittest
from llstack import LLStack
from maze import Maze


class TestLLStack(unittest.TestCase):

    def test_pop(self):  # shows that the function removes the top node on the stack
        head = LLStack()
        head.push((0, 1))
        head.push((2, 1))
        head.push((3, 1))
        self.assertEqual((3, 1), LLStack.pop(head))

    def test_push(self):  # shows the function adds a new node to the top of the stack
        head = LLStack()
        # head.push((0, 1))
        # head.push((2, 1))
        # head.push((3, 1))
        self.assertEqual(head.push((0, 2)), LLStack.push(LLStack(), (0, 2)))

    def test_string(self):  # shows that the string outputs that correct thing
        head = LLStack()
        head.push((0, 1))
        head.push((2, 1))
        head.push((3, 1))
        self.assertEqual('(3,1) -> (2,1) -> (0,1)', LLStack.__str__(head))


class TestMaze(unittest.TestCase):

    def test_helper_larger_grid_true(self):
        grid1 = [['o', 'x', 'o', 'o', 'o', 'x', 'o', 'x'],
                 ['o', 'x', 'o', 'x', 'o', 'x', 'x', 'o'],
                 ['o', 'o', 'o', 'x', 'o', 'o', 'x', 'x'],
                 ['x', 'x', 'x', 'o', 'x', 'o', 'o', 'x'],
                 ['o', 'o', 'x', 'o', 'o', 'x', 'o', 'o'],
                 ['x', 'x', 'x', 'o', 'o', 'o', 'o', 'o'],
                 ['o', 'x', 'o', 'o', 'x', 'x', 'x', 'x']]
        entry = (0, 0)
        exits = (6, 2)
        solve = Maze(grid1, entry, exits)
        self.assertTrue(True, solve.solve())

    def test_helper_medium_grid_true(self):
        grid1 = [['o', 'x', 'o', 'o', 'o'],
                 ['o', 'x', 'o', 'x', 'o'],
                 ['o', 'o', 'o', 'x', 'o'],
                 ['o', 'x', 'x', 'o', 'o'],
                 ['o', 'o', 'o', 'o', 'o']]
        entry = (0, 0)
        exits = (4, 4)
        solve = Maze(grid1, entry, exits)
        self.assertTrue('True', solve.solve())

    def test_helper_medium_grid_false(self):
        grid1 = [['o', 'x', 'o', 'o', 'o'],
                 ['o', 'x', 'o', 'x', 'o'],
                 ['o', 'o', 'o', 'x', 'o'],
                 ['o', 'x', 'x', 'o', 'o'],
                 ['o', 'o', 'o', 'x', 'o']]
        entry = (0, 0)
        exits = (4, 4)
        solve = Maze(grid1, entry, exits)
        self.assertFalse(False, solve.solve())

    def test_helper_smaller_grid_true(self):
        grid2 = [['o', 'x', 'x', 'x'],
                 ['o', 'x', 'x', 'x'],
                 ['o', 'o', 'o', 'x'],
                 ['x', 'x', 'o', 'o']]
        entry = (0, 0)
        exits = (3, 3)
        solve = Maze(grid2, entry, exits)
        self.assertTrue(True, solve.solve())

    def test_helper_smaller_grid_false(self):
        grid2 = [['o', 'x', 'x', 'x'],
                 ['o', 'x', 'x', 'x'],
                 ['o', 'o', 'x', 'x'],
                 ['x', 'x', 'o', 'o']]
        entry = (0, 0)
        exits = (3, 3)
        solve = Maze(grid2, entry, exits)
        self.assertFalse(False, solve.solve())

    def test_helper_tiny_grid_true(self):
        grid2 = [['o', 'x', 'x'],
                 ['o', 'x', 'x'],
                 ['o', 'o', 'o']]
        entry = (0, 0)
        exits = (2, 2)
        solve = Maze(grid2, entry, exits)
        self.assertTrue(True, solve.solve())

    def test_helper_tiny_grid_false(self):
        grid2 = [['o', 'x', 'x'],
                 ['o', 'x', 'x'],
                 ['o', 'x', 'o']]
        entry = (0, 0)
        exits = (2, 2)
        solve = Maze(grid2, entry, exits)
        self.assertFalse(False, solve.solve())

    def test_sortest_dict(self):
        grid = [['o', 'x', 'o', 'o', 'o'],
                ['o', 'x', 'o', 'x', 'o'],
                ['o', 'o', 'o', 'x', 'o'],
                ['o', 'x', 'x', 'o', 'o'],
                ['o', 'o', 'o', 'o', 'o']]
        entry = (0, 0)
        exits = (4, 4)
        solve = Maze(grid, entry, exits)
        self.assertEqual('', solve.solve_shortest())


