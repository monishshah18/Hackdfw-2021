from flask import Flask
from flask import request
from flask_ngrok import run_with_ngrok
from flask import g
import json
# input
# data points (gal of water per farmer per unit area) [(s1, g1), (s2,g2), (s3,g3), (s4,g4), (s5,g5), (s6,g6), (s7,g7), (s8,g8), (s9,g9)]
# weights [(2,4), (1, 3, 5), (2, 6), (1, 5, 7), (2, 4, 6, 8), (4, 8), (7, 4, 9), (6, 8)]


def permute(nums):
    def dfs(nums, psize, path, res):
        # print(path,res, psize)
        if len(path) == psize:
            res.append(path)
            return
        for i in range(len(nums)):
            dfs(nums[:i]+nums[i+1:], psize, path + [nums[i]], res)
    res = []
    dfs(nums, len(nums), [], res)
    return res


def main(data_points, weights):
    # first find the average of data points
    average_data = 0
    # total water = Surface water + Ground water
    received_water = []
    for i in data_points:
        tsum = i[0] + i[1]
        average_data += tsum
        received_water.append(tsum)

    average_data /= len(data_points)

    # nw we need to create the need of each point
    need = []

    for i in range(len(received_water)):
        need.append(received_water[i] - average_data)
    print(need)
    print(average_data)
    # now for each data_point we need to get water from the one that have more water
    # find all the negative nodes
    negative_nodes = []
    positive_nodes = []
    for i in range(len(need)):
        if need[i] < 0:
            negative_nodes.append(i)
        else:
            positive_nodes.append(i)
    print(positive_nodes)
    print(negative_nodes)
    # now for all the positive nodes find distance of it from the all the negative nodes
    # or from a negative node find the distance to all the positive nodes

    # que = []
    dic = {}
    for i in negative_nodes:
        dic[i] = {}

    for i in negative_nodes:
        print("started node", i, "...")
        to_explore = [i]
        visited = set()
        level = 1
        que = []

        while to_explore:
            print("to_explore > ", to_explore)
            x = to_explore.pop(0)
            connections = weights[x]
            visited.add(x)
            for j in connections:
                if j not in visited:
                    if need[j] > 0:
                        dic[i][j] = level
                    que.append(j)

            if to_explore == []:
                # refill
                if que == []:
                    break
                to_explore = list(set(que))
                que = []
                level += 1

    print(dic)

    prms = permute(positive_nodes)
    print(prms)

    # now reverse the dict

    for k in dic:
        for subkeys in dic[k]:
            pass


def get_cost(prm, need, dic):
    cost = 0
    for i in range(len(prm)):
        # get curr need
        curr = need[prm[i]]

        # reduce curr until it gets to zero by subtracting(here adding) the values of the need
        # so just add the
        # satisfy all the prm
        for j in dic[prm[i]]:
            # print(j, need[j])
            if need[j] == 0:
                continue
            tempcost = dic[prm[i]][j]
            remaining = curr + need[j]
            # print("rem", remaining)

            if remaining > 0:
                # we have to add more so continue in the loop

                # we add the tempcost * remaining to cost
                cost += (tempcost*remaining)

                # update the current curr
                curr = remaining
                need[j] = 0

            elif remaining <= 0:
                # the current element succesfully finished curr
                # update the cost
                tc = remaining - need[j]
                need[j] = remaining
                curr = 0
                cost += (tempcost*tc)
            # print("--->", cost)
            if curr == 0:
                # completed need of this element now move to another
                # print(">>>>>")
                break

    # print(cost)
    return cost


def main2(data_points, weights):
    # first find the average of data points
    average_data = 0
    # total water = Surface water + Ground water
    received_water = []
    for i in data_points:
        tsum = i[0] + i[1]
        average_data += tsum
        received_water.append(tsum)

    average_data /= len(data_points)

    # nw we need to create the need of each point
    need = []

    for i in range(len(received_water)):
        need.append(received_water[i] - average_data)
    # print(need)
    # print(average_data)
    # now for each data_point we need to get water from the one that have more water
    # find all the negative nodes
    negative_nodes = []
    positive_nodes = []
    for i in range(len(need)):
        if need[i] < 0:
            negative_nodes.append(i)
        else:
            positive_nodes.append(i)
    # print(positive_nodes)
    # print(negative_nodes)
    # now for all the positive nodes find distance of it from the all the negative nodes
    # or from a negative node find the distance to all the positive nodes

    # que = []
    dic = {}
    for i in positive_nodes:
        dic[i] = {}

    for i in positive_nodes:
        # print("started node", i, "...")
        to_explore = [i]
        visited = set()
        level = 1
        que = []

        while to_explore:
            # print("to_explore > ",to_explore)
            x = to_explore.pop(0)
            connections = weights[x]
            visited.add(x)
            for j in connections:
                if j not in visited:
                    if need[j] < 0:
                        dic[i][j] = level
                    que.append(j)

            if to_explore == []:
                # refill
                if que == []:
                    break
                to_explore = list(set(que))
                que = []
                level += 1

    # print(dic)

    prms = permute(positive_nodes)
    # print(prms)

    # get_cost(prms[0], need[:], dic)
    mini = 10**19
    m_prm = None
    for i in range(len(prms)):
        cst = get_cost(prms[i], need[:], dic)
        if mini > cst:
            mini = cst
            m_prm = prms[i]

    print("--"*20)
    print(mini, m_prm)
    return [mini, m_prm]

# input:
# 1) pool members and their distribution - [10,20,30,40,10]
# 2) total cap of the pool - 100
# base price - 20

# dynamic inputs
# 1) supply or demand
# 2) quantity


demand = 0
supply = 0
total_cap, base = 1000, 100


def buy(demand, supply, total_cap, base_price, demand_req):
    # demand_req = int(input("Input the amount of water in gallon you want to buy: "))
    if supply == 0:
        # calculate the % of the total cap the current supply_req is
        per_change = (demand_req/total_cap) * 100

        # add the demand req to the current demand
        demand += demand_req

        # increase the base price
        base_price = base_price + ((base_price*per_change)/100)
    elif supply > 0:
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


def sell(demand, supply, total_cap, base_price, supply_req):
    # supply_req = int(input("Input the amount of water in gallons you want to sell: "))
    if demand == 0:
        # calculate the % of the total cap the current supply_req is
        per_change = (supply_req/total_cap) * 100

        # add the supply req to the supply
        supply += supply_req

        # reduce the base price
        base_price = base_price - ((base_price*per_change)/100)

    elif demand > 0:
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


app = Flask(__name__)
demand = 0
supply = 0
total_cap = 1000
base = 20
run_with_ngrok(app)


@app.route('/buy_api', methods=['GET'])
def buy_api():
    global demand
    global supply
    global total_cap
    global base
    buyamt = int(request.args['buyamt'])
    demand, supply, base = buy(demand, supply, total_cap, base, buyamt)
    return json.dumps({'demand': demand, 'supply': supply, 'base': base})


@app.route('/sell_api', methods=['GET'])
def sell_api():
    global demand
    global supply
    global total_cap
    global base
    sellamt = int(request.args['sellamt'])
    demand, supply, base = sell(demand, supply, total_cap, base, sellamt)
    return json.dumps({'demand': demand, 'supply': supply, 'base': base})


@app.route('/distribute', methods=['POST'])
def distribute():
    # Use form body here for both json1 and json2
    json1 = '{"0":[1,3],"1":[0,2,4],"2":[1,5],"3":[0,4,6],"4":[1,3,5,7],"5":[2,4,8],"6":[3, 7],"7":[6,4,8],"8":[5,7]}'
    json2 = '{"0":[19,1],"1":[24,1],"2":[17,1],"3":[4,1],"4":[9,1],"5":[17,1],"6":[10,1],"7":[8,1],"8":[18,1]}'
    json1_d = json.loads(json1)
    json2_d = json.loads(json2)
    weights = [i for i in json1_d.values()]  # Json
    data_points = [i for i in json2_d.values()]  # Json
    Solution = main2(data_points, weights)
    return json.dumps({'Minimum': Solution[0], 'Permutation': Solution[1]})


app.run()
