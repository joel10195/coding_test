def solution(price, money, count):
    result = 0
    n_price = 0
    
    for i in range(1, count+1):
        n_price = price * i
        result = result + n_price
        
    if money - result >= 0:
        return 0
    else:
        return -(money - result)

    