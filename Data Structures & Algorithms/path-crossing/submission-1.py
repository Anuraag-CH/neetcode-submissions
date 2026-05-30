class Solution:
    def isPathCrossing(self, path: str) -> bool:

        cur_pos_x = 0
        cur_pos_y = 0

        hash_set = set()
        hash_set.add((0,0))

        for s in path:
            if s == "E":
                cur_pos_x += 1
            elif s == "W":
                cur_pos_x -= 1
            elif s == "N":
                cur_pos_y += 1
            else:
                cur_pos_y -= 1

            if (cur_pos_x, cur_pos_y) in hash_set:
                return True
            hash_set.add((cur_pos_x, cur_pos_y))

        return False