import unittest
from source.janken_judge import judge

class TestJudge(unittest.TestCase):
    def test_judge(self):
        pattern = [
            ('グー', 'グー'),
            ('グー', 'チョキ'),
            ('グー', 'パー'),
            ('チョキ', 'チョキ'),
            ('チョキ', 'グー'),
            ('チョキ', 'パー'),
            ('パー', 'パー'),
            ('パー', 'グー'),
            ('パー', 'チョキ'),
        ]

        for computer_hand, player_hand in pattern:
            with self.subTest(f'{computer_hand} vs {player_hand}'):
                result = judge(computer_hand, player_hand)
                print(f'computer_hand: {computer_hand}, player_hand: {player_hand}, result: {result}')

