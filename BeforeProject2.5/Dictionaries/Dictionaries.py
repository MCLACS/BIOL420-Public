"""
unorderd, mutable,key value pairs
keys must be ummutable
"""

d = {} # empty dictionary
print d
d = {"Tom" : 24, "Sally" : 18}
print d # notice not ordered
print len(d) # find the lenght, which is 2

print d['Tom'] # review value by key, prints 24

name = 'Tom'
print d[name] # variables can be used for keys

print "Tom" in d # prints true

print d.keys() # prints all keys, in this case "Tom" and "Sally"
print d.values() # prints values, in this case 24 and 18

# iterate the keys
for k in d.keys():
	print k

# iterate the values
for k in d.values():
	print k

del d["Tom"] # remove item by key
print d
d["Sally"] = 19 # change a value
print d

d = {"Tom" : {"age" : 24, "height" : "5'9"}} # nested dictionaries
print d["Tom"]["height"]
print d["Tom"]["height"]

d = {"Tom" : {"cars" : ["toyota", "ford", 'honda'] } } # you can nest lists too
print d
print d["Tom"]["cars"]
print d["Tom"]["cars"][1] # wow, this prints ford

d = {0 : "one", 1 : "two"} # dictionary that looks like - keys are integers
print d[1]

# dictionary as sparse arrrays
# looks like an array of size 1000, but it really just had 2 items
d = {}
d[0] = "hello"
d[999] = "goodbye"
print d
