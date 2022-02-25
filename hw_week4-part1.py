# # # Part 1
# # c：進貨成本、r：零售價格、n：需求量、probability：需求量機率、q：訂貨量

cost = int(input("cost= "))
price = int(input("price= "))
demand = int(input("demand= "))
order_quantity = int(input("order quantity= "))
# create an empty list
probs = []
# iterate till the range
for i in range(0, demand + 1):
    probability = float(input())
    probs.append(probability)
    
print(probs)

profit = 0
pn = 1

for j in range(0, order_quantity):
    profit += probs[j] * (j * price - order_quantity * cost)
    # print(j, profit)
    pn -= probs[j]
    # print(pn)

profit += pn * (order_quantity * price - order_quantity * cost)
profit = int(profit)  
print("expected profit=", profit)  