def get_cycle(n):
    results = []
    remainders = [1]
    val = 1
    while True:
        result = (val*10)//n
        remainder = (val*10)%n
        results.append(result)
        if remainder == 0 or remainder in remainders:
            break
        remainders.append(remainder)
        val = remainder
    return ("0.{}".format(''.join(map(str, results))), 0 if remainder == 0 else
            len(remainders) - remainders.index(remainder))

print(max(range(1,1000), key = lambda x: get_cycle(x)[1]))
