# # # Part 1
# # c：進貨成本、r：零售價格、n：需求量、probability：需求量機率、q：訂貨量

c = int(input("cost= "))
r = int(input("price= "))
n = int(input("demand= "))
q = int(input("order= "))
# create an empty list
lst = []
# iterate till the range
for i in range(0, n + 1):
    probability = float(input())
    lst.append(probability)
    pi = lst
print(pi)

profit = 0
pn = 1

for j in range(0, q):
    profit += pi[j] * (j * r - q * c)
    # print(j, profit)
    pn -= pi[j]
    # print(pn)

profit += pn * (q * r - q * c)
profit = int(profit)  
print("expected profit=", profit)  