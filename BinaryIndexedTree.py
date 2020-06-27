class BinaryIndexedTree:
    def __init__(self,n,default = 0):
        self.s = [default]*(n+1)
        self.n = n
    # idxは1-indexted
    def add(self,val,idx):
        while idx < self.n+1:
            self.s[idx] = self.s[idx] + val
            idx += idx&(-idx)
        return
    
    def get(self,idx):
        res = 0
        while idx > 0:
            res = res + self.s[idx]
            idx -= idx&(-idx)
        return res
