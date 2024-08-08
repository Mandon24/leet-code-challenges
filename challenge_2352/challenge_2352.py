class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        col_list = []

        for idx1, row in enumerate(grid):
            for idx2, col in enumerate(row):
                if idx2 >= len(col_list):
                    col_list.append([])
                col_list[idx2].append(col)

        pair_tracker = 0
        for r in grid:
            if r in col_list:
                no_occurrences = col_list.count(r)
                pair_tracker += no_occurrences

        return pair_tracker

    # more optimal solution:
        # rows = defaultdict(int)
        # n = len(grid)
        # for r in grid:
        #     rows[tuple(r)] += 1
        
        # ans = 0
        # for i in range(n):
        #     c = [j[i] for j in grid]
        #     ans += rows[tuple(c)]
        # return ans
