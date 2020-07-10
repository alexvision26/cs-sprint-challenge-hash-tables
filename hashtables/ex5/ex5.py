# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    result = []
    cache = {}

    for idx, x in enumerate(files):
        new_val = x.split('/')
        new_val = new_val[len(new_val) - 1]
        if new_val not in cache:
            cache[new_val] = [x]
        else:
            cache[new_val].append(x)


    for i in queries:
        if i in cache:
            for x in cache[i]:
                result.append(x)

    # print(cache)
    # print(result)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/test/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
