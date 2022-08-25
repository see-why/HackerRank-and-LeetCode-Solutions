# https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem?isFullScreen=true

averageX, averageY = [float(num) for num in input().split(" ")]

# Cost
CostX = 160 + 40*(averageX + averageX**2)
CostY = 128 + 40*(averageY + averageY**2)

print(round(CostX, 3))
print(round(CostY, 3))
