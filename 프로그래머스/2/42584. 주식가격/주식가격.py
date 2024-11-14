def solution(prices):
    answer = [0] * len(prices)
    st = []

    for i, price in enumerate(prices):
        for j in range(i+1, len(prices)):
            if price <= prices[j]:
                answer[i] += 1
                is_fall = True
            else:
                answer[i] = j - i
                break

    return answer