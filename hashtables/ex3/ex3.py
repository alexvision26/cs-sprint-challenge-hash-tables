def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}
    result = []

    match = len(arrays)

    for x in arrays:
        for i in x:
            if i not in cache:
                cache[i] = 1
            else:
                cache[i] += 1

    ans = list(cache.items())

    for i in ans:
        if i[1] == match:
            result.append(i[0])


    return result


if __name__ == "__main__":
    arrays = [[1,2,3],[1,4,5],[1,6,7]]

    # arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    # arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    # arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
