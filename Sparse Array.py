def matchingStrings(stringList, queries):
    arr = []
    for query in queries:
        arr.append(stringList.count(query))
    return arr
