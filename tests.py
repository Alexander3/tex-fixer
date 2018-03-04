from io import StringIO
from unittest import TestCase
from unittest.mock import patch, MagicMock
from os.path import join

from correct_endings import add_hard_spaces

with open(join('example', '3_rozwiniecie_fixed.tex')) as f:
    desired_output = f.read()

write_file_mock = StringIO()
write_file_mock.close = MagicMock()


@patch('correct_endings.glob', return_value=[''])  # open is anyway mocked
@patch('correct_endings.open', side_effect=[open(join('example', '3_rozwiniecie.tex')), write_file_mock])
class ReplacingTestCase(TestCase):
    def test_full_usage(self, open_mock, *args):
        add_hard_spaces('')
        self.assertMultiLineEqual(write_file_mock.getvalue(), desired_output)
        self.assertEqual(open_mock.call_count, 2)
