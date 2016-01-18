def KtoF(k):
    c = KtoC(k)
    return CtoF(c)

def FtoK(f):
    c = FtoC(f)
    return CtoK(c)

def KtoC(k):
    return k - 273.15

def CtoK(c):
    return c + 273.15

def FtoC(f):
    return (f-32) * (5/9.0)

def CtoF(c):
    return (c * (9/5.0)) + 32
