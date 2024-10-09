from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        y = 0
        while y < len(students): 
            if students[0] == sandwiches[0]:
                 students.pop(0)
                 sandwiches.pop(0)
                 y = 0 
            else: 
                 temp = students.pop(0)
                 students.append(temp)
                 y+=1
        return len(students)     

#students = [1,1,0,0]
#sandwiches = [0,1,0,1]
students = [1,1]
sandwiches = [1,1]

#students = [x for x in input("Students: ").split()]
#sandwiches = [x for x in input("Sandwiches: ").split()]

solution = Solution()
res = solution.countStudents(students, sandwiches)
print(res)