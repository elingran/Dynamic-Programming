import sys

sys.setrecursionlimit(100000000)
            
def g(x, cache):
    if x in cache:
        return cache[x]
    else:
        if x < cache["k"]:
            cache[x] = 0.0
            return cache[x]
        elif x == cache["k"]:
            cache[x] = cache["p"] ** cache["k"]
            return cache[x]
        else:   
            cache[x] = g(x-1, cache) + cache["p"] ** cache["k"] * (1- cache["p"]) * (1 - g(x - cache["k"] - 1, cache))
            return cache[x]
        

def main_kattis():
    cache = {}
    n = int(sys.stdin.readline())
    k = int(sys.stdin.readline())
    p = float(sys.stdin.readline())
    cache["k"] = k
    cache["p"] = p
    return print(g(n, cache))

if __name__ == '__main__':
    main_kattis()
