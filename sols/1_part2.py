from pathlib import Path


def __solution__():
    current_dir = Path(__file__)
    path = current_dir.parent.parent / "tests" / "2.txt"
    curr = 50
    ans = 0
    with open(path) as f:
        while True:
            move = f.readline()
            if (len(move)) > 0:
                dir = move[0]
                sign = 1 if dir == "R" else -1
                l = int(move[1:])
                
                if sign > 0 :
                    ans += (curr +l)//100
                else:
                    diff = curr - l
                    if diff <= 0:
                        ans+=(abs(diff)+100)//100
                curr = (curr + sign * l)%100

                
                        
                

            else:
                break
    return ans
print((-5)%100)
print(__solution__())