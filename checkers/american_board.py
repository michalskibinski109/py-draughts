from __future__ import annotations
from typing import Generator
from checkers.base_board import BaseBoard
from checkers.models import T8X8, Move
import numpy as np
"""
 board 8x8
 Short moves only 
 Cannot capture backwards
 Capture - choose any
"""
class AmericanBoard(BaseBoard):
    
    STARTING_POSITION = np.array([1] * 12 + [0] * 8 + [-1] * 12, dtype=np.int8)
    size =int(np.sqrt(len(STARTING_POSITION) * 2))
    row_idx = { val:val//4 for val in range(len(STARTING_POSITION))}
    col_idx = { val:val%8 for val in range(len(STARTING_POSITION))}
    SQUARES_MAP = T8X8

    def legal_moves(self) -> Generator[Move, None, None]:
        moves: list[Move] = []
        
        """
        Standard:
            1  (+4, +5) -> 5,6 
            4 [size//2] (+4)  -> 8
            8 (+4, +5) -> 11, 12
            CHECK IF:
            row(x+4) == row(x) + 1
            row(x+5) == row(x) + 1
        Captures:
            1: (+9) -> 10, !8
            2: (+7, +9) -> 9, 11
            CHECK IF 
            row(x+7) == row(x) + 2
            row(x+9) == row(x) + 2
        """


b= AmericanBoard()