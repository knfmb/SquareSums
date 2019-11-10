def squaresum(n):
    if n <= 0:
        print ("Please enter a positive number.")
    else:
        sum = 0
        temp = 1
    while temp <= n:
        sum += temp**2
        temp += 1
    return sum