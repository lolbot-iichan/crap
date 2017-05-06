steps = {}
steps[1] = 0

def count_steps(n, debug=False):
    k = 0
    search = n
    while not search in steps:
        if  debug:
            print search
        k += 1
        search = search/2 if search%2==0 else 3*search+1
    steps[n] = steps[search] + k
    return steps[n]

for i in range(1,10000000):
    print i, '\t', count_steps(i)
