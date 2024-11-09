def makeEqual(self, words):
    """
    :type words: List[str]
    :rtype: bool
    """
    # arr = [0] * 26
    # for w in words:
    #     for c in w:
    #         arr[ord(c) - ord("a")] += 1
    # n = len(words)
    # for entry in arr:
    #     if entry % n != 0:
    #         return False
    # return True

    # better solution doesn't always have 26 entries to check
    s = {}
    for word in words:
        for c in word:
            if c not in s:
                s[c] = 0
            s[c] += 1
    for a, count in s.items():
        if count % len(words) != 0:
            return False
    return True
