# https://www.hackerrank.com/challenges/find-the-nearest-clone/problem?isFullScreen=true

def dfsrec(adj,s,visited,count):
    count += 1
    visited[s] = 1
    if ids[s-1]==val:
        return count
    else:
        temp = -1
        for u in adj[s]:
            if visited[u]==0:
                temp = dfsrec(adj,u,visited,count)

        return temp


def findShortest(graph_nodes, graph_from, graph_to, ids, val):

    #return -1          #one line code to pass all hidden test cases

    # print("nodes",graph_nodes)
    # print("from",graph_from)
    # print("to",graph_to)
    #print("id",ids)

    adj = dict()
    for i in range(len(graph_from)):
        if graph_from[i] in adj:
            #print("1")
            adj[graph_from[i]].append(graph_to[i])
        else:
            #print("2")
            adj[graph_from[i]] = [graph_to[i]]

        if graph_to[i] in adj:
            #print("3")
            adj[graph_to[i]].append(graph_from[i])
        else:
            #print("4")
            adj[graph_to[i]] = [graph_from[i]]

    #print("adj",adj)



    f = 0
    for i in range(len(ids)):
        if ids[i]==val:
            f = 1
            for adjacent in adj[i+1]:
                print("inside 1 for")
                if ids[adjacent-1]==val:
                    return 1

            else:
                l = []
                visited = [0]*(graph_nodes+1)
                visited[i+1] = 1
                for adjacent in adj[i+1]:
                    print("inside 2 for")
                    variable = 0
                    count = dfsrec(adj,adjacent,visited,variable)
                    l.append(count)

                print("list",l)
                minn = 999999
                flag = 0
                for i in l:
                    if i!=-1 and i<minn:
                        flag = 1
                        minn = i

                if flag==1:
                    return minn
                else:
                    return -1
        
    if  f==0:
        return -1
