from unittest import TestCase, mock
from game_map import GameMap
from itertools import chain, cycle


class TestGameMap(TestCase):
    def setUp(self):
        self.game_map = GameMap(5, 5)

    def test_rows(self):
        self.assertEqual(5, self.game_map.rows, "行数不正确")

    def test_cols(self):
        self.assertEqual(5, self.game_map.cols, "列数不正确")

    @mock.patch('random.random', new=mock.Mock(side_effect=chain(cycle([0.2, 0.4, 0.6, 0.8, 1]))))
    def test_reset(self):
        self.game_map.reset()
        for i in range(0, 5):
            self.assertEqual(1, self.game_map.get(i, 0), "第一列的值为1")
            self.assertEqual(1, self.game_map.get(i, 1), "第二列的值为1")
            for j in range(2, 5):
                self.assertEqual(0, self.game_map.get(i, j), "第三、四、五列的值为0")

    def test_get_set(self):
        self.game_map.set(0, 0, 0)
        self.assertEqual(0, self.game_map.get(0, 0), "通过set修改后值为0")
        self.game_map.set(0, 0, 1)
        self.assertEqual(1, self.game_map.get(0, 0), "通过set修改后值为1")

    def test_get_neighbor_count(self):
        self.game_map.cells = [[1] * 5] * 5
        neighbor_count = [[8] * 5] * 5
        for i in range(0, 5):
            for j in range(0, 5):
                self.assertEqual(neighbor_count[i][j], self.game_map.get_neighbor_count(i, j), "周围有8个活的")
        self.game_map.cells = [[0] * 5] * 5
        neighbor_count = [[0] * 5] * 5
        for i in range(0, 5):
            for j in range(0, 5):
                self.assertEqual(neighbor_count[i][j], self.game_map.get_neighbor_count(i, j), "周围有0个活的")

    @mock.patch('game_map.GameMap.get_neighbor_count', new=mock.Mock(return_value=8))
    def test_get_neighbor_count_map(self):
        neighbor_count = [[8] * 5] * 5
        self.assertEqual(neighbor_count, self.game_map.get_neighbor_count_map())

    def test_set_map(self):
        self.game_map.set_map([[1] * 5] * 5)
        self.assertEqual([[1] * 5] * 5, self.game_map.cells)
        self.game_map.set_map([[0] * 5] * 5)
        self.assertEqual([[0] * 5] * 5, self.game_map.cells)
        self.assertRaises(TypeError, self.game_map.set_map, {(0, 0, 0, 0, 0) * 5})
        self.assertRaises(TypeError, self.game_map.set_map, [['1'] * 5] * 5)
        self.assertRaises(AssertionError, self.game_map.set_map, [[1] * 4] * 4)
        self.assertRaises(AssertionError, self.game_map.set_map, [[2] * 5] * 5)

    def test_print_map(self):
        self.game_map.cells = [
            [1, 1, 1, 0, 0],
            [0, 0, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0]
        ]
        with mock.patch('builtins.print') as mock1:
            self.game_map.print_map()
            mock1.assert_has_calls([
                mock.call('1 1 1 0 0'),
                mock.call('0 0 1 1 1'),
                mock.call('1 1 1 1 1'),
                mock.call('0 0 0 0 0'),
                mock.call('0 0 1 0 0')
            ])
