# input 
# data points (gal of water per farmer per unit area) [(s1, g1), (s2,g2), (s3,g3), (s4,g4), (s5,g5), (s6,g6), (s7,g7), (s8,g8), (s9,g9)]
# weights [(2,4), (1, 3, 5), (2, 6), (1, 5, 7), (2, 4, 6, 8), (4, 8), (7, 4, 9), (6, 8)]
# 
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
            print("to_explore > ",to_explore)
            x = to_explore.pop(0)
            connections = weights[x]
            visited.add(x)
            for j in connections:
                if j not in visited:
                    if need[j] > 0:
                        dic[i][j] = level
                    que.append(j)
        
            if to_explore == []:
                #refill
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
        #get curr need
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
                cost+=(tempcost*remaining)

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
                #refill
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
    


weights = [ list(i) for i in [(1,3), (0, 2, 4), (1, 5), (0, 4, 6), (1, 3, 5, 7), (2, 4, 8), (3, 7), (6, 4, 8), (5, 7)]]
data_points = [[19,1], [24,1], [17,1], [4,1], [9,1], [17,1], [10,1], [8,1], [18, 1]]
# main(data_points, weights)
main2(data_points, weights)