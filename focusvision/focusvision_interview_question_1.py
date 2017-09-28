"""
What would be the output
""" 
def f(chars):
    for c in chars:
        yield c
    for elt in f(chars):
        for c in chars:
            yield elt + c

g = f('cat')
print g.next() # 'c'
print g.next() # 'cc'
print g.next() # 'ca'
print g.next() # 'ct' 
print g.next() #  
print g.next()
print g.next()
print g.next()
print g.next()
