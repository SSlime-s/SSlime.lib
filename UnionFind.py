class UnionFind:
    def __init__(self, n):
        '木の初期化をする'
        self.p = [-1] * n
        self.rank = [1]*n
        self.size = [1]*n
    def find(self, x):
        'x の親を返す'
        if self.p[x] == -1:
            return x
        else:
            self.p[x] = self.find(self.p[x])
            return self.p[x]

    def unite(self, x, y):
        'rankの低い親を高い方のの親にする'
        if not self.same(x,y):
            x = self.find(x)
            y = self.find(y)
            if self.rank[x] > self.rank[y]:
                x,y = y,x
            elif self.rank[x] == self.rank[y]:
                self.rank[y] += 1
            self.p[x] = y
            self.size[y] += self.size[x]
            return True
        else:
            return False

    def same(self, x, y):
        return self.find(x) == self.find(y)
