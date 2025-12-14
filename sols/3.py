## Part1 

from pathlib import Path
from collections import deque
def func():

    file  = Path(__file__).parent.parent / 'tests' / "3.txt"
    ans = 0
    with open(file ) as f:
        line = f.readline()
       
    
        while line:
            m = 0
            sm = int(line[-2])
            for i in range(len(line) - 3 , -1 , -1):
                curr_digit = int(line[i])
                if  curr_digit>= m:
                    if m != 0:
                        sm = max (m , sm)
                    m = curr_digit
                
    
            ans += m * 10 + sm 
            line = f.readline()
    
    return ans




## part2 


def func2():
    file  = Path(__file__).parent.parent / 'tests' / "3.txt"
    ans = 0
    with open(file ) as f:
        line = f.readline()
       
    
        
        while line:
            line = line.strip()
            to_remove = len(line) - 12
            st = deque()

            for d in line:
                if d > "9" or d < "1":
                    continue
                while st and d > st[-1] and to_remove > 0:
                    to_remove-=1
                    st.pop()
                st.append(d)
            line = f.readline()
            if len(st) < 12:
                continue
           
            ans+= int("".join(list(st)[:12]))
           

    return ans

print(func2())






