initial_map = [["_" for i in range(8)] for j in range(8)]
for i in [3,4]:
    for j in [1,3,4,6]:
        initial_map[i][j]=initial_map[j][i]="X"
    for j in [0,7]:
        initial_map[i][j]=initial_map[j][i]="O"
for i,j in [(1,2),(1,5),(2,6),(5,6)]:
    initial_map[i][j]=initial_map[j][i]="O"

def map_print(x,y,map):
    for j in range(8):
        for i in range(8):
            print map[i][j] if (i,j)!=(x,y) else "G",
        print "\n",

def find_variants(x,y,map):
    def try_variant(x,y,map):
        return [(x,y)] if x>=0 and x<8 and y>=0 and y<8 and map[x][y]!="X" else []
    res = []
    res += try_variant(x-2,y-1,map)
    res += try_variant(x-1,y-2,map)
    res += try_variant(x-2,y+1,map)
    res += try_variant(x-1,y+2,map)
    res += try_variant(x+2,y-1,map)
    res += try_variant(x+1,y-2,map)
    res += try_variant(x+2,y+1,map)
    res += try_variant(x+1,y+2,map)
    return res
    
def find_solution(x,y,map,history):
    Os = sum([sum([map[i][j]=="O" for i in range(8)]) for j in range(8)])
    if  Os == 1 and map[x][y] == "O":
        if  y == 0:
            return True
        else:
            return False

    v = find_variants(x,y,map)
    if  not v:
        return None
    for (x1,y1) in v:
        map1 = [[map[i][j] for j in range(8)] for i in range(8)]
        map1[x][y] = "X"
        res = find_solution(x1,y1,map1,[h for h in history]+[(x1,y1)])
        if  res == True:
            print history
            map_print(x1,y1,map1)
            return True
    return None

find_solution(1,7,initial_map,[(1,7)])