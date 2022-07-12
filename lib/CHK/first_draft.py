def main(SKUs):
    a = 0
    b = 0
    c = 0
    d = 0 #create a running total of the total amount of each item in basket
    for s in SKUs:
        if s == "A":
            a += 1
        elif s == "B":
            b += 1
        elif s == "C":
            c += 1
        elif s == "D":
            d += 1   #here we add 1 on to the running total for each item in the basket
        else:
            return -1   #if an incorrect input has been entered return -1


