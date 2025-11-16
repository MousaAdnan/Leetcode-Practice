
def maxProfit(prices):
    left = 0
    right = 1
    maxP = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            maxP = max(profit, maxP)
        else:
            prices[left] = prices[right]
        
        right += 1
    
    return maxP
            

def main():
    prices = [7,6,4,3,1]
    print(maxProfit(prices))
    #maxProfit(prices)

if __name__ == "__main__":
    main()