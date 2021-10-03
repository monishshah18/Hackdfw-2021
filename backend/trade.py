# input: 
# 1) pool members and their distribution - [10,20,30,40,10]
# 2) total cap of the pool - 100
# base price - 20

# dynamic inputs
# 1) supply or demand
# 2) quantity


def buy(demand, supply, total_cap, base_price):
    demand_req = int(input("Input the amount of water in gallon you want to buy: "))
    if supply == 0:
        # calculate the % of the total cap the current supply_req is
        per_change = (demand_req/total_cap) * 100
        
        # add the demand req to the current demand
        demand += demand_req

        # increase the base price
        base_price = base_price + ((base_price*per_change)/100)
    elif supply>0:
        # if supply is greater than 0 then initially reduce the supply to zero and then and only then you can cahnge the base price
        if demand_req > supply:
            # get demand to 0
            
            demand_req = demand_req-supply
            supply = 0

            # now we have to decrease the base price
            per_change = (demand_req/total_cap) * 100
        
            # add the supply req to the current supply
            demand += demand_req

            # increase the base price
            base_price = base_price + base_price*per_change

        elif demand_req <= demand:
            # no change in base price as demand is still more, just reduced the demand
            demand = demand - demand_req
    return demand, supply, base_price

def sell(demand, supply, total_cap, base_price):
    supply_req = int(input("Input the amount of water in gallons you want to sell: "))
    if demand == 0:
        # calculate the % of the total cap the current supply_req is
        per_change = (supply_req/total_cap) * 100
        
        # add the supply req to the supply
        supply += supply_req

        # reduce the base price
        base_price = base_price - ((base_price*per_change)/100)

    elif demand>0:
        # if demand is greater than 0 then initially reduce the demand to zero and then and on;y then you can cahnge the base price
        if supply_req > demand:
            # get demand to 0
            
            supply_req = supply_req-demand
            demand = 0

            # now we have to decrease the base price
            per_change = (supply_req/total_cap) * 100
        
            # add the supply req to the current supply
            supply += supply_req

            # reduce the base price
            base_price = base_price - ((base_price*per_change)/100)

        elif supply_req <= demand:
            # no change in base price as demand is still more, just reduced the demand
            demand = demand - supply_req
    return demand, supply, base_price

def trade(pool, distribution, total_cap, base):
    # considering we are the x [0] person in the pool
    # demand and supply variables

    demand = 0
    supply = 0
    # we can buy or sell
    # lets take input from user
    while True:
        print("buy: 0, sell: 1")
        i = int(input())
        demand, supply, base = buy(demand, supply, total_cap, base) if i==0 else sell(demand, supply, total_cap, base)
        print("demand, supply, base ", demand, supply, base)

trade([], [], 10000, 20)