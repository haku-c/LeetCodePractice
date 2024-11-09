def minimumDeletions(self, s: str) -> int:
    # bcount = 0
    # n = len(s)
    # # opt[i] holds the min number of deletions to balance from 0 to i in the string
    # opt = [0] * n
    # for i in range(n):
    #     if s[i] == "a":
    #         # we can either delete all prior bs to create a block of as, or balance the prior string and delete this a
    #         opt[i] = min(bcount, opt[i-1] + 1)
    #     else:
    #         # we can either delete all prior bs so this current b is the first b or balance the prior string
    #         opt[i] = min(opt[i-1], bcount)
    #         bcount += 1
    # return opt[len(s)-1]

    # you can also decrease memory space by holding values in 2 variables instead of tracking the entire array
    bcount = 0
    n = len(s)
    curr = 0
    past = 0
    for i in range(n):
        if s[i] == "a":
            curr = min(bcount, past + 1)
            past = curr
        else:
            bcount += 1
    return curr
