def main(SKUs):
    product_amounts = find_total_values(SKUs) #fn finds the amount of each product
    if product_amounts == -1: 
        return -1 #returns -1 if illegal input is found
    total_cost = work_out_cost(product_amounts) #fn works out the total checkout value of the items
    return total_cost


def find_total_values(SKUs):
    a = 0
    b = 0
    c = 0
    d = 0 
    e = 0 #create a running total of the total amount of each item in basket
    for s in SKUs:
        if s == "A":
            a += 1
        elif s == "B":
            b += 1
        elif s == "C":
            c += 1
        elif s == "D":
            d += 1  
        elif s == "E":
            e += 1   #here we add 1 on to the running total for each item in the basket
        else:
            return -1   #if an incorrect input has been entered return -1
    return {"A":a, "B":b, "C":c, "D":d, "E":e}
    
def work_out_cost(product_amounts):
    total_cost = 0
    if product_amounts["A"] >= 3: # if any special offers for A
        total_cost += int(product_amounts["A"]/3) * 130 #work out how many multiples of 3 for A which requires special price
        total_cost += product_amounts["A"] % 3 * 50 #also add any individual As on top
    else:
        total_cost += product_amounts["A"] * 50 #if less than 3 As, just work out individual 

    if product_amounts["B"] >= 2: # if any special offers for B
        total_cost += int(product_amounts["B"]/2) * 45 #work out how many multiples of 2 for B which requires special price
        total_cost += product_amounts["B"] % 2 * 30 #also add any individual Bs on top
    else:
        total_cost += product_amounts["B"] * 30 #if less than 2 Bs, just work out individual 
    total_cost += product_amounts["C"] * 20 
    total_cost += product_amounts["D"] * 15 # add any Cs and Ds
    return total_cost  
    

print(main("ABCD")) #should output 115
print(main("ABBBCD")) #should output 160
print(main("AAABCD")) #should output 195
print(main("AAAABCD")) #should output 245
print(main("AAABBCD")) #should output 210
print(main("AAAEBBCD")) #should output -1
