class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for i in range(numCourses)]
        for i, j in prerequisites:
            adj_list[i].append(j)
        
        def dfs(i, visited):
            if(visited[i]==True):
                return False
            visited[i]=True
            for j in adj_list[i]:
                if not dfs(j, visited):
                    return False
            visited[i]=False
            return True
        
        for i in range(numCourses):
            visited = [False for i in range(numCourses)]
            res = dfs(i, visited)
            if(res==False):
                return False
        return True