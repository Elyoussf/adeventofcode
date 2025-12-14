from pathlib import Path


def sol():
    path = Path(__file__)
    curr_dir = path.parent
    file  = curr_dir.parent / "tests" / "2_part1.txt"
    ans = 0

    with open(file) as f:
        line = f.readline()
        ranges = [[int(l.split('-')[0]) , int (l.split('-')[1])]  for l in line.split(",")]

    for r in ranges:
        start,end = r[0],r[1]
        
        for id in range(start , end+1):
            str_id = str(id)
            l = len(str_id)
           
            for i in range(l//2):
                if l // (i+1) >2:
                    continue
                
                if str_id == str_id[:(i+1)] * (l // (i+1)):
                    print(id)
                    ans += id
                    break
    return ans


res = sol()
print(res)