import unittest
from project import play_hangman, get_hangman_figure, word_categories
from unittest.mock import patch
import io

class TestHangmanGame(unittest.TestCase):

    def test_get_hangman_figure(self):
        self.assertEqual(get_hangman_figure(6).strip(), r"""
        +---+
        |   |
            |
            |
            |
            |
        =========""".strip())
        self.assertEqual(get_hangman_figure(5).strip(), r"""
        +---+
        |   |
        O   |
            |
            |
            |
        =========""".strip())
        # ... Add assertions for the remaining hangman figures (4 to 0)

    @patch('builtins.input', side_effect=['a', 'p', 'l', 'e'])  # Example with 4 inputs
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_play_hangman_win(self, mock_stdout, mock_input):
        category = 'fruits'
        with patch('project.random.choice', return_value='apple'):
            play_hangman(category)
            output = mock_stdout.getvalue()
            self.assertIn('Incorrect attempts remaining:', output)
            self.assertIn('Congratulations! You won!', output)

    @patch('builtins.input', side_effect=['x', 'y', 'z', 'q', 'w', 'r'])  # Example with 6 inputs
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_play_hangman_loss(self, mock_stdout, mock_input):
        category = 'fruits'  # You can use any category here
        with patch('project.random.choice', return_value='apple'):
            play_hangman(category)
            output = mock_stdout.getvalue()
            self.assertIn('Incorrect attempts remaining:', output)
            self.assertIn('You ran out of attempts.', output)  # Check for loss message

if __name__ == "__main__":
    unittest.main()




