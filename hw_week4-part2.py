# # Part 2
# c：進貨成本、r：零售價格、n：需求量、probability：需求量機率、quantity：訂貨量 (介於 0 到 n 之間)

cost = int(input("cost= "))
price = int(input("price= "))
demand = int(input("demand= "))
# create an empty list
probs = []
# iterate till the range
for i in range(0, demand + 1):
    probability = float(input())
    probs.append(probability)

# print(probs)

maxprofit = 0
max_quantity = -1
for quantity in range(demand + 1):
# quantity 訂貨量落在 0 到 demand 之間（包含 0 和 demand）
    pn = 1
    profit = 0
    for j in range(quantity + 1):
    # demand 需求量一定在 0 到 quantity 之間（包含 0 和 quantity）
        if j == quantity:
            profit += pn * (quantity * price - quantity * cost)
        else:
            profit += probs[j] * (j * price - quantity * cost)
            pn -= probs[j]
    # print(j, quantity, profit)
    
    """ 
    題目說道：
    如果有數個訂貨量會導致一模一樣的預期利潤（是預期利潤一樣，不是無條件捨去之後一樣！），
    請用比較小的那一個當最佳訂貨量。 所以這裡要用 > 而不是 >=
    """
    if profit > maxprofit:
        maxprofit = profit
        max_quantity = quantity
    
maxprofit = int(maxprofit)
# quantity = int(quantity - 1)  // redundant 
print(max_quantity, maxprofit)  










