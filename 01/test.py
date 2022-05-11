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
        self.assertTrue(game.validate_input("0"))
        game.make_move(0)
        game.make_move(1)
        self.assertFalse(game.validate_input("0"))
        self.assertFalse(game.validate_input("1"))
        game.show_board()

    def test_check_winner_diag(self):
        game = tictac.TicTac()
        for i in range(9):
            game.make_move(i)
            tmp = game.check_winner()
            if i < 6:
                self.assertEqual(tmp, 0)
            else:
                self.assertEqual(tmp, 1)
                break
        print("--------------------------------------")
        game.show_board()
        game = tictac.TicTac()
        for i in [1, 0, 2, 4, 3, 8]:
            game.make_move(i)
            tmp = game.check_winner()
            if i != 8:
                self.assertEqual(tmp, 0)
            else:
                self.assertEqual(tmp, -1)
                break
        print("--------------------------------------")
        game.show_board()

    def test_check_winner_row(self):
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

    def test_check_winner_col(self):
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

    def test_check_winner_draw(self):
        game = tictac.TicTac()
        for i in [4, 0, 2, 6, 3, 5, 7, 1, 8]:
            game.make_move(i)
            self.assertEqual(game.check_winner(), 0)
        print("--------------------------------------")
        game.show_board()


if __name__ == "__main__":
    unittest.main()
