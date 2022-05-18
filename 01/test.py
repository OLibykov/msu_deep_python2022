import unittest
import tictac


class TestTicTac(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_validate_input(self):
        game = tictac.TicTac()
        self.assertFalse(game.validate_input("biliberda"))
        self.assertFalse(game.validate_input("a"))
        self.assertFalse(game.validate_input("-1"))
        self.assertFalse(game.validate_input("9"))
        self.assertFalse(game.validate_input("100"))
        self.assertTrue(game.validate_input("0"))
        game.make_move(0)
        game.make_move(1)
        self.assertFalse(game.validate_input("0"))
        self.assertFalse(game.validate_input("1"))
        game.show_board()

    def test_all_valid_input(self):
        game = tictac.TicTac()
        self.assertTrue(game.validate_input("0"))
        self.assertTrue(game.validate_input("1"))
        self.assertTrue(game.validate_input("2"))
        self.assertTrue(game.validate_input("3"))
        self.assertTrue(game.validate_input("4"))
        self.assertTrue(game.validate_input("5"))
        self.assertTrue(game.validate_input("6"))
        self.assertTrue(game.validate_input("7"))
        self.assertTrue(game.validate_input("8"))

    def test_check_winner_diag(self):  # 2 теста на победу по диагонали
        game = tictac.TicTac()
        for i in range(9):
            game.make_move(i)
            tmp = game.check_winner()
            if i < 6:
                self.assertEqual(tmp, 0)
            else:
                self.assertEqual(tmp, 1)
                break
        game = tictac.TicTac()
        for i in [1, 0, 2, 4, 3, 8]:
            game.make_move(i)
            tmp = game.check_winner()
            if i != 8:
                self.assertEqual(tmp, 0)
            else:
                self.assertEqual(tmp, -1)
                break

    def test_check_winner_row(self):  # 3 теста на победу по горизонтали
        game = tictac.TicTac()
        for i in [0, 3, 1, 4, 2]:
            game.make_move(i)
            tmp = game.check_winner()
            if i != 2:
                self.assertEqual(tmp, 0)
            else:
                self.assertEqual(tmp, 1)
                break
        game = tictac.TicTac()
        for i in [0, 6, 1, 7, 5, 8]:
            game.make_move(i)
            tmp = game.check_winner()
            if i != 8:
                self.assertEqual(tmp, 0)
            else:
                self.assertEqual(tmp, -1)
                break
        game = tictac.TicTac()
        for i in [6, 0, 7, 2, 8]:
            game.make_move(i)
            tmp = game.check_winner()
            if i != 8:
                self.assertEqual(tmp, 0)
            else:
                self.assertEqual(tmp, 1)
                break

    def test_check_winner_col(self):  # 3 теста на победу по вертикали
        game = tictac.TicTac()
        for i in [0, 1, 3, 2, 6]:
            game.make_move(i)
            tmp = game.check_winner()
            if i != 6:
                self.assertEqual(tmp, 0)
            else:
                self.assertEqual(tmp, 1)
                break
        game = tictac.TicTac()
        for i in [0, 1, 2, 4, 5, 7]:
            game.make_move(i)
            tmp = game.check_winner()
            if i != 7:
                self.assertEqual(tmp, 0)
            else:
                self.assertEqual(tmp, -1)
                break
        game = tictac.TicTac()
        for i in [0, 2, 1, 5, 3, 8]:
            game.make_move(i)
            tmp = game.check_winner()
            if i != 8:
                self.assertEqual(tmp, 0)
            else:
                self.assertEqual(tmp, -1)
                break

    def test_check_winner_draw(self):
        game = tictac.TicTac()
        for i in [4, 0, 2, 6, 3, 5, 7, 1, 8]:
            game.make_move(i)
            self.assertEqual(game.check_winner(), 0)
        print("--------------------------------------")
        game.show_board()


if __name__ == "__main__":
    unittest.main()
