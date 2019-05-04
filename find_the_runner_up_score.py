# Find the Runner Up Score!
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

n = int(input("How many scores will you enter?: "))  # n numbers will be introduced next
ar = [int(x) for x in input("Enter the scores separated by a space: ").split()]  # creates a list with n integers
sorted_ar = sorted(ar)  # By default, the sorting is ascending, so the max score will have index [-1]
while sorted_ar.count(max(ar)) >= 1:  # We need to check if the max score is not duplicated
    sorted_ar.pop()  # This removes the last item of the list, that's why whe sorted it
runner_up_score = sorted_ar[-1]
print(runner_up_score)