class BinaryIndexedTree:
    def __init__(self, n, default=0):
        "nの長さのBITをdefaultを初期値として構築する"
        self.s = [default]*(n+1)
        self.n = n
    # idxは0-indexted

    def add(self, idx, val):
        "idx(0-indexted)の値にvalを加える"
        idx += 1
        while idx < self.n+1:
            self.s[idx] = self.s[idx] + val
            idx += idx & (-idx)
        return

    def get(self, idx):
        "idx(0-indexted)以下の要素の和を求める"
        idx += 1
        res = 0
        while idx > 0:
            res = res + self.s[idx]
            idx -= idx & (-idx)
        return res
