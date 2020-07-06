def nth_element(array, will):
    "arrayの[0,will)を大きいほうからwill(1-indexted)番目までの要素にする"
    will -= 1
    n = len(array)
    left = 0
    right = n-1
    while right > left:
        i = left-1
        j = right
        v = array[right]
        while True:
            i += 1
            j -= 1
            while array[i]>v:i+=1
            while array[j]<v:j-=1
            if i>=j:break
            array[i],array[j] = array[j],array[i]
        array[i],array[right] = array[right],array[i]
        if i == will:break
        if i > will:
            right = i-1
        else:
            left = i+1
    return array
