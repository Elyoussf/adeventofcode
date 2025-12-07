from pathlib import Path


def __solution__():
    current_dir = Path(__file__)
    path = current_dir.parent.parent / "tests" / "1part12.txt"
    curr = 50
    ans = 0
    
    with open(path) as f:
        while True:
            move = f.readline()
            if (len(move)) > 0:
                dir = move[0]
                sign = 1 if dir == "R" else -1
                l = int(move[1:])
                curr = (curr + sign * l + 100)% 100
                if curr == 0:
                    ans+=1
            else:
                break
    return ans
print(__solution__())