    a = 10000
    b = 20000
    c= 40000
    d = 50000
    e = 60000
    def add(a,b):
        c=a+b
        return c
    def sub(a,b):
        c=a-b
        return c
    def mul(a,b):
        c=a*b
        return c
    def div(a,b):
        c=a//b
        return c
    print(div(mul(sub(add(a,b),c),d),e))
