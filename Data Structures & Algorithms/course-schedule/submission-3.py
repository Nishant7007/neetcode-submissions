class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for i in range(numCourses)]
        for i, j in prerequisites:
            adj_list[i].append(j)
        visited = [False for i in range(numCourses)]
        
        def dfs(i, curr_path):
            if(i in curr_path):
                return False
            curr_path.add(i)
            for j in adj_list[i]:
                if not dfs(j, curr_path):
                    return False
            curr_path.remove(i)
            return True
        
        for i in range(numCourses):
            if(not visited[i]):
                visited[i] = True
                curr_path = set()
                res = dfs(i, curr_path)
                if(res==False):
                    return False
        return True
