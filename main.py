import unittest
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (
                (r, c) in visit
                or r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or heights[r][c] < prevHeight
            ):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res


class TestPacificAtlantic(unittest.TestCase):
    def setUp(self):
        self.solution = Solution().pacificAtlantic

    def test_empty_matrix(self):
        """Test with an empty matrix"""
        self.assertEqual(self.solution([]), [])

    def test_single_cell(self):
        """Test with a single cell matrix"""
        self.assertEqual(self.solution([[1]]), [[0, 0]])

    def test_single_row(self):
        """Test with a single row matrix"""
        self.assertEqual(sorted(self.solution([[1, 2, 2, 3, 5]])), sorted([[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]))

    def test_single_column(self):
        """Test with a single column matrix"""
        self.assertEqual(sorted(self.solution([[1], [2], [2], [3], [5]])), sorted([[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]))

    def test_increasing_heights(self):
        """Test with a matrix where heights are strictly increasing"""
        heights = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(sorted(self.solution(heights)), sorted([[0, 2], [1, 2], [2, 2], [2, 1], [2, 0]]))

    def test_decreasing_heights(self):
        """Test with a matrix where heights are strictly decreasing"""
        heights = [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ]
        self.assertEqual(sorted(self.solution(heights)), sorted([[0, 0], [0, 1], [0, 2], [1, 0], [2, 0]]))

    def test_equal_heights(self):
        """Test with a matrix where all heights are the same"""
        heights = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        self.assertEqual(sorted(self.solution(heights)), sorted([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]))

    def test_large_matrix(self):
        """Test with a large matrix to ensure performance"""
        heights = [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4]
        ]
        expected_output = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        self.assertEqual(sorted(self.solution(heights)), sorted(expected_output))

    def test_all_cells_flow(self):
        """Test with a matrix where all cells can flow to both oceans"""
        heights = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        expected_output = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
        self.assertEqual(sorted(self.solution(heights)), sorted(expected_output))

    def test_no_cells_flow(self):
        """Test with a matrix where no cells can flow to both oceans"""
        heights = [
            [10, 10, 10],
            [10, 1, 10],
            [10, 10, 10]
        ]
        expected_output = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]]
        self.assertEqual(sorted(self.solution(heights)), sorted(expected_output))

    def test_diagonal_increasing(self):
        """Test with a matrix where heights increase diagonally"""
        heights = [
            [1, 2, 3],
            [2, 3, 4],
            [3, 4, 5]
        ]
        expected_output = [[0, 2], [1, 2], [2, 2], [2, 1], [2, 0]]
        self.assertEqual(sorted(self.solution(heights)), sorted(expected_output))

    def test_diagonal_decreasing(self):
        """Test with a matrix where heights decrease diagonally"""
        heights = [
            [5, 4, 3],
            [4, 3, 2],
            [3, 2, 1]
        ]
        expected_output = [[0, 0], [0, 1], [0, 2], [1, 0], [2, 0]]
        self.assertEqual(sorted(self.solution(heights)), sorted(expected_output))

    def test_checkerboard_pattern(self):
        """Test with a checkerboard pattern matrix"""
        heights = [
            [1, 2, 1],
            [2, 1, 2],
            [1, 2, 1]
        ]
        expected_output = [[0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1]]
        self.assertEqual(sorted(self.solution(heights)), sorted(expected_output))


    def test_ridges_and_valleys(self):
        """Test with a matrix that has ridges and valleys"""
        heights = [
            [1, 3, 1, 3, 1],
            [2, 1, 2, 1, 2],
            [1, 3, 1, 3, 1],
            [2, 1, 2, 1, 2],
            [1, 3, 1, 3, 1]
        ]
        expected_output = [[0, 3], [0, 4], [1, 4], [3, 0], [4, 0], [4, 1]]
        self.assertEqual(sorted(self.solution(heights)), sorted(expected_output))

    def test_single_ocean_reachable(self):
        """Test with a matrix where cells can only flow to one ocean"""
        heights = [
            [5, 5, 5, 5],
            [5, 1, 1, 5],
            [5, 1, 1, 5],
            [5, 5, 5, 5]
        ]
        expected_output = [
            [0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 3], [2, 0], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3]
        ]
        self.assertEqual(sorted(self.solution(heights)), sorted(expected_output))

    def test_matrix_with_barriers(self):
        """Test with a matrix where some cells act as barriers"""
        heights = [
            [1, 2, 3, 4],
            [2, 3, 1, 5],
            [3, 1, 2, 6],
            [4, 5, 6, 7]
        ]
        expected_output = [
            [0, 3], [1, 3], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3]
        ]
        self.assertEqual(sorted(self.solution(heights)), sorted(expected_output))


if __name__ == '__main__':
    unittest.main()
