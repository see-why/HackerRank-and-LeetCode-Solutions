# https://www.hackerrank.com/challenges/luck-balance/problem?isFullScreen=true

def luckBalance(k, contests):
    # Write your code here
    luck_importance_array = [item[0] for item in contests if item[1]==1]
    luck_value_array = [item[0] for item in contests]
    
    luck_sum = sum(luck_value_array)
    
    luck_value_array.sort()
    luck_importance_array.sort()

    for i in range(len(luck_importance_array)-k):
        luck_sum -= 2 * luck_importance_array[i]
    
    return luck_sum
