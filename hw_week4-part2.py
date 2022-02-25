# # Part 2
# c：進貨成本、r：零售價格、n：需求量、probability：需求量機率、q：訂貨量 (介於 0 到 n 之間)

c = int(input("cost= "))
r = int(input("price= "))
n = int(input("demand= "))
# create an empty list
lst = []
# iterate till the range
for i in range(0, n + 1):
    probability = float(input())
    lst.append(probability)
    pi = lst
# print(pi)

maxprofit = 0

for q in range(n + 1):
# q 訂貨量落在 0 到 n 之間（包含 0 和 n）
    pn = 1
    profit = 0
    for j in range(q + 1):
    # n 需求量一定在 0 到 q 之間（包含 0 和 q）
        if j == q:
            profit += pn * (q * r - q * c)
        else:
            profit += pi[j] * (j * r - q * c)
            pn -= pi[j]
    # print(j, q, profit)
    if profit >= maxprofit:
        maxprofit = profit
    else:
        break

maxprofit = int(maxprofit)
q = int(q - 1)  
print(q, maxprofit)  










