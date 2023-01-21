class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def count_rotations(target):
            a_rots = b_rots = 0
            for i in range(len(tops)):
                if tops[i] != target and bottoms[i] != target:
                    return -1
                elif tops[i] != target:
                    a_rots += 1
                elif bottoms[i] != target:
                    b_rots += 1
            
            return min(a_rots, b_rots)

        ## Approach 2: 
        ## T.C = O(n)
        ## S.C = O(1)
        value = count_rotations(tops[0])
        if value == -1:
            return count_rotations(bottoms[0])
        return value

        ## Approach 1 : with hashmap
        ## T.C = O(n)
        ## S.C = O(n)
        from collections import defaultdict
        hm = defaultdict(int)
        target = -1

        for i in range(len(tops)):
            hm[tops[i]] += 1
            if hm[tops[i]] == len(tops):
                target = tops[i]
                break
            hm[bottoms[i]] += 1
            if hm[bottoms[i]] == len(tops):
                target = bottoms[i]
                break
        
        #print(hm, target)
        if target == -1:
            return target
        return count_rotations(target)

        




