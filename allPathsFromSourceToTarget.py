'''Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.  
The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.'''

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result, graph_len = [], len(graph) - 1
        que = deque([[0]])
        
        while que:
            cur_path = que.popleft()
            
            if cur_path[-1] == graph_len:
                result.append(cur_path)
                continue

            for child in graph[cur_path[-1]]:
                que.append(cur_path + [child])
        
        return result
