import os


class TicTac:
    def __init__(self):
        self.__board = [[0 for i in range(3)] for j in range(3)]
        self.__dct = {-1: "0", 0: ".", 1: "x"}
        self.__turn = 1
        self.__move = 0

    def show_board(self):
        for i in self.__board:
            for j in i:
                print(self.__dct[j], end="  ")
            print()

    def validate_input(self, inp):
        if inp.isdigit():
            tmp = int(inp)
            if 0 <= tmp <= 8:
                if self.__board[tmp // 3][tmp % 3] == 0:
                    return True
                print("Это значение уже занято")
            else:
                print("Значение должно быть от 0 до 8")
        else:
            print("Входное значение - число от 0 до 8")
        return False

    def make_move(self, inp):
        inp = int(inp)
        self.__board[inp // 3][inp % 3] = self.__turn
        if self.__turn == 1:
            self.__turn = -1
        else:
            self.__turn = 1

    def check_col(self):
        for i in range(3):
            sum_col = 0
            for j in self.__board:
                sum_col += j[i]
            if sum_col in (-3, 3):
                return sum_col // 3
        return 0

    def check_row(self):
        for i in range(3):
            sum_row = sum(self.__board[i][:])
            if sum_row in (-3, 3):
                return sum_row // 3
        return 0

    def check_diag(self):
        sum_diag = 0
        for i in range(3):
            sum_diag += self.__board[i][i]
        if sum_diag in (-3, 3):
            return sum_diag // 3
        sum_diag = 0
        for i in range(3):
            sum_diag += self.__board[i][2 - i]
        if sum_diag in (-3, 3):
            return sum_diag // 3
        return 0

    def check_winner(self):
        win_col = self.check_col()
        if win_col in (-1, 1):
            return win_col
        win_row = self.check_row()
        if win_row in (-1, 1):
            return win_row
        return self.check_diag()

    def start_game(self):
        self.show_board()
        while not self.check_winner():
            self.__move += 1
            inp = input()
            while not self.validate_input(inp):
                inp = input()
            self.make_move(inp)
            os.system("cls")
            self.show_board()
            if self.check_winner() == 1:
                print("Победил крестик")
                return 1
            if self.check_winner() == -1:
                print("Победил нолик")
                return -1
            if self.__move == 9:
                print("Ничья")
                return 0


if __name__ == "__main__":
    game = TicTac()
    game.start_game()
