def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    cache = {}
    answer = ()

    for x in range(len(weights)):
        res = limit - weights[x]
        if res in cache:
            answer = (x, cache[res])
        cache[weights[x]] = x

    if len(answer) == 2:
        return answer
    else:
        return None



w = [4, 6, 10, 15, 16]

print(get_indices_of_item_weights(w, 5, 21))