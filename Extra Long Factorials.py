def extraLongFactorials(n):
    # Write your code here
    f = 1
    for i in range(2, n+1):
        f *= i
    print(f)
