l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
op=[]
def flat(l):
    for i in l:
        if isinstance(i, list):
            flat(i)
        else:
            op.append(i)
flat(l)
print(op)