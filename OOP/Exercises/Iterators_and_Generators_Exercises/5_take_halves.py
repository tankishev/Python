def solution():
    def integers():
        i = 0
        while True:
            i += 1
            yield i

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        pass

    return (take, halves, integers)
