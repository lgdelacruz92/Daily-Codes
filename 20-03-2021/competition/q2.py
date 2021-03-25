import heapq
from typing import List
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
	
        classes_heap = [(passed_num / total - (passed_num + 1) / (total + 1),
                         passed_num, total) for (passed_num, total) in classes]
        heapq.heapify(classes_heap)

        for i in range(extraStudents):
          ratio_delta, passed, total = heapq.heappop(classes_heap)
          passed += 1
          total += 1

          entry = (passed / total - (passed + 1) / (total + 1), passed, total)
          heapq.heappush(classes_heap, entry)

        ratio_average = 0
        for entry in classes_heap:
          ratio_delta, passed, total = entry
          ratio_average = ratio_average + passed / total

        return(ratio_average/len(classes_heap))

classes = [[1,2],[3,5],[2,2]]
extraStudents = 2
s = Solution()
s.maxAverageRatio(classes, extraStudents)