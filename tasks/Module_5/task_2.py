from dataclasses import dataclass

import pyinputplus as pyip


@dataclass
class Item:
    name: str
    weight: int
    price: int


@dataclass
class Hero:
    stamina: int


class Board:

    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.board_items = []


board_items = [Item('gold coin', 2, 4), '', Item('dagger', 3, 1),
               '', Item('gold coin', 2, 1), '',
               'H', Item('dagger', 5, 8), '']

BOUNDARY = '\n+---+---+---+'


def print_board(board, init_board):
    print(BOUNDARY)
    for row in (board[i:i + init_board.rows] for i in
                range(0, init_board.rows * init_board.columns, init_board.columns)):
        print("|", end="")
        for e in row:
            if isinstance(e, Item):
                e = "X"
            print("{:^3}|".format(e), end="")
        print(BOUNDARY)


def move_hero(board, hero):
    hero_movement = pyip.inputMenu(["north", "south", "west", "east"], numbered=True)
    for i, k in enumerate(board, 1):
        if k == "H":
            if hero_movement == "north" and i > 3:
                board[i - 1] = ""
                board[i - 3 - 1] = "H"
                reduce_stamina(hero)
                break
            elif hero_movement == "south" and i < 6:
                board[i - 1] = ""
                board[i + 3 - 1] = "H"
                reduce_stamina(hero)
                break
            elif hero_movement == "west" and i % 3 != 1:
                board[i - 1] = ""
                board[i - 2] = "H"
                reduce_stamina(hero)
                break
            elif hero_movement == "east" and i % 3 != 0:
                board[i - 1] = ""
                board[i] = "H"
                reduce_stamina(hero)
                break
            print("The end of map. Try right direction")
    print("===================================")
    return hero


def reduce_stamina(hero):
    hero.stamina -= 10
    print(f"Stamina = {hero.stamina}")


class Play:

    def __init__(self, board, hero):
        self.board = board
        self.hero = hero

    def play_game(self):
        print_board(board_items, self.board)
        while self.hero.stamina > 0:
            move_hero(board_items, self.hero)
            print_board(board_items, self.board)


board = Board(3, 3)
play = Play(board, Hero(50))
play.play_game()
