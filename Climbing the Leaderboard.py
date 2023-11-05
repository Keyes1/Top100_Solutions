def climbingLeaderboard(scores, alice):
    scores = sorted(list(set(scores)))
    index = 0
    ranks= []
    n = len(scores)
    for i in alice:
        while (n > index and i >= scores[index]):
            index += 1
        ranks.append(n+1-index)
    return ranks
