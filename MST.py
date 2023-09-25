"""
Author: Jin Huang

Implement Prims' algorithm.

Input: adjancency matrix;

Output: a list of tuples, wherein each tuple
represents an edge of the MST as (v1, v2, weight)
"""
import sys

def outputMST(parent, vertices, G):
    result = tuple()
    temp = list(result)
    for i in range(1, vertices):
        thisEdge = parent[i], i, G[i][parent[i]]
        temp.append(thisEdge)
    result = temp
    return result


def minKey(key, mstSet, vertices):
    min = sys.maxsize 
    for vertex in range(vertices):
        if key[vertex] < min and mstSet[vertex] == False:
            min = key[vertex]
            minVertexIndex = vertex
    return minVertexIndex 

def Prims(G):
    vertices = len(G)
    key = [sys.maxsize] * vertices
    parent = [None] * vertices 
    key[0] = 0 
    mstSet = [False] * vertices 
    parent[0] = -1 
    for count in range(vertices):
        thisVertex = minKey(key, mstSet, vertices)
        mstSet[thisVertex] = True 
        for neighbor in range(vertices):
            if G[thisVertex][neighbor]>0 and mstSet[neighbor] == False and key[neighbor]>G[thisVertex][neighbor]:
                key[neighbor] = G[thisVertex][neighbor]
                parent[neighbor] = thisVertex 
    return outputMST(parent, vertices, G)
