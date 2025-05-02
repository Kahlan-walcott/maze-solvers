"""
Kahlan Walcott
Date: 4/15/2024
This code is for project 3 in CIS 163. It recursively goes through a maze and puts the coordinates into a singly linked
list that is returned to the user. It will find if a maze is solvable or not. If the maze is solvable it will find that
path and the sortest path.
"""


from typing import List
from llstack import LLStack
import math


class InvalidCoordinateError(Exception):
    """This class is used when the coordinate is not in the maze."""
    pass


class Maze:
    """This class controls everything that has to do with creating and moving through the maze."""
    def __init__(self, grid: List[List[str]], entry_loc: tuple, exit_loc: tuple):
        """This function sets up the grid, entry location, exit location, the number of rows and columns, the path that
        was taken and the shortest path available."""
        if not isinstance(grid, list):  # check to see if the grid is frst a list
            raise TypeError()
        else:  # when it is a list
            for lst in grid:  # go through it and check the contents
                if not isinstance(lst, list):  # see if everything in the first list is a list
                    raise TypeError()
                else:  # when grid is a list of lists
                    for coord in lst:  # go through it and check the contents
                        if not isinstance(coord, str):  # see if everything in the lists is a string
                            raise TypeError()
                        if coord != 'o':  # if the current string is not an o
                            if coord != 'x':  # if the current string is not an x
                                raise TypeError()
        self.__grid = grid

        if len(grid) < 3:  # if the length of the grid is less than 3 it is not a valid grid
            raise ValueError()
        else:  # if the grid is greater than 3 then it is valid
            self.__nrows = len(grid)

        if len(grid[0]) < 3:  # if the length of the second list is less than 3 it is not a valid grid
            raise ValueError()
        else:  # if the grid is greater than 3 it is valid
            self.__ncols = len(grid[0])

        if not isinstance(entry_loc, tuple):  # if the entry location is not a tuple raise a type error
            raise TypeError()
        else:  # when the entry location is a tuple check the information in it
            for num in entry_loc:  # go through the tuple
                if not isinstance(num, int):  # check to see if the things in the tuple are integers
                    raise TypeError()

        if (entry_loc[0] > self.__nrows - 1 or entry_loc[1] > self.__ncols - 1 or
                self.__grid[entry_loc[0]][entry_loc[1]] == "x"):  # make sure that the x coordinate of the entry location is not less than the index or the y coordinate in the entry location is not less than the indexes or the grid at the x and y coordinates of the entry is x/ a wall
            raise InvalidCoordinateError()
        self.__entry = entry_loc

        if not isinstance(exit_loc, tuple):  # if the exit location is not a tuple raise a type error
            raise TypeError()
        else:  # when the exit location is a tuple
            for num in exit_loc:  # check every thing in the tuple
                if not isinstance(num, int):  # when the things in the tuple are not integers raise a typ error
                    raise TypeError()
        if (exit_loc[0] > self.__nrows - 1 or exit_loc[1] > self.__ncols - 1 or
                self.__grid[exit_loc[0]][exit_loc[1]] == "x"): # make sure that the x coordinate of the exit location is not less than the index or the y coordinate in the exit location is not less than the indexes or the grid at the x and y coordinates of the exit  is x/a wall
            raise InvalidCoordinateError()
        self.__exit = exit_loc

        self.__path = None
        self.__shortest_path = None
        self.dict = {}
    @property
    def nrows(self):
        """This function returns the number of rows to be readable only."""
        return self.__nrows

    @property
    def ncols(self):
        """This function returns the number of columns to be readable only."""
        return self.__ncols

    @property
    def entry_coords(self):
        """This function returns the entry coordinates to be readable only."""
        return self.__entry

    @property
    def exit_coords(self):
        """This function returns the exit coordinates to be readable only."""
        return self.__exit

    @nrows.setter
    def nrows(self, num_rows):
        """This function allows the number of rows to be writable."""
        if num_rows < 3:  # checks that the input number of rows is greater then 3
            raise ValueError()
        else:  # if it is set __nrows to it
            self.__nrows = num_rows

    @ncols.setter
    def ncols(self, num_cols):
        """This function allows the number of columns to be writable."""
        if num_cols < 3:  # checks that the input number of columns is greater then 3
            raise ValueError()
        else:  # if it is set __ncols to it
            self.__ncols = num_cols

    @entry_coords.setter
    def entry_coords(self, entry: tuple):
        """This function allows the entry coordinates to be writable."""
        if not isinstance(entry, tuple):  # if the input entry coordinates are not in a tuple raise a type error
            raise TypeError()
        else:  # when the input coordinates are a tuple
            for num in entry:  # check everything in it
                if not isinstance(num, int):  # if the things in the tuple are not integers rais a type error
                    raise TypeError()
            row, col = entry
            if entry[0] > self.__nrows >= 0 or entry[1] > self.__ncols >= 0 or self.__grid[row][col] == "x":
                # if the first value in the input tuple is greater than the number of rows and the number of rows is greater than or equal to the number of rows or the second value is greater than the number of colums and the number of columns is greater or equal to 0 or the grid at that location is an x/wall
                raise InvalidCoordinateError()

    @exit_coords.setter
    def exit_coords(self, exits):
        """This function allows the exit coordinates to be writable."""
        if not isinstance(exits, tuple):  # if the input coordinates is not a tuple rais a type error
            raise TypeError()
        else:  # when the input coordinates are a tuple
            for num in exits:  # check everything in it
                if not isinstance(num, int):  # if the things in the tuple are not integers rais a type error
                    raise TypeError()
            row, col = exits
            if exits[0] > self.__nrows >= 0 or exits[1] > self.__ncols >= 0 or self.__grid[row][col] == "x":
                # if the first value in the input tuple is greater than the number of rows and the number of rows is greater than or equal to the number of rows or the second value is greater than the number of columns and the number of columns is greater or equal to 0 or the grid at that location is an x/wall
                raise InvalidCoordinateError()

    @property
    def path(self):
        """This function returns the path the solve function took as readable only."""
        return self.__path

    @property
    def shortest_path(self):
        """This function returns the path the solve_shortest function took as readable only."""
        return self.__shortest_path

    def solve(self):
        """This function finds a solution to a maze if it is solvable."""
        self.__path = LLStack()
        copy_grid = self.__grid[:][:]  # from Kayle
        if self.__solve_helper(self.__entry[0], self.__entry[1], copy_grid):  # if the recursive helper function returned true the maze is solvable
            return True
        self.__path = None
        return False

    def __solve_helper(self, x, y, grid):
        """This function recursively goes through the maze to find if it is solvable by either returning true if it is
        and False if it is not. It also adds each spot to the singly linked list, if the spot is not valid it is removed
        from the linked list."""
        if x >= self.__nrows or x < 0 or y < 0 or y >= self.__ncols:  # if the x coordinate is out of bounds or the y coordinate id out of bounds return False to go back inside the maze
            return False
        if grid[x][y] != 'o':  # check to see if the current spot is a wall, if it is return False to go back
            return False

        grid[x][y] = 'Visited'  # from Kayle
        self.__path.push((x, y))
        if (x, y) == self.__exit:  # when the exit has been reached the maze has been solved and true can be returned
            return True

        if (self.__solve_helper(x + 1, y, grid) or self.__solve_helper(x, y - 1, grid) or
                self.__solve_helper(x, y + 1, grid) or self.__solve_helper(x - 1, y, grid)):  # if you can move down, left, right, or up then return true
            return True

        self.__path.pop()
        return False

    def solve_shortest(self):
        """This function finds the shortest path to the exit."""
        if self.__shortest_helper_dic(self.__entry[0], self.__entry[1],
                                      self.__grid[:][:]):  # if the recursive helper function returned true there is a shorter path
            return True
        if self.__shortest_helper_stack(self.__entry[0], self.__entry[1]):
            self.__shortest_path = None
            return False

    def __shortest_helper_dic(self, x, y, grid):
        """This function recursively goes through the maze to find all solutions and then compares them to find the
        shortest one. It returns true if it can be found, if it can't false is returned."""
        if x >= self.__nrows or x < 0 or y < 0 or y >= self.__ncols:  # if the x coordinate is out of bounds or the y coordinate id out of bounds return False to go back inside the maze
            # self.__dict[(x, y)] = math.inf
            return
        if grid[x][y] != 'o':  # check to see if the current spot is a wall, if it is return False to go back
            # self.__dict[(x, y)] = math.inf
            return
        if grid[x][y] == 'Visited':
            return
        if (x, y) in self.dict:
            return
        grid[x][y] = 'Visited'
        if x == self.__exit[0] and y == self.__exit[1]:
            self.dict[(x, y)] = 1
            return
        self.__shortest_helper_dic(x + 1, y, grid)  # down
        self.__shortest_helper_dic(x - 1, y, grid)  # up
        self.__shortest_helper_dic(x, y + 1, grid)  # right
        self.__shortest_helper_dic(x, y - 1, grid)  # left
        # from Julian
        self.dict[(x, y)] = 1 + min(self.dict.get((x + 1, y), math.inf), self.dict.get((x - 1, y), math.inf),
                                      self.dict.get((x, y + 1), math.inf), self.dict.get((x, y - 1), math.inf))
        print(self.dict)
        grid[x][y] = 'o'

    def __shortest_helper_stack(self, x, y):
        self.__shortest_path = LLStack()
        if (x, y) == self.__exit:
            return

        self.__shortest_path.push(self.__entry)
        nabors = {(x + 1, y): self.dict.get((x + 1, y), math.inf), (x - 1, y): self.dict.get((x - 1, y), math.inf),
                 (x, y + 1): self.dict.get((x, y + 1), math.inf), (x, y - 1): self.dict.get((x, y - 1), math.inf)}
        direction = min(nabors, key=nabors.get)
        self.__shortest_helper_stack(direction[0], direction[1])
        print()
        print(nabors)
        print(direction)

if __name__ == "__main__":
    grid2 = [['o', 'x', 'o', 'o', 'o'],
             ['o', 'x', 'o', 'x', 'o'],
             ['o', 'o', 'o', 'x', 'o'],
             ['o', 'x', 'x', 'o', 'o'],
             ['o', 'o', 'o', 'o', 'o']]

    grids = [['o', 'o', 'o', 'o'],
             ['o', 'o', 'x', 'o'],
             ['o', 'o', 'x', 'o'],
             ['x', 'x', 'o', 'o']]
    entry = (0, 0)
    exits = (3, 3)
    
    maze = Maze(grids, entry, exits)
    maze.solve_shortest()

