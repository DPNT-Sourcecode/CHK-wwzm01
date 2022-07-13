

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    #catologue of product prices
    product_prices = {"A":50,"B":30,"C":20,"D":15,"E":40,"F":10,"G":20,"H":10,"I":35,"J":60,"K":80,"L":90,
    "M":15,"N":40,"O":10,"P":50,"Q":30,"R":50,"S":20,"T":20,"U":40,"V":50,"W":20,"X":17,"Y":20,"Z":21}

    #fn finds the amount of each product
    product_amounts = find_total_values(skus, product_prices) 

    #returns -1 if illegal input is found
    if product_amounts == -1: 
        return -1 

    #fn works out the total checkout value of the items
    total_cost = work_out_cost(product_amounts, product_prices) 
    return total_cost


def find_total_values(skus, product_prices):

    #create a running total of the total amount of each item in basket
    product_amounts = {} 
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
    product_amounts = buy_get_free('E', product_amounts, 2, 'B')
    product_amounts = buy_get_free('F', product_amounts, 2, 'F')
    product_amounts = buy_get_free('N', product_amounts, 3, 'M')
    product_amounts = buy_get_free('R', product_amounts, 3, 'Q')
    product_amounts = buy_get_free('U', product_amounts, 3, 'U')

    return product_amounts
    

def buy_get_free(product, product_amounts, buy, get_free):
    #do we get the same product free as we bought?
    if product==get_free:

        #does the offer apply to the amount
        if product_amounts[product] >= buy+1:
            #subtract the free amount
            product_amounts[product] = (product_amounts[product] - int(product_amounts[product]/(buy+1)))

    else:
        #free product different from bought product
        #subtract free amount from other product
        product_amounts[get_free] = max(product_amounts[get_free] - int(product_amounts[product]/buy) , 0)
    return product_amounts


def work_out_cost(product_amounts, product_prices):
    total_cost = 0
    # here we total up the special offers first 
    total_cost += special_offer_for("A", product_amounts, product_prices["A"], 5, 200, 3, 130)
    total_cost += special_offer_for("B", product_amounts, product_prices["B"], 2, 45)
    total_cost += special_offer_for("H", product_amounts, product_prices["H"], 10, 80, 5, 45)
    total_cost += special_offer_for("K", product_amounts, product_prices["K"], 2, 150)
    total_cost += special_offer_for("P", product_amounts, product_prices["P"], 5, 200)
    total_cost += special_offer_for("Q", product_amounts, product_prices["Q"], 3, 80)
    total_cost += special_offer_for("V", product_amounts, product_prices["V"], 3, 130, 2, 90)
    total_cost += special_offer_for_multiple(product_amounts, product_prices, 3, 45)
    product_done = 'ABHKPQV'

    # then we can simple add up the totals of the remaining products
    for p in product_amounts:
        if p not in product_done:
            total_cost += product_amounts[p] * product_prices[p] 
    return total_cost

def special_offer_for_multiple(product_amounts, product_prices, multiple, price):
    cost = 0
    #find out total amount of products in special offer
    total_amount = product_amounts['S'] + product_amounts['T'] + product_amounts['X'] + product_amounts['Y'] + product_amounts['Z']

    #does special offer apply?
    if total_amount >= multiple:

        #find out how many multiples
        multiple_amount = int(total_amount/multiple)

        #work out cost when deal applied
        cost += multiple_amount * price
        amount_to_subtract = multiple_amount * multiple

        #now we need to subtract multiple_amount items from the products in the product_amounts dict, in order of highest cost first
        if amount_to_subtract >= product_amounts['Z']:
            amount_to_subtract -= product_amounts['Z']
            product_amounts['Z'] = 0
            if amount_to_subtract >= product_amounts['S']:
                amount_to_subtract -= product_amounts['S']
                product_amounts['S'] = 0
                if amount_to_subtract >= product_amounts['T']:
                    amount_to_subtract -= product_amounts['T']
                    product_amounts['T'] = 0
                    if amount_to_subtract >= product_amounts['Y']:
                        amount_to_subtract -= product_amounts['Y']
                        product_amounts['Y'] = 0
                        if amount_to_subtract >= product_amounts['X']:
                            amount_to_subtract -= product_amounts['X']
                            product_amounts['X'] = 0
                        else:
                            product_amounts['X'] -= amount_to_subtract
                    else:
                        product_amounts['Y'] -= amount_to_subtract
                else:
                    product_amounts['T'] -= amount_to_subtract
            else:
                product_amounts['S'] -= amount_to_subtract
        else:
            product_amounts['Z'] -= amount_to_subtract

    return cost






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
