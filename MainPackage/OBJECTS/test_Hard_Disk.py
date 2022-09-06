from unittest import TestCase, mock
from unittest.mock import patch
from Hard_Disk import Hard_disk


class TestHard_disk(TestCase):
    def setUp(self):
        self.hd = Hard_disk(100)

    def test_used_space(self):
        self.assertEqual(0, self.hd.used_space())

    def test_free_space_valid(self):
        with patch('Hard_Disk.Hard_disk.used_space') as mock_used_space:
            mock_used_space.return_value = 0
            self.assertEqual(100, self.hd.free_space())
            mock_used_space.return_value = 99.9
            self.assertEqual(0.1, round(self.hd.free_space(), 1))

