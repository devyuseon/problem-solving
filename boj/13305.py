n = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))
result = length[0] * price[0]
min_price = price[0]

for i in range(1, len(price) - 1):
    if price[i] < min_price:
        min_price = price[i]
    result += length[i] * min_price
        
print(result)