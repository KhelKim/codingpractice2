import re


class DFS(object):
    def __init__(self, candis):
        self.candis = candis
        self.visit = set()
        self.combination = set()

    def __call__(self, depth=0):
        if depth == len(self.candis):
            target = "$".join(sorted(self.visit))
            if target not in self.combination:
                self.combination.add(target)
        else:
            for candi in self.candis[depth]:
                if candi in self.visit: continue
                else:
                    self.visit.add(candi)
                    self(depth+1)
                    self.visit.remove(candi)


def get_candis(user_id, banned_id):
    user_id_str = f'#{"##".join(user_id)}#'
    candis = []
    for hidden_id in banned_id:
        hidden_id = "#" + re.sub("\*", "[a-z0-9]", hidden_id) + "#"
        search_result = re.findall(hidden_id, user_id_str)
        candis.append(search_result)
    return candis


def solution(user_id, banned_id):
    candis = get_candis(user_id, banned_id)
    dfs = DFS(candis)
    dfs()
    return len(dfs.combination)


if __name__ == "__main__":
    user_id, banned_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]
    print(solution(user_id, banned_id))
