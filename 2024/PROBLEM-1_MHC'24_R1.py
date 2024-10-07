def solve(ip, op):
    with open(ip, 'r') as infile:
        data = infile.readlines()
    
    T = int(data[0].strip())
    results = []

    index = 1
    for case_num in range(1, T + 1):
        N = int(data[index].strip())
        index += 1

        A = []
        B = []

        for i in range(1, N + 1):
            a, b = map(int, data[index].strip().split())
            A.append(a)
            B.append(b)
            index += 1
        mlb = 0
        mub = float('inf')

        for i in range(1, N + 1):
            a_i = A[i - 1]
            b_i = B[i - 1]
            lower_bound = i / b_i if b_i > 0 else float('inf')
            upper_bound = i / a_i if a_i > 0 else float('inf')
            mlb = max(mlb, lower_bound)
            mub = min(mub, upper_bound)

        if mlb <= mub:
            result = f"{mlb:.6f}"
        else:
            result = "-1"
        
        results.append(f"Case #{case_num}: {result}")
    
    with open(op, 'w') as outfile:
        outfile.write("\n".join(results) + "\n")

ip = ''
op = ''
solve(ip, op)