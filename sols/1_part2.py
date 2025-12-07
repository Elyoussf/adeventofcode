from pathlib import Path
from typing import Tuple

def solve_file(path: Path) -> int:
  
    n = 100
    curr = 50

    part2 = 0

    with open(path, "r") as f:
        for line in f:
            move = line.strip()
            if not move:
                continue
            direction = move[0]
            dist = int(move[1:])

            if direction == "R":
                needed = (n - curr) % n
            else:  # 'L'
                needed = curr % n

            # treat needed==0 as needed==n (the next time you hit zero is after a full n steps)
            if needed == 0:
                needed = n

            # how many clicks during this move land on 0?
            if dist < needed:
                during_hits = 0
            else:
                during_hits = 1 + (dist - needed) // n

            part2 += during_hits

            # update current position
            delta = dist if direction == "R" else -dist
            curr = (curr + delta) % n

           

    return part2





print(solve_file(Path(__file__).parent.parent / "tests"/"1_part12.txt"))