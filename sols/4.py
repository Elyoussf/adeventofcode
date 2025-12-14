from pathlib import Path


# part 1 
def forklift():

    file  = Path(__file__).parent.parent / "tests" / "4.txt"

    with open(file)  as f:
        matrix = []
        while True:
            line = f.readline().strip().rstrip()
            if not line:
                break
            matrix.append([e == '@' for e in line])

        n = len(matrix)
        m = len(matrix[0])
        dirs = [(1,0),(-1,0),(-1,-1) , (1,1),(0,1),(0,-1),(-1,1),(1,-1)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if not matrix[i][j]:
                    continue
                guards = 0
                for dx ,dy in dirs:
                    if i +dx >=0 and i +dx < n and j + dy >= 0 and j + dy< m and matrix[i+dx][j+dy]:
                        guards+=1
            
                if guards < 4:
                    print((i,j))
                    ans+=1
        return ans
    

# part 2
def iteration(matrix):
    n = len(matrix)
    m = len(matrix[0])
    dirs = [(1,0),(-1,0),(-1,-1) , (1,1),(0,1),(0,-1),(-1,1),(1,-1)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if not matrix[i][j]:
                continue
            guards = 0
            for dx ,dy in dirs:
                if i +dx >=0 and i +dx < n and j + dy >= 0 and j + dy< m and matrix[i+dx][j+dy]:
                    guards+=1
        
            if guards < 4:
                print((i,j))
                matrix[i][j] = False
                ans+=1
    return matrix , ans

def forklift2():

    file  = Path(__file__).parent.parent / "tests" / "4.txt"

    with open(file)  as f:
        matrix = []
        while True:
            line = f.readline().strip().rstrip()
            if not line:
                break
            matrix.append([e == '@' for e in line])
        ans = 0
        matrix , curr  = iteration(matrix)
        while curr > 0:
            ans+= curr
            matrix , curr = iteration(matrix)
        ans+= curr
    return ans
print(forklift2())