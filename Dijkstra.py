# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 15:50:46 2023

@author: livin
"""

def sum_edges(adj_matrix):
    w_sum = 0
    l = len(adj_matrix)
    for i in range(l):
        for j in range(i,l):
            w_sum += adj_matrix[i][j]
    return w_sum

def dijkstra(adj_matrix, source, dest):
    shortest = [0 for i in range(len(adj_matrix))]
    selected = [source]
    l = len(adj_matrix)
    #Base case from source
    inf = float('inf')
    min_sel = inf
    for i in range(l):
        if(i==source):
            shortest[source] = 0 #adj_matrix[source][source]
        else:
            if(adj_matrix[source][i]==0):
                shortest[i] = inf
            else:
                shortest[i] = adj_matrix[source][i]
                if(shortest[i] < min_sel):
                    min_sel = shortest[i]
                    ind = i
                
    if(source==dest):
        return 0, [source]
    # dijkstra's in Play
    selected.append(ind) 
    while(ind!=dest):
        #print('ind',ind)
        for i in range(l):
            if i not in selected:
                if(adj_matrix[ind][i]!=0):
                    #Check if distance needs to be updated
                    if((adj_matrix[ind][i] + min_sel) < shortest[i]):
                        shortest[i] = adj_matrix[ind][i] + min_sel
        temp_min = float('inf')
        #print('shortest:',shortest)
        #print('selected:',selected)
        
        for j in range(l):
            if j not in selected:
                if(shortest[j] < temp_min):
                    temp_min = shortest[j]
                    ind = j
        min_sel = temp_min
        selected.append(ind)
        
    path = [dest]
    while path[-1] != source:
        current_node = path[-1]
        for i in range(l):
            if adj_matrix[current_node][i] != 0 and shortest[current_node] - adj_matrix[current_node][i] == shortest[i]:
                path.append(i)
                break
    
    return shortest[dest], path[::-1]
                            
#Finding odd degree vertices in graph

def get_odd(adj_matrix):
    degrees = [0 for i in range(len(adj_matrix))]
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):
                if(adj_matrix[i][j]!=0):
                    degrees[i]+=1
                
    #print(degrees)
    odds = [i for i in range(len(degrees)) if degrees[i]%2!=0]
    #print('odds are:',odds)
    return odds

#Function to generate unique pairs
def gen_pairs(odds):
    pairs = []
    for i in range(len(odds)-1):
        pairs.append([])
        for j in range(i+1,len(odds)):
            pairs[i].append([odds[i],odds[j]])
        
    #print('pairs are:',pairs)
    #print('\n')
    return pairs


#Final Compiled Function
def Chinese_Postman(adj_matrix):
    odds = get_odd(adj_matrix)
    if(len(odds)==0):
        return sum_edges(adj_matrix)
    pairs = gen_pairs(odds)
    l = (len(pairs)+1)//2
    
    pairings_sum = []
    
    def get_pairs(pairs, done = [], final = []):
        
        if(pairs[0][0][0] not in done):
            done.append(pairs[0][0][0])
            
            for i in pairs[0]:
                f = final[:]
                val = done[:]
                if(i[1] not in val):
                    f.append(i)
                else:
                    continue
                
                if(len(f)==l):
                    pairings_sum.append(f)
                    return 
                else:
                    val.append(i[1])
                    get_pairs(pairs[1:],val, f)
                    
        else:
            get_pairs(pairs[1:], done, final)
            
    get_pairs(pairs)
    min_sums = []
    
    for i in pairings_sum:
        s = 0
        for j in range(len(i)):
            temp, spp = dijkstra(adj_matrix, i[j][0], i[j][1])
            s += temp
        min_sums.append(s)
    
    added_dis = min(min_sums)
    chinese_dis = added_dis + sum_edges(adj_matrix)
    return chinese_dis

"""
adj_matrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
         [4, 0, 8, 0, 0, 0, 0, 11, 0],
         [0, 8, 0, 7, 0, 4, 0, 0, 2], 
         [0, 0, 7, 0, 9, 14, 0, 0, 0], 
         [0, 0, 0, 9, 0, 10, 0, 0, 0], 
         [0, 0, 4, 0, 10, 0, 2, 0, 0], 
         [0, 0, 0, 14, 0, 2, 0, 1, 6], 
         [8, 11, 0, 0, 0, 0, 1, 0, 7], 
         [0, 0, 2, 0, 0, 0, 6, 7, 0] ];
"""
def start(adj_matrix):
    print('Chinese Postman Distance is:',Chinese_Postman(adj_matrix))
