def makeEqual(self, words):
    """
    :type words: List[str]
    :rtype: bool
    """
    arr = [0] * 26
    for w in words:
        for c in w:
            arr[ord(c) - ord("a")] += 1
    n = len(words)
    for entry in arr:
        if entry % n != 0:
            return False
    return True
