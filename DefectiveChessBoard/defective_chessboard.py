from random import randint
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 


class ChessBoard:
    def __init__(self, k=3, show_intermediate=False):
        '''
        the class handling the board and tiling logic.

        k: represents a board of size 2^k

        show_intermediate: if True, plots the board after each individual
            tiling. Since it uses pyplot, closing the plot's popup window 
            at each stage will trigger the next step of the tiling.
        '''
        self.k = k
        self.show_intermediate = show_intermediate

        # initializing the board
        self.board = self._createboard()

        # setting trionimo count to 0
        # this allows us to display the count on the board
        self.num_tri = 0

    def _createboard(self):
        '''
        k: represents the size of the board.
            Number of squares on the board = 2^k * 2^k
        '''
        print("Generating a board with a side length of {} tiles..." \
            .format(2**self.k))
        rows = [[] for i in range(2**self.k)]
        for i in range(2**self.k):
            rows[i] = [0] * 2**self.k
        return rows


    def add_defect(self):
        '''
        adds a random defect to the board. A defect
        here means that no trinimo can overlap with the
        defected square.
        '''
        len_ = len(self.board)
        row = randint(0, len_ - 1)
        col = randint(0, len_ - 1)

        print("Adding a defect at ({}, {})...".format(row, col))

        self.board[row][col] = -1


    def _locate_defect(self, r1, c1, r2, c2):
        '''
        (r1, c1): row, column number of upper left square of board
        (r2, c2): row, column number of lower right square
        '''

        # find defective elem
        r = 0
        c = 0
        loc_ = []
        for i in range(r1, r2 + 1):
            loc_[:] = self.board[i][c1:c2 + 1]
            if -1 in loc_:
                c = loc_.index(-1) + c1
                r = i
                break
        # top
        if r <= r1 + (r2 - r1) // 2:
            # left
            if c <= c1 + (c2 - c1) // 2:
                return 0, r, c
            # right
            else:
                return 1, r, c

        # bottom
        else:
            # left
            if c <= c1 + (c2 - c1) // 2:
                return 2, r, c
            # right
            else:
                return 3, r, c

    def drawboard(self, size=(8, 8), annot=True):
        '''
        plots the board.

        size: size of plot
        annot: if true, displays the number of the trionimo a particular
            square belongs to.
        '''

        plt.figure(figsize=size)
        _ = sns.heatmap(self.board, linewidths=.1, linecolor='white',
                    annot=False, cmap='magma', yticklabels=False,
                    xticklabels=False, cbar=False, square=True)

        _ = sns.heatmap(self.board, linewidths=.1, linecolor='white',
                    annot=annot, cmap='magma', yticklabels=False,
                    xticklabels=False, cbar=False, square=True,
                    mask=np.array(self.board)<0)
        plt.show()

    def _add_trionimo(self, defect, r1, c1, r2, c2):
        '''
        defect: integer between 0-3 representing which quadrant of the
            board the defect lies in.
            0: top-left
            1: top-right
            2: bottom-left
            3: bottom-right
        '''

        dict_ = {
            0: (r1, c1),
            1: (r1, c2),
            2: (r2, c1),
            3: (r2, c2),
        }

        self.num_tri += 1
        for i in range(r1, r2 + 1):
            self.board[i][c1:c2+1] = [self.num_tri]*(r2-r1 + 1)

        rd, cd = dict_[defect]
        self.board[rd][cd] = -1


    def _tile_rec(self, r1, c1, r2, c2):
        '''
        the recursive util function which performs the recursive
        tiling
        '''

        # centre coordinates
        dict_ = {
                0: (r1 + (r2 - r1)//2, c1 + (c2 - c1)//2),
                1: (r1 + (r2 - r1)//2, c1 + (c2 - c1)//2 + 1),
                2: (r1 + (r2 - r1)//2 + 1, c1 + (c2 - c1)//2),
                3: (r1 + (r2 - r1)//2 + 1, c1 + (c2 - c1)//2 + 1)
            }

        # locate defect quadrant
        if self.show_intermediate:
            self.drawboard()
        defect, r, c = self._locate_defect(r1, c1, r2, c2)

        # if board size == 2 x 2
        if (r1 == r2 - 1) and (c1 == c2 - 1):
            self._add_trionimo(defect, r1, c1, r2, c2)
            return None

        else:
            # add defect to centres
            redo = True
            for value in dict_.values():
                if self.board[value[0]][value[1]] == 0:
                    self.board[value[0]][value[1]] = -1
                else:
                    redo = False
            if redo:
                self.board[dict_[defect][0]][dict_[defect][1]] = 0

            # solving the four sub-problems: each of the four quadrants
            self._tile_rec(r1, c1, r1 + (r2-r1)//2, c1 + (c2 - c1)//2),
            self._tile_rec(r1, c1 + (c2 - c1)//2 + 1, r1 + (r2-r1)//2, c2),
            self._tile_rec(r1 + (r2-r1)//2 + 1, c1, r2, c1 + (c2 - c1)//2),
            self._tile_rec(r1 + (r2-r1)//2 + 1, c1 + (c2 - c1)//2 + 1, r2, c2)

            # add last trionimo to cover defects
            self.num_tri += 1

            # assume that first defect was centre
            redo = True
            for value in dict_.values():
                if self.board[value[0]][value[1]] == -1:
                    self.board[value[0]][value[1]] = self.num_tri
                else:
                    redo = False
            if redo:
                self.board[dict_[defect][0]][dict_[defect][1]] = -1


    def tile(self):
        '''
        the main tiling function. Takes an untiled board
        with a single defect and places trionimos on it.
        '''

        print("Starting the tiling process...")
        self._tile_rec(0, 0, 2**self.k - 1, 2**self.k - 1)

        print("Tiling complete...")
        self.drawboard()


if __name__ == '__main__':
    
    # setting the value of  k
    k = 3

    # creating a chess board of side 2^k
    board = ChessBoard(k)

    # adding a random defect to the board
    board.add_defect()

    # the tile function calls the drawboard(), allowing us
    # to view the state of the board at each recursive call
    board.tile()