"""
Tuples are immutable ordered collections of arbitrarty objects
Because they are immutable they can be used as dictionary keys
Similar to lists except they are immutable
"""
t = () # empty tuple
print t

t = ('a', 'b', 1, 2, 3.0, "4");
print t
print len(t) # number of items in the tuple

print t[1]
print t[0:3] # first three items
print t[3:] # fourth item to the end

t2 = ('x', 'x', 'y', 'z')
print t + t2 # concatenate two tuples, makes a new tuble with all items in it

print t2 * 3 # repeat 3 times, makes a new tuple that has t2 in it three times

#iterate items in a tuple
for i in t2:
	print i

print 'y' in t2 #true
print 'A' in t2 #false

print [x * 2 for x in t2] #comprehension makes tuple by doubling the items in t2

print t.index("4") # returns the index (zero based) of "4" in t

print t2.count('x') #counts how many times 'x' is in t2

t3 = (1, 2, 3, ('a', 'b', 'c', ('D', 'E', 'F'))) # nested tuples!
print t3
print len(t3)
print t3[0]
print t3[3]
print t3[3][3]
