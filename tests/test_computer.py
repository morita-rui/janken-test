import unittest;
from unittest.mock import patch
from source.computer import computer_pon;

class Testplayer(unittest.TestCase):
    @patch("random.choice")
    def test_computer_pong(self, mock_choice):
        mock_choice.return_value = 'グー'
        self.assertEqual(computer_pon(), 'グー')
        
    @patch("random.choice")
    def test_computer_pont(self, mock_choice):
        mock_choice.return_value = 'チョキ'
        self.assertEqual(computer_pon(), 'チョキ')
    
    @patch("random.choice")
    def test_computer_ponp(self, mock_choice):
        mock_choice.return_value = 'パー'
        self.assertEqual(computer_pon(), 'パー')