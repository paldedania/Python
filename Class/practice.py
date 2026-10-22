def func(a):
    a+=1
    if a ==5:
        return a
    func(a)
    return a

print(func(1))