def solve(m, n):
    tileArea = 2*1
    boardArea = m*n
    return boardArea / tileArea

if __name__ == "__main__":
    m, n = map(int, raw_input().split(" "))
    print (solve(m,n))