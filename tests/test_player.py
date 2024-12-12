import unittest;
from unittest.mock import patch
from source.player import player_pon;

class Testplayer(unittest.TestCase):
    @patch('builtins.input', return_value='1')
    def test_player_pong(self, mock_input):
            result = player_pon()
            self.assertEqual(result, 'グー')
    
    @patch('builtins.input', return_value='2')
    def test_player_pont(self, mock_input):
            result = player_pon()
            self.assertEqual(result, 'チョキ')
            
    @patch('builtins.input', return_value='3')
    def test_player_pontp(self, mock_input):
            result = player_pon()
            self.assertEqual(result, 'パー')
    
    @patch('builtins.input', side_effect = ['0', '4', '1'])
    def test_player_pon(self, mock_input):
            result = player_pon()
            self.assertEqual(result, 'グー')
            
            
if __name__ == '__main__':
    unittest.main()
