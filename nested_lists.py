# Nested lists
# https://www.hackerrank.com/challenges/nested-list/problem
lista = [[input(), float(input())] for i in range(int(input()))] # Create the list with input
scorelist = sorted(list(set([lista[i][1] for i in range(len(lista))]))) # The set is to ignore duplicates
second_lowest = []
for i in range(len(lista)):
    if lista[i][1] == scorelist[1]: # Check who has the second lowest grade
        second_lowest.append(lista[i][0])
second_lowest.sort()
for i in range(len(second_lowest)):
    print(second_lowest[i])