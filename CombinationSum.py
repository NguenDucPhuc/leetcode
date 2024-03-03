class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(start, target, path, result):
            if target == 0:
                result.append(path)
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                backtrack(i, target - candidates[i], path + [candidates[i]], result)
        
        result = []
        candidates.sort()
        backtrack(0, target, [], result)
        return result
