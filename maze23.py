from collections import defaultdict
import sys

"""
The BFS search function to find the shortest path
"""
def BFS(graph,s):
    queue=[]
    queue.append(s)
    seen=set()
    seen.add(s)
    parent={s:None}
    while len(queue)>0:
        """
        The use of queue to implement BFS function
        """
        vertex=queue.pop(0)
        nodes=graph[vertex]
        for w in nodes:
            if w not in seen:
                temp=float(w)
                temq=float(vertex)
                p=int(temp)
                q=int(temq)
                """
                To judge whether we should go horizontally, vertically or diagonally
                """
                if p==q*2 or p==q-3:
                    queue.append(w)
                    seen.add(w)
                    parent[w]=vertex
    return parent

def test():
    filename = sys.argv[1] + '.txt'
    with open(filename) as f:
        # discard first line (column labels)
        f.readline()
        # process the remainder of the lines
        h=0
        w=0
        brr=[]
        """
        Read a file from command line
        """
        for line in f:
            # strip the newline at the end of the line
            line = line.split()
            for k in range(0,len(line)):
                brr.append(line[k])
            w=len(line)
            h+=1
        """
        To make sure the width and height of the two dimensional array
        """
        print("the width is "+str(w))
        print("the height is "+str(h))
        #some float operation
        factor=0.1
        for prefix in range(0,len(brr)):
            for suffix in range(prefix+1,len(brr)):
                if brr[suffix]==brr[prefix]:
                    temp=float(brr[suffix])
                    temp+=factor
                    brr[suffix]=str(temp)
                    factor+=0.1
            factor=0.1
        """
        Creat a two dimensional array to decide where to go
        """
        Matrix = [[0 for x in range(w)] for y in range(h)]
        index=0
        for m in range (0,w):
            for n in range(0,h):
                Matrix[m][n]=brr[index]
                index+=1
    g=defaultdict(list)
    """
    Creat a dictionary to store the numbers which are in the maze puzzle 
    """
    for p in range(0,w):
        for q in range(0,h):
            if p==0 and q==0:
                g[Matrix[p][q]].append(Matrix[p][q+1])
                g[Matrix[p][q]].append(Matrix[p+1][q+1])
                g[Matrix[p][q]].append(Matrix[p+1][q])
            elif p==0 and q==w-1:
                g[Matrix[p][q]].append(Matrix[p][q -1])
                g[Matrix[p][q]].append(Matrix[p + 1][q - 1])
                g[Matrix[p][q]].append(Matrix[p + 1][q])
            elif p==h-1 and q==0:
                g[Matrix[p][q]].append(Matrix[p-1][q])
                g[Matrix[p][q]].append(Matrix[p - 1][q + 1])
                g[Matrix[p][q]].append(Matrix[p][q+1])
            elif p==h-1 and q==w-1:
                g[Matrix[p][q]].append(Matrix[p][q-1])
                g[Matrix[p][q]].append(Matrix[p - 1][q - 1])
                g[Matrix[p][q]].append(Matrix[p-1][q])
            elif p==0:
                g[Matrix[p][q]].append(Matrix[p][q -1])
                g[Matrix[p][q]].append(Matrix[p - 1][q + 1])
                g[Matrix[p][q]].append(Matrix[p + 1][q])
                g[Matrix[p][q]].append(Matrix[p + 1][q+1])
                g[Matrix[p][q]].append(Matrix[p ][q + 1])
            elif q==0:
                g[Matrix[p][q]].append(Matrix[p-1][q])
                g[Matrix[p][q]].append(Matrix[p - 1][q + 1])
                g[Matrix[p][q]].append(Matrix[p][q+1])
                g[Matrix[p][q]].append(Matrix[p + 1][q + 1])
                g[Matrix[p][q]].append(Matrix[p+1][q])
            elif p==h-1:
                g[Matrix[p][q]].append(Matrix[p][q-1])
                g[Matrix[p][q]].append(Matrix[p - 1][q - 1])
                g[Matrix[p][q]].append(Matrix[p-1][q ])
                g[Matrix[p][q]].append(Matrix[p - 1][q + 1])
                g[Matrix[p][q]].append(Matrix[p ][q+1])
            elif q == w - 1:
                g[Matrix[p][q]].append(Matrix[p-1][q])
                g[Matrix[p][q]].append(Matrix[p - 1][q - 1])
                g[Matrix[p][q]].append(Matrix[p][q-1])
                g[Matrix[p][q]].append(Matrix[p + 1][q - 1])
                g[Matrix[p][q]].append(Matrix[p+1][q])
            else:
                g[Matrix[p][q]].append(Matrix[p - 1][q-1])
                g[Matrix[p][q]].append(Matrix[p - 1][q ])
                g[Matrix[p][q]].append(Matrix[p-1][q + 1])
                g[Matrix[p][q]].append(Matrix[p][q - 1])
                g[Matrix[p][q]].append(Matrix[p][q+1])
                g[Matrix[p][q]].append(Matrix[p+1][q - 1])
                g[Matrix[p][q]].append(Matrix[p + 1][q])
                g[Matrix[p][q]].append(Matrix[p + 1][q+1])
    """
    Make a function call to implement the solution
    we go from  start and stop at end
    """
    start=Matrix[0][0]
    end=Matrix[w-1][h-1]
    parent= BFS(g,start)
    hp = end
    arr = []
    while hp is not None:
        arr.append(hp)
        hp = parent[hp]
    for i in range(0, len(arr)):
        arr[i] = float(arr[i])
        arr[i] = int(arr[i])
    array=[]
    for n in range(len(arr)-1,-1,-1):
        array.append(arr[n])
    print(array)






if __name__ == '__main__':
    test()