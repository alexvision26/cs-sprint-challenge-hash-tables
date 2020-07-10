def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    test= []
    cache = {}

    for idx, x in enumerate(a):
        cache[x] = x

    # print(cache)

    ans = list(cache.items())
    print(ans)

    for i in ans:
        if i[1] < 0:
            curr = abs(i[1])
            if curr in cache:
                result.append(curr)


    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
