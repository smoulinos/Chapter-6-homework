def tuple((a,b), (c,d)):
    if (a*c) + (b*d) > 20:
        return "greater than 20"
    else:
        return "less than 20"

print(tuple[(1,4),(3,5)])