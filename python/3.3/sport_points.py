def solve(score):
    while score > 0:
        for x in [3,6,7,8]:
            if score % x == 0:
                score %= x
        if score == 0:
            break
        if score % 2 == 0:
            if score > 8:
                score -= 8
            else:
                score -= 6
        else:
            if score > 7:
                score -= 7
            else:
                score -= 3
    if score == 0:
        print 'valid'
    else:
        print 'invalid'

solve(35)
solve(2)
