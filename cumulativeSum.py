def ruiseki(n, A):
    "長さnの数列Aの累積和を返す　ただし[0] = 0"
    res = [0]*(n+1)
    for i in range(n):
        res[i+1] = res[i] + A[i]
    return res
