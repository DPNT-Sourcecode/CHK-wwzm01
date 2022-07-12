def main(SKUs):
    product_amounts = find_total_values(SKUs)
    if product_amounts == -1:
        return -1
    total_cost = work_out_cost(product_amounts)
    return total_cost


def find_total_values(SKUs):
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
    return {"A":a, "B":b, "C":c, "D":d}
    
def work_out_cost(product_amounts):
    total_cost = int(product_amounts["A"]/3) * 130
    total_cost += product_amounts["A"] % 3 * 50
    total_cost += int(product_amounts["B"]/2) * 45
    total_cost += product_amounts["A"] % 2 * 30
    total_cost += product_amounts["C"] 
    total_cost += product_amounts["D"]
    return total_cost 
    

print(main("AAABCD")) #should output 195
print(main("AAAABCD")) #should output 245
print(main("AAABBCD")) #should output 210
print(main("AAAEBBCD")) #should output -1

