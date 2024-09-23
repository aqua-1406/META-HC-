import math
import random
from collections import defaultdict
from multiprocessing import Pool

def gcd(a, b):
    return math.gcd(a, b)

def h1(dx, dy):
    g = gcd(dx, dy)
    return (dx // g, dy // g) if g != 0 else (dx, dy)

def h2(points, itr=500):
    n = len(points)
    mpp = 0
    
    for _ in range(itr):
        i, j = random.sample(range(n), 2)
        p1, p2 = points[i], points[j]
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        slope = h1(dx, dy)
        line_count = defaultdict(int)
        for p in points:
            dx = p[0] - p1[0]
            dy = p[1] - p1[1]
            if dx == 0 and dy == 0:
                continue 
            normalized_slope = h1(dx, dy)
            line_count[normalized_slope] += 1

        mpp = max(mpp, max(line_count.values(), default=0) + 1)
        if mpp > n // 2:
            break
    
    return n - mpp
def tests(data, idx, case_num):
    N = int(data[idx])
    idx += 1
    points = []
    for i in range(N):
        X, Y = map(int, data[idx].split())
        points.append((X, Y))
        idx += 1

    moves_needed = h2(points)
    return f"Case #{case_num}: {moves_needed}"

def main(input_file, output_file):
    with open(input_file, 'r') as f:
        data = f.read().splitlines()

    T = int(data[0])
    idx = 1

    
    chunks = []
    case_num = 1
    for t in range(T):
        N = int(data[idx])
        chunk = (data, idx, case_num)
        chunks.append(chunk)
        idx += N + 1
        case_num += 1
    with Pool() as pool:
        results = pool.starmap(tests, chunks)

    with open(output_file, 'w') as f:
        f.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main(' ', ' ')
