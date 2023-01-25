class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        if node1 == node2:
            return node1
        
        index_visited_1 = {}
        i = node1
        dist = 0
        while i not in index_visited_1 and i >=0:
            index_visited_1[i] = dist
            
            i = edges[i]
            dist += 1 
        
        index_visited_2 = {}
        i = node2
        dist = 0
        while i not in index_visited_2 and i >=0:
            index_visited_2[i] = dist
            
            i = edges[i]
            dist += 1
            
        common_nodes = set(list(index_visited_1.keys())).intersection(set(list(index_visited_2.keys())))
        min_dist = float(inf)
        res = -1
        
        for iterator in common_nodes:
            curr_dist = max(index_visited_1[iterator], index_visited_2[iterator])
            if curr_dist < min_dist:
                res = iterator
                min_dist = curr_dist
            elif curr_dist == min_dist:
                if iterator < res:
                    res = iterator
        return res