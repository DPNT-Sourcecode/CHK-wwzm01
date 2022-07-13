
def main(skus):
    product_prices = {"A":50,"B":30,"C":20,"D":15,"E":40,"F":10,"G":20,"H":10,"I":35,"J":60,"K":80,"L":90,
    "M":15,"N":40,"O":10,"P":50,"Q":30,"R":50,"S":30,"T":20,"U":40,"V":50,"W":20,"X":90,"Y":10,"Z":50}
    product_amounts = find_total_values(skus, product_prices) #fn finds the amount of each product
    if product_amounts == -1: 
        return -1 #returns -1 if illegal input is found
    # total_cost = work_out_cost(product_amounts) #fn works out the total checkout value of the items
    return total_cost


def find_total_values(skus, product_prices):

    product_amounts = {} #create a running total of the total amount of each item in basket
    for s in skus:
        if s in product_prices:
            if s in product_amounts:
                product_amounts[s] += 1
            else:
                product_amounts[s] = 1
        else:
            return -1   #if an incorrect input has been entered return -1
    for p in product_prices:
        if p not in product_amounts:
            product_amounts[p] = 0 #add all the products that have not been found yet with amount 0
    
    # here we need to apply all the buy and get free offers to remove items that aren't being charged


    return product_amounts
    

def buy_get_free(product, product_amounts, product_price, buy, get_free, y):
    if product==get_free:
        product_amounts[product] = (product_amounts[product] - int(product_amounts[product]/buy))


# def work_out_cost(product_amounts):
#     total_cost = 0
#     if product_amounts["A"] >= 5: # if any special offers for A
#         total_cost += int(product_amounts["A"]/5) * 200 #work out how many multiples of 3 for A which requires special price
#         product_amounts["A"] = product_amounts["A"] % 5
#         total_cost += special_offer_A(product_amounts)
#     else:
#         total_cost += special_offer_A(product_amounts)
#     if product_amounts["E"] >= 2: # if more than 2 Es
#         product_amounts["B"] = max(product_amounts["B"] - int(product_amounts["E"]/2) , 0) #subtract the amount of free Bs from total amount of Bs, but can't go below 0 Bs
#     if product_amounts["B"] >= 2: # if any special offers for B
#         total_cost += int(product_amounts["B"]/2) * 45 #work out how many multiples of 2 for B which requires special price
#         total_cost += product_amounts["B"] % 2 * 30 #also add any individual Bs on top
#     else:
#         total_cost += product_amounts["B"] * 30 #if less than 2 Bs, just work out individual 
#     total_cost += product_amounts["C"] * 20 
#     total_cost += product_amounts["D"] * 15 
#     total_cost += product_amounts["E"] * 40 # add any Cs, Ds, Es
#     if product_amounts["F"] >= 3:
#         product_amounts["F"] = (product_amounts["F"] - int(product_amounts["F"]/3))
#     total_cost += product_amounts["F"] * 10
#     return total_cost  
    


def special_offer_for(product, product_amounts, product_price, special_offer, special_price, special_offer_2=None, special_price_2=None):
    cost = 0

    #do we need to apply special_offer?
    if product_amounts[product] >= special_offer: 
        cost += int(product_amounts[product]/special_offer) * special_price #work out how many multiples of special_offer for product which requires special price
        product_amounts[product] = product_amounts[product] % special_offer #find remaining products after special_offer applied

        #do we have special_offer_2?
        if special_offer_2: 
            cost += special_offer_for(product, product_amounts, product_price, special_offer_2, special_price_2)

        #no special_offer_2, just add extra products 
        else:
            cost += product_amounts[product] % special_offer * product_price #also add any individual As on top

    #not applying special_offer
    else:

        #do we have special_offer_2?
        if special_offer_2:
            cost += special_offer_for(product, product_amounts, product_price, special_offer_2, special_price_2)

        #no special_offer_2, just add extra products 
        else:
            cost += product_amounts[product] * product_price #if less than 3 As, just work out individual 
    return cost

print(special_offer_for("A", {"A":2}, 50, 5, 200, 3, 130))

# print(main("AAAA"))
# print(main("AAAAA"))
# print(main("AAAAAAAA"))
# print(main("AAAAAAAAAAA"))
# print(main("FFFFFFFF"))
# print(main("ABCD")) #should output 115
# print(main("ABBBCD")) #should output 160
# print(main("AAABCD")) #should output 195
# print(main("AAAABCD")) #should output 245
# print(main("AAABBCD")) #should output 210
# print(main("AAABBECD")) #should output 250
# print(main("AAABBBECD")) #should output 280
# print(main("AAABBBEEEEEEEEECD")) #should output 525
# print(main("AAAEBBZCD")) #should output -1

