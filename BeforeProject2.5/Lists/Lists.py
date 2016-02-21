"""
Lists - ordered, accepts different types items, mutable, grows as needed
"""
mylist = [1, "2", 3.0]
print mylist

print 1 in mylist # True
print 99 in mylist # False
print 3.0 in mylist # True
print 3 in mylist # True
print "2" in mylist # True
print 2 in mylist # False

#iterate the items in a list
for i in mylist:
	print i
	print i * 2 # for the string we get "22"

print mylist.index("2") # prints 1

print len(mylist) # prints the length, which is 3
print mylist[1] # 0-based indexing
mylist =  mylist + ["new", "items"] # + appends a list to a list!
print mylist

print mylist[:2] # new list from start up to but not including 3rd item
print mylist[1:3] # new list from item 1 up to but not including 4th item
print mylist[3:] # new list from item 3 to end
print mylist[-1] # last item
print mylist[-2:] # second to last item to end

mylist.pop(2) #delete the third item
print mylist

mylist.insert(2, -99) # insert in third spot
print mylist

mylist.append(24) # add 24 to the end of the list

mylist.sort() # sorts items in the list ascneding
print mylist

mylist.reverse() # reverses list
print mylist



print range(4) # creates this list [0,1,2,3]
print range(4, 10, 2) # creates this list [4,6,8]

nested = [ [1,2,3], [4,5,6] ] # lists can nest!
print nested[1][2] # prints 6

print [x * 2 for x in nested[0]] # comprehension creates list [2,4,6]
print [x * 2 for x in range(11)] # comprehension creates list [0,2,4,8 ... 20]
print [ [x, x * 2] for x in range(11)] # comprehension creates list [ [0,0],[1,2] [2,4] ... [10,20]]

l1 = [1, 2, 3]
l2 = l1
l3 = [1, 2, 3]
print l1 == l2 # True they are equal
print l1 is l2 # True they are identical
print l1 == l3 # True they are equal
print l1 is l3 # False they are not identical

l2.reverse() # reverses l2, but it also reverses l1!!  Yikes -- python uses pointers
print l2
print l1
