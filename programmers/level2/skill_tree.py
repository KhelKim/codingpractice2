from collections import deque


def proper_skill_tree(skill_queue, skill_set, skills):
    for skill in skills:
        if skill in skill_set:
            if skill == skill_queue[0]:
                skill_queue.popleft()
            else:
                return False
    return True


def solution(skill, skill_trees):
    skill_list = list(skill)
    skill_set = set(skill_list)

    count = 0
    for skills in skill_trees:
        skill_queue = deque(skill_list)
        if proper_skill_tree(skill_queue, skill_set, skills):
            count += 1
    return count


if __name__ == "__main__":
    skill, skill_trees = "CBD", ["BACDE", "CBADF", "AECB", "BDA"]
    print(solution(skill, skill_trees))
